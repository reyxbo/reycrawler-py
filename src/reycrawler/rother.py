#!/usr/bin/env python3

"""
@Time    : 2024-01-10
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Other website crawling module.
    Provides data crawling methods for other websites.
"""

from json import loads as json_loads
from reykit.rnet import request
from reykit.rre import search
from reykit.rtime import now

__all__ = (
    'crawl_lunar_calendar',
)

def crawl_lunar_calendar(
    year: int | None = None,
    month: int | None = None
) -> list[dict]:
    """
    Crawl Rili website lunar calendar table.

    Parameters
    ----------
    year : Given year.
        - `None`: Now year.
    month : Given month.
        - `None`: Now month.

    Returns
    -------
    Lunar calendar table.
    """

    # Get parameter.
    now_date = now('date')
    year = year or now_date.year
    month = month or now_date.month
    url = f'https://www.rili.com.cn/rili/json/pc_wnl/{year}/{month:0>2}.js'
    params = {'_': now('timestamp')}

    # Request.
    response = request(url, params)

    # Extract.
    pattern = '{.+}'
    text = search(pattern, response.text)
    data = json_loads(text)
    table = data['data']

    return table
