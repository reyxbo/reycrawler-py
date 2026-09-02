#!/usr/bin/env python3

"""
@Time    : 2023-12-29
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Base methods module.
    Provides common base methods and shared dependencies used by other crawler modules.
    It is mainly used to support the operation of other modules and provide common base functionality.
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
