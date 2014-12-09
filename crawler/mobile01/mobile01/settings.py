# -*- coding: utf-8 -*-

# Scrapy settings for mobile01 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os
import sys


BOT_NAME = 'mobile01'

SPIDER_MODULES = ['mobile01.spiders']
NEWSPIDER_MODULE = 'mobile01'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'mobile01.comm <https://github.com/bryanyang0528>'
DEPTH_LIMIT = 2
DOWNLOAD_DELAY = 1

FEED_EXPORTERS = {
	'json': 'crawler_lib.misc.UnicodeJsonItemExporter'
}

DATABASE = {'drivername': 'postgres',
			'host': 'localhost',
			'port': '5432',
			'username': 'bryanyang',
			'password': 'root',
			'database': 'social_listening'}

ITEM_PIPELINES = ['mobile01.pipelines.Mobile01Pipeline']

