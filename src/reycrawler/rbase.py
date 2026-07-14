# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2023-12-29
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Base methods.
"""

from fake_useragent import UserAgent
from reykit.rbase import Base

__all__ = (
    'CrawlerBase',
    'ua'
)

class CrawlerBase(Base):
    """
    Crawler base type.
    """

ua = UserAgent()
