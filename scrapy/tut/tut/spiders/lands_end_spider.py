from scrapy.spider import BaseSpider
from scrapy.selector import XmlXPathSelector
from tut.items import TutItem

class LandsEndSpider(BaseSpider):
    name = "lands_end"
    allowed_domains = ["landsend.com"]

    start_urls = ["http://www.landsend.com/pp/servlet/StoreLocServlet?lat=29.9108312&lng=-95.6563119&radius=8000&S=S&L=L&C=undefined&N=N"]

    def parse(self, response):
        xxs = XmlXPathSelector(response)
        stores = xxs.select('//marker')
        items = []
        for store in stores:
            item = TutItem()
            item['address']   = store.select('./@address').extract()[0]
            item['city']      = store.select('./@city').extract()[0]
            item['state']     = store.select('./@state').extract()[0]
            item['zip']       = store.select('./@zip').extract()[0]
            item['tel']       = store.select('./@phonenumber').extract()[0]
            item['store_num'] = store.select('./@storenumber').extract()[0]
            item['lat']       = store.select('./@lat').extract()[0]
            item['lng']       = store.select('./@lng').extract()[0]
            items.append(item)

        return items
