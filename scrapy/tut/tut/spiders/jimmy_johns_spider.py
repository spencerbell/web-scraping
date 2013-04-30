from scrapy.spider import BaseSpider
from scrapy.selector import XmlXPathSelector
from tut.items import TutItem



class JimmyJohnsSpider(BaseSpider):
    name = "jimmy_johns"
    allowed_domains = ["jimmyjohns.com"]
    
    # this should pull from a database of zipcodes
    
    start_urls = [
        "http://www.jimmyjohns.com/services/findajjs_lookup.asmx/getLocationsByZip?zip=78701",
        "http://www.jimmyjohns.com/services/findajjs_lookup.asmx/getLocationsByZip?zip=10009"
    ]

    def parse(self, response):
        xxs = XmlXPathSelector(response)
        stores = xxs.select('//locationinfo')
        items = []
        for store in stores:
            item = TutItem()
            item['address']  = store.select('address')
            item['address2'] = store.select('address2')
            items.append(item)

        return items
