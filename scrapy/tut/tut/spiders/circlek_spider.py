from scrapy.spider import BaseSpider
from scrapy.http import FormRequest, Request
from scrapy.selector import XmlXPathSelector
import json
from tut.items import TutItem
import pprint

class CirclekSpider(BaseSpider):
    name = "circlek"
    allowed_domains = ["circlek.com"]

    start_urls = [ "http://www.circlek.com/CircleK/SitesService.asmx/GetStores" ]

    def start_requests(self):
        return [FormRequest(url  = self.start_urls[0],
                    formdata={
                        'optionsString' : 'false:false:false:false:false:false:false:30.24567279999999:-97.76883579999998:50000'
                    },
                    headers = {
                        'Referer' : 'http://www.circlek.com/CircleK/FindAStore.aspx',
                        'X-Requested-With' : 'XMLHttpRequest'
                    }
                )]

    def parse(self, response):
        xxs    = XmlXPathSelector(response)

        # we do this becuse they do not return properly formatted json
        tmpstr = xxs.select('//*/text()')[0].extract().replace('"D"',"'D'")

        stores = json.loads(tmpstr)

        items = []

        for store in stores:
            item = TutItem()

            item['address']  = store['Address']
            item['city']     = store['City']
            item['state']    = store['State']
            item['zip']      = store['Zip']
            item['lat']      = store['Latitude']
            item['lng']      = store['Longitude']
            item['store_num'] = store['Store']

            items.append(item)

        return items

