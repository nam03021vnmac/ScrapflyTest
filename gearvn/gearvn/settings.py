import copy
import os
import logging
from colorlog import ColoredFormatter
import scrapy
from scrapy import logformatter
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
BOT_NAME = 'gearvn'

SPIDER_MODULES = ['gearvn.spiders']
NEWSPIDER_MODULE = 'gearvn.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1
SCRAPFLY_API_KEY = os.environ.get('SCRAPFLY_API_KEY')

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'gearvn.middlewares.GearvnSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'gearvn.middlewares.GearvnDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = 'images'

color_formatter = ColoredFormatter(
    (
        '%(log_color)s%(levelname)-5s%(reset)s '
        '%(white)s[%(asctime)s]%(reset)s'
        '%(cyan)s %(name)s %(funcName)s %(bold_purple)s:%(lineno)d%(reset)s '
        '%(log_color)s%(message)s%(reset)s'
    ),
    datefmt='%y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'blue',
        'INFO': 'green',
        'WARNING': 'bold_purple',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)
_get_handler = copy.copy(scrapy.utils.log._get_handler)


def get_handler_custom(*args, **kwargs):
    handler = _get_handler(*args, **kwargs)
    handler.setFormatter(color_formatter)
    return handler


scrapy.utils.log._get_handler = get_handler_custom


class PoliteLogFormatter(logformatter.LogFormatter):
    def dropped(self, item, exception, response, spider):
        return {
            'level': logging.WARNING,  # lowering the level from logging.WARNING
            'msg': "Dropped: %(exception)s" + os.linesep + "%(item)s",
            'args': {
                'exception': exception,
                'item': item['url'],
            }
        }
