from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tut.items import TutItem
from pprint import pprint

class CirclekSpider(BaseSpider):
    name = "biglots"
    allowed_domains = ["biglots.com"]

    start_urls = [ "http://www.biglots.com/store-locator?fromSearch=true&zipCode=77095&city=&state=&mileRange=4000" ]

    def parse(self, response):
        hxs    = HtmlXPathSelector(response)
        stores = hxs.select('//div[@class="store-address"]')

        # we do this becuse they do not return properly formatted json

        items = []

        for store in stores:
            item = TutItem()
            #pprint(store.select('//span').extract())

            item['address']  = store.select('./span[2]/text()').extract()[0]
            item['city']     = store.select('./span[3]/text()').extract()[0].split(', ')[0]
            item['state']    = store.select('./span[3]/text()').extract()[0].split(', ')[1].split(' ')[0]
            item['zip']      = store.select('./span[3]/text()').extract()[0].split(', ')[1].split(' ')[1]
            item['store_num'] = store.select('./span[1]/a/text()').extract()[0].split(' ')[-1]

            items.append(item)

        return items

