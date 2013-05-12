from scrapy.spider import BaseSpider
from tut.items import TutItem
import json

class SearsSpider(BaseSpider):
    name = "sears"
    allowed_domains = ["sears.com"]

    # this is a distance hack on geolocation
    # change 50 to 5000, presumably in miles
    start_urls = ["http://www.sears.com/shc/s/StoreLocatorSearch?storeId=10153&latitude=30.24567279999999&longitude=-97.76883579999998&distance=5000&sourcePage=storeLocator&shcAJAX=1"]

    def parse(self, response):
        stores = json.loads(response.body)

        items = []
        for store in stores['result']:
            item = TutItem()
            item['store_num'] = store['storeId']
            item['address']   = store['address']
            item['city']   = store['city']
            item['state']  = store['stat']
            item['zip']    = store['zip'][0:5]
            item['tel']    = store['phone1']
            item['lat']    = store['latitude']
            item['lng']    = store['longitude']

            items.append(item)

        return items

