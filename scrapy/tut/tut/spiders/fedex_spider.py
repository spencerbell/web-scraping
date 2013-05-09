from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request

import json
from tut.items import TutItem
from pprint import pprint

class FedExSpider(CrawlSpider):
    name = 'fedex'
    allowed_domains = ['local.fedex.com']
    start_urls = ['http://local.fedex.com/sitemap.html']
    #start_urls = ['http://local.fedex.com/dc/washington/']

    rules = (
        Rule(
            SgmlLinkExtractor(
                allow=('dc/washington/$'),
            ),
            callback='parse_state',
        ),
        Rule(
            SgmlLinkExtractor(
                allow=('/[a-z]{2}/'),
                deny=('/[a-z]{2}/.+','/us/*'),
                restrict_xpaths=('//*[@id="col-main"]/div/div/div[2]/div/div[1]/div[2]/div//a')
            ),
            follow=True),
        Rule(
            SgmlLinkExtractor(
                allow=('/[a-z]{2}/.+/'),
                deny=('/us/*'),
                restrict_xpaths=('/html/body/div/div[4]/div/div/div/div/div[3]/div/div/div[2]/div')
            ),
            callback='parse_state',
        )
    )

    def parse_state(self,response):
        return Request(response.url + '?ajax=true&show=100', callback=self.parse_item)
        #return Request(response.url+ '?ajax=true&filters[]=fedex&filters[]=office&show=100', dont_filter=True)

    def parse_item(self, response):

        rows = json.loads(response.body)

        items = []
        for row in rows['results']:
            item = TutItem()
            item['address']  = row['address']
            item['address2'] = row['bldg']
            item['city']     = row['city']
            item['state']    = row['state']
            item['zip']      = row['zipcode']
            item['tel']      = row['stor_phone']
            item['store_num']= row['fxo_branch_id']
            item['lat']      = row['latitude']
            item['lng']      = row['longitude']

            items.append(item)

        return items
