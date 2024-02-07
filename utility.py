from datetime import datetime
from typing import Tuple
from scrapy.crawler import CrawlerRunner
import scrapy
from datamanager import DataManager
import pytz

from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

from crochet import setup
# this is implemented because without it after
# calling spider once it (spider) won't work next time
# setup()


def crawling_processing(site: str, spider: scrapy.Spider) -> Tuple[bool, str]:
    #configure_logging()
    crawler = CrawlerRunner(settings=get_project_settings())
    crawler.crawl(spider)
    crawler.join()

    print(f'[INFO]: Crawling {site}')
    print(f'[INFO]: Crawling finished {site}')

    data_manager = DataManager(site)
    return data_manager.task_manager()


def cnn_link() -> str:
    cnn_time = datetime.now(pytz.timezone('EST')).date()
    cnn_mon = cnn_time.strftime("%m")
    cnn_day = cnn_time.strftime("%d")
    cnn_year = cnn_time.strftime("%Y")
    return f'https://edition.cnn.com/europe/live-news/russia-ukraine-war-news-{cnn_mon}-{cnn_day}-{cnn_year[2:]}/index.html'


def save_data(data: str, file_name: str) -> None:
    with open(f'{file_name}.txt', "w") as file_write:
        file_write.writelines(data)


SITES = {'minuta': 'https://dennikn.sk/minuta/tema/6826/vojna-na-ukrajine',
         'cnn': f"{cnn_link()}",
         'liveua': 'https://liveuamap.com'}
