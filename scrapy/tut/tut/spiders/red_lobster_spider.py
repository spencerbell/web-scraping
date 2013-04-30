from scrapy.spider import BaseSpider
from tut.items import TutItem
import json
import pprint

class RedLobsterSpider(BaseSpider):
    name = "red_lobster"
    allowed_domains = ["redlobster.com"]

    # url string hack. Presumably all the locations are returned

    start_urls = [ "http://www.redlobster.com/locator_g/getdata.aspx?_=&lat=&lon=&table=&search=&state_code="]

    def parse(self, response):
        stores = json.loads(response.body)        
        
        items = []
        for store in stores['results']:
            item = TutItem()
            item['store_num'] = store['RestId']
            item['address']   = store['Address1']
            item['address2']  = ''
            item['city']   = store['city']
            item['state']  = store['state']
            item['zip']    = store['zip']
            item['tel']    = store['phone_number']
            item['lat']    = store['lat']
            item['lng']    = store['lng']
            
            items.append(item)

        return items

