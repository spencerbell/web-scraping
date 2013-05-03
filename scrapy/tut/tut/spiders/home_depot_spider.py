from scrapy.spider import BaseSpider
from tut.items import TutItem
import json
import pprint

class HomeDepotSpider(BaseSpider):
    name = "home_depot"
    allowed_domains = ["homedepot.com"]

    # this is a distance hack on geolocation
    # change 50 to 5000, presumably in miles
    start_urls = [ "https://hdapps.homedepot.com/StoreSearchServices/v1.0/kvp/get-stores-by-address/json?address=Austin%2C+Travis+County%2C+TX%2C+78704&radius=5000&maxMatches=5000&truckRental=false&keyCutting=false&toolRental=false&freeWifi=false&hasPropane=false&penskeRental=false&_=1367464116308" ]

    def parse(self, response):
        rows = json.loads(response.body)

        items = []
        for store in rows['stores']:
            item = TutItem()
            item['store_num'] = store['fields']['RecordId']
            item['address']   = store['fields']['address']
            item['address2']  = ''
            item['city']   = store['fields']['city']
            item['state']  = store['fields']['state']
            item['zip']    = store['fields']['postal']
            item['tel']    = store['fields']['user1']
            item['lat']    = store['fields']['Lat']
            item['lng']    = store['fields']['Lng']

            items.append(item)

        return items

