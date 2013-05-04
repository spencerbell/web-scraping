from scrapy.spider import BaseSpider
from scrapy.selector import XmlXPathSelector
from scrapy.http import FormRequest, Request
import json
from tut.items import TutItem

class WendysSpider(BaseSpider):
    name = "wendys"
    allowed_domains = ["wendys.com"]

    start_urls = [
            "http://www.mapquestapi.com/search/v1/radius?key=Gmjtd%7Clu612dubnh%2C70%3Do5-lwz0l&origin=anchorage,AK&hostedData=MQA.MQ_34663_wendys_stores&radius=5999&maxMatches=4999",
            "http://www.mapquestapi.com/search/v1/radius?key=Gmjtd%7Clu612dubnh%2C70%3Do5-lwz0l&origin=toronto,ON&hostedData=MQA.MQ_34663_wendys_stores&radius=5999&maxMatches=4999",
            "http://www.mapquestapi.com/search/v1/radius?key=Gmjtd%7Clu612dubnh%2C70%3Do5-lwz0l&origin=vancouver,bc&hostedData=MQA.MQ_34663_wendys_stores&radius=5999&maxMatches=4999",
            "http://www.mapquestapi.com/search/v1/radius?key=Gmjtd%7Clu612dubnh%2C70%3Do5-lwz0l&origin=san%20%juan,pr&hostedData=MQA.MQ_34663_wendys_stores&radius=5999&maxMatches=4999",
            "http://www.mapquestapi.com/search/v1/radius?key=Gmjtd%7Clu612dubnh%2C70%3Do5-lwz0l&origin=new%20%york,ny&hostedData=MQA.MQ_34663_wendys_stores&radius=5999&maxMatches=4999",
            "http://www.mapquestapi.com/search/v1/radius?key=Gmjtd%7Clu612dubnh%2C70%3Do5-lwz0l&origin=miami,fl&hostedData=MQA.MQ_34663_wendys_stores&radius=5999&maxMatches=4999",
            "http://www.mapquestapi.com/search/v1/radius?key=Gmjtd%7Clu612dubnh%2C70%3Do5-lwz0l&origin=austin,TX&hostedData=MQA.MQ_34663_wendys_stores&radius=5999&maxMatches=4999",
            "http://www.mapquestapi.com/search/v1/radius?key=Gmjtd%7Clu612dubnh%2C70%3Do5-lwz0l&origin=chicago,IL&hostedData=MQA.MQ_34663_wendys_stores&radius=5999&maxMatches=4999",
            "http://www.mapquestapi.com/search/v1/radius?key=Gmjtd%7Clu612dubnh%2C70%3Do5-lwz0l&origin=los%20%angeles,CA&hostedData=MQA.MQ_34663_wendys_stores&radius=5999&maxMatches=4999"

    ]

    def make_requests_from_url(self,url):
        return Request(url  = url,
                    headers = {
                        'Referer' : 'http://www.wendys.com/store-locator/index.jsp',
                        'Host'    : 'www.mapquestapi.com'
                    }
                )

    def parse(self, response):
        stores = json.loads(response.body)

        items = []

        for store in stores['searchResults']:
            item = TutItem()

            item['address']  = store['fields']['address']
            item['city']     = store['fields']['city']
            item['state']    = store['fields']['state']
            item['zip']      = store['fields']['postal']
            item['tel']      = store['fields']['phone']
            item['lat']      = store['fields']['Lat']
            item['lng']      = store['fields']['Lng']
            item['store_num'] = store['fields']['RecordId']

            items.append(item)

        return items
