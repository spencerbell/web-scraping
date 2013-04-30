from scrapy.spider import BaseSpider
from tut.items import TutItem
import json
import pprint

class KmartSpider(BaseSpider):
    name = "kmart"
    allowed_domains = ["kmart.com"]

    # this is a distance hack on geolocation
    # change 50 to 5000, presumably in miles
    start_urls = [ "http://www.kmart.com/shc/s/StoreLocatorSearch?storeId=10151&latitude=40.7275043&longitude=-73.9800645&distance=5000&sourcePage=storeLocator&shcAJAX=1"]

    def parse(self, response):
        stores = json.loads(response.body)        
        
        items = []
        for store in stores['result']:
            item = TutItem()
            item['store_num'] = store['storeId']
            item['address']   = store['address']
            item['address2']  = ''
            item['city']   = store['city']
            item['state']  = store['stat']
            item['zip']    = store['zip']
            item['tel']    = store['phone1']
            item['lat']    = store['latitude']
            item['lng']    = store['longitude']
            
            items.append(item)

        return items

