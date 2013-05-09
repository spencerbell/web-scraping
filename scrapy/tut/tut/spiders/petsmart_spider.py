from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
import re
from tut.items import TutItem

class TargetSpider(CrawlSpider):
    name = 'petsmart'
    allowed_domains = ['petsmart.com']
    start_urls = ['http://stores.petsmart.com/all']

    rules = (
            Rule(SgmlLinkExtractor(allow=('/all/US/', )), callback='parse_item', follow=True),)

    def parse_item(self, response):

        hxs = HtmlXPathSelector(response)

        rows = hxs.select('//table[@class="locations stores-table striped"][1]//tr')
        rows.pop(0)

        items = []
        for row in rows:
            item = TutItem()


            # Get the address
            item['address'] = row.select('td[2]/text()')[0].extract()

            csz = row.select('td[3]/text()')[0].extract().split(', ')

            item['city']  = csz[0]
            item['state'] = csz[1]
            item['zip']   = csz[2]

            item['tel']   = row.select('td[4]/text()')[0].extract()
            item['store_num'] = row.select('td[1]/a/@href')[0].extract().split('/')[::-1][0]


            items.append(item)

        return items
