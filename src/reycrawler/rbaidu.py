#!/usr/bin/env python3

"""
@Time    : 2024-01-10
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Baidu website crawling module.
    Provides data crawling methods for Baidu-related websites.
"""

from json import loads as json_loads
from reydb import DatabaseEngine
from reykit.rnet import request
from reykit.rre import search, findall
from reykit.rtime import now

from .rbrowser import crawl_page_use_db

__all__ = (
    'crawl_baidu_calendar',
    'crawl_baidu_bjh_articles',
    'crawl_baidu_bjh_article_images'
)

def crawl_baidu_calendar(
    year: int | None = None,
    month: int | None = None
) -> list[dict]:
    """
    Crawl Baidu website calendar table.

    Parameters
    ----------
    year : Given year.
        - `None`: Now year.
    month : Given month.
        - `None`: Now month.

    Returns
    -------
    Calendar table.
    """

    # Get parameter.
    now_date = now('date')
    year = year or now_date.year
    month = month or now_date.month
    if month == 12:
        month = 1
    else:
        month += 1
    url = 'https://opendata.baidu.com/data/inner'
    query = f'{year}年{month}月'
    params = {
        'tn': 'reserved_all_res_tn',
        'type': 'json',
        'resource_id': '52109',
        'query': query,
        'apiType': 'yearMonthData',
        'cb': 'jsonp_1706670926975_94318'
    }

    # Request.
    response = request(url, params)

    # Extract.
    pattern = '{.+}'
    text = search(pattern, response.text)
    data: dict = json_loads(text)
    table: list[dict] = data['Result'][0]['DisplayData']['resultData']['tplData']['data']['almanac']

    # Convert.
    week_dict = {
        '一': 0,
        '二': 1,
        '三': 2,
        '四': 3,
        '五': 4,
        '六': 5,
        '日': 6
    }
    table = [
        {
            'year': int(row['year']),
            'month': int(row['month']),
            'day': int(row['day']),
            'week': week_dict[row['cnDay']],
            'work': row.get('status'),
            'festival': [
                {
                    'name': info['name'],
                    'url': info.get('baikeUrl')
                }
                for info in row.get('festivalInfoList', [])
            ],
            'animal': row['animal'],
            'lunar_year': int(row['lunarYear']),
            'lunar_month': int(row['lunarMonth']),
            'lunar_day': int(row['lunarDate']),
            'gz_year': row['gzYear'],
            'gz_month': row['gzMonth'],
            'gz_day': row['gzDate'],
            'suit': row['suit'].split('.'),
            'avoid': row['avoid'].split('.'),
            'url': row['yjJumpUrl']
        }
        for row in table
    ]
    for row in table:
        week = row['week']
        work = row['work']
        match work:
            case None:
                is_work_day = week not in (5, 6)
            case '1':
                is_work_day = False
            case '2':
                is_work_day = True
        row['work'] = is_work_day

    return table

def crawl_baidu_bjh_articles(
    db_engine: DatabaseEngine,
    bjh_id: int
) -> list[str]:
    """
    Crawl Baidu website BJH all article URLs list.
    Note: dependent `rbrowser.CrawlerBrowser` type.

    Parameters
    ----------
    db_engine : Database engine instance.
    bjh_id : BJH ID.

    Returns
    -------
    Article URLs list.
    """

    # Crawl.
    url = 'https://author.baidu.com/home'
    params = {
        'from': 'bjh_article',
        'app_id': bjh_id
    }
    html = crawl_page_use_db(
        db_engine,
        url,
        params,
        'crawl morn bless image home.'
    )

    # Extract.
    pattern = r'https://baijiahao.baidu.com/s\?id=\d+'
    urls: tuple[str] = findall(pattern, html)

    return urls

def crawl_baidu_bjh_article_images(
    db_engine: DatabaseEngine,
    article_url: str
) -> list[str]:
    """
    Crawl baidu website BJH article all image URLs list.
    Note: dependent `rbrowser.CrawlerBrowser` type.

    Parameters
    ----------
    db_engine : Database engine instance.
    article_url : BJH article URL.

    Returns
    -------
    Image URLs list.
    """

    # Crawl.
    html = crawl_page_use_db(
        db_engine,
        article_url,
        note='Crawl morn bless image article.'
    )

    # Extract.
    pattern = r'https://pics\d.baidu.com/feed/[0-9a-f]{40}.jpeg@f_auto\?token=[0-9a-f]{32}'
    urls: tuple[str] = findall(pattern, html)

    return urls
