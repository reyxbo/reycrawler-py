[中文](README_zh.md)

# reycrawler

**reycrawler** is a Python method integration package for web crawling.

It provides crawling methods for websites such as Baidu, Douban, Sina, Toutiao, and Weibo, and integrates crawling capabilities for different websites through a modular design.

It also provides browser-based human-like page crawling methods, which can simulate browser behavior to retrieve page HTML content and bypass anti-crawling mechanisms on some websites.

It is suitable for website data collection, information retrieval, and web crawling scenarios.

## Features

* Provides web crawling methods
* Integrates crawling methods for multiple well-known websites
* Supports crawling Baidu-related websites
* Supports crawling Douban
* Supports crawling Sina
* Supports crawling Toutiao
* Supports crawling Weibo
* Provides crawling methods for other websites
* Supports human-like page crawling through browsers
* Supports retrieving page HTML content through browsers
* Supports browser crawling tasks based on database polling
* Provides unified method exports
* Modular design, allowing crawling methods for different websites to be used as needed

---

## Installation

Requires **Python 3.12 or higher**.

```bash
pip install reycrawler
```

---

# Modules

reycrawler is divided into multiple modules by functionality and target website, with each module responsible for different website crawling and base functionality.

## `rall` — All import methods

**Unified export module.**

Provides convenient exports of all reycrawler module methods. It allows the functionality provided by the package to be imported centrally, reducing the need to import from multiple modules separately.

---

## `rbaidu` — Crawl Baidu website methods

**Baidu website crawling module.**

Provides data crawling methods for Baidu-related websites.

Mainly includes:

* Baijiahao website data crawling
* Baidu Translate website data crawling
* Other Baidu-related website data crawling

---

## `rbase` — Base methods

**Base methods module.**

Provides common base methods and shared dependencies used by other crawler modules.

It is mainly used to support the operation of other modules and provide common base functionality.

---

## `rbrowser` — Browser methods

**Browser crawling module.**

Uses human-like browser control to crawl webpage HTML content, allowing anti-crawling mechanisms on some websites to be bypassed.

Browser crawling tasks are provided through database polling, allowing other programs to invoke browser crawling capabilities through database tasks.

Mainly provides:

* Human-like browser control
* Webpage HTML content retrieval
* Browser crawling for anti-crawling scenarios
* Crawling tasks based on database polling
* Browser crawling integration methods

---

## `rdouban` — Crawl Douban website methods

**Douban website crawling module.**

Provides data crawling methods for Douban.

Mainly includes:

* Movie and TV ranking data crawling
* Movie and TV details crawling
* Other Douban website data crawling

---

## `rother` — Crawl other website methods

**Other website crawling module.**

Provides data crawling methods for other websites.

Mainly includes:

* Chinese lunar calendar date information crawling
* Other website data crawling

---

## `rsina` — Crawl Sina website methods

**Sina website crawling module.**

Provides data crawling methods for Sina.

Mainly includes:

* Securities market search result crawling
* Stock detail data crawling
* Other Sina website data crawling

---

## `rtoutiao` — Crawl Toutiao website methods

**Toutiao website crawling module.**

Provides data crawling methods for Toutiao.

Mainly includes:

* Hot news data crawling
* Other Toutiao website data crawling

---

## `rweibo` — Crawl Weibo website methods

**Weibo website crawling module.**

Provides data crawling methods for Weibo.

Mainly includes:

* Hot news data crawling
* Other Weibo website data crawling

---

# Module Overview

| Module     | Function                                        |
| ---------- | ----------------------------------------------- |
| `rall`     | Unified export of all methods                   |
| `rbase`    | Base methods and shared dependencies            |
| `rbrowser` | Human-like browser control and webpage crawling |
| `rbaidu`   | Baidu-related website crawling                  |
| `rdouban`  | Douban website crawling                         |
| `rother`   | Other website crawling                          |
| `rsina`    | Sina website crawling                           |
| `rtoutiao` | Toutiao website crawling                        |
| `rweibo`   | Weibo website crawling                          |

---

# Dependencies

Main dependencies:

* `bs4`
* `fake_useragent`
* `reydb`
* `reykit`
* `selenium`

---

# Project Information

| Project    | Information                                                    |
| ---------- | -------------------------------------------------------------- |
| Name       | `reycrawler`                                                   |
| Version    | `1.0.18`                                                       |
| Python     | `>=3.12`                                                       |
| Author     | `Rey`                                                          |
| Email      | `reyxbo@163.com`                                               |
| Homepage   | [reyxbo.com](https://www.reyxbo.com/release/python/reycrawler) |
| Repository | [reycrawler-py](https://github.com/reyxbo/reycrawler-py.git)   |

## Keywords

`rey` · `reyxbo` · `crawler` · `crawl-web` · `browser` · `baidu` · `douban` · `sina` · `toutiao` · `weibo`
