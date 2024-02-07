import scrapy
from utility import cnn_link, save_data


class CnnSpider(scrapy.Spider):
    name = "cnn"
    start_urls = [cnn_link()]

    def parse(self, response) -> None:
        try:  # test it without this try, except protection
            str_resp = response.css('div.sc-bdVaJa.post-content-rendered.render-stellar-contentstyles__Content-sc-9v7nwy-0.erzhuK')
            str_resp = str_resp.css('p::text').getall()
        except:
            print('[INFO]: cnn not updated yet, today')  # ! no need to send this info,
        new_str = " ".join(str_resp[:4])                  # ! data mannager will just say nothing new
        print(f'[INFO]: data is {str_resp[:4]}')

        save_data(new_str, self.name)
        print(f'[INFO] cnn crawling resp: {new_str[:10]}')


class MinutaSpider(scrapy.Spider):
    name = "minuta"
    start_urls = ['https://dennikn.sk/minuta/tema/6826/vojna-na-ukrajine']

    def parse(self, response) -> None:
        str_resp = response.css('div.mnt-article')
        str_resp1 = str_resp.css('strong::text').get()
        str_resp2 = str_resp.css('p::text').get()
        save_data(str_resp1 + str_resp2, self.name)
        print(f'[INFO] minuta crawling resp: {str_resp1[:10]}')


class LiveUaMapSpider(scrapy.Spider):
    name = "liveua"
    start_urls = ['https://liveuamap.com/']

    def parse(self, response) -> None:
        resp = response.css("div.title::text").get()
        save_data(resp, self.name)
        print(f'[INFO]: liveua crawling finished {resp[:20]}')


def main() -> None:  # tests
    '''
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings
    print('we are calling them')
    crawler = CrawlerProcess()
    crawler.start(MinutaSpider)'''


if __name__ == '__main__':
    main()
