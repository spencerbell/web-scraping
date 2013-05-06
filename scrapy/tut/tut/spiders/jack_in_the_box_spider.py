from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tut.items import TutItem

class JackInTheBoxSpider(BaseSpider):
    name = "jack_in_the_box"
    allowed_domains = ["jackinthebox.com"]
    start_urls      = [
        "http://www.jackinthebox.com/locations?q=77095&distance=5000",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        rows = hxs.select('//ol[@class="locations"]/li')

        items = []
        for store in rows:
            item = TutItem()

            csz = store.select('.//li[@class="location-city-state-zip"]/text()')[0].extract()

            item['store_num'] = store.select('./@class').extract()[0].split(' ')[1].replace('location-','')

            item['address']  = store.select('.//li[@class="location-address"]/text()')[0].extract()

            item['city']  = csz.split(', ')[0]
            item['state'] = csz.split(', ')[1].split(' ')[0]
            item['zip']   = csz.split(', ')[1].split(' ')[1]
            item['tel']   = store.select('.//li[@class="location-phone"]/text()')[0].extract().strip()
            item['lat']   = store.select('./@data-lat').extract()[0]
            item['lng']   = store.select('./@data-long').extract()[0]

            items.append(item)

        return items
