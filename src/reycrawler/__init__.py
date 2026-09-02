#!/usr/bin/env python3

"""
@Time    : 2023-02-19
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Method integration package for web crawling.

Modules
-------
rall : Unified export module.
    Provides convenient exports of all reycrawler module methods.
    It allows the functionality provided by the package to be imported centrally, reducing the need to import from multiple modules separately.
rbaidu : Baidu website crawling module.
    Provides data crawling methods for Baidu-related websites.
rbase : Base methods module.
    Provides common base methods and shared dependencies used by other crawler modules.
    It is mainly used to support the operation of other modules and provide common base functionality.
rbrowser : Browser crawling module.
    Uses human-like browser control to crawl webpage HTML content, allowing anti-crawling mechanisms on some websites to be bypassed.
    Browser crawling tasks are provided through database polling, allowing other programs to invoke browser crawling capabilities through database tasks.
rdouban : Douban website crawling module.
    Provides data crawling methods for Douban.
rother : Other website crawling module.
    Provides data crawling methods for other websites.
rsina : Sina website crawling module.
    Provides data crawling methods for Sina.
rtoutiao : Toutiao website crawling module.
    Provides data crawling methods for Toutiao.
rweibo : Weibo website crawling module.
    Provides data crawling methods for Weibo.
"""
