from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from tut.items import TutItem

from urlparse import urlparse, parse_qs

import pprint

class BjsSpider(CrawlSpider):
    name = 'bjs'
    allowed_domains = ['bjs.com']
    start_urls = ['http://www.bjs.com/webapp/wcs/stores/servlet/LocatorAllClubsView?langId=-1&storeId=10201&catalogId=10201']

    rules = (
        Rule(
            SgmlLinkExtractor(
                allow=('/webapp/wcs/stores/servlet/LocatorMapDirectionsView\?catalogId=10201\&langId=-1\&locationId', )
            ),
            callback='parse_item',
            follow=False
        ),
        Rule(
            SgmlLinkExtractor(
                allow=('/webapp/wcs/stores/servlet/LocatorMapDirectionsView', )
            ),
            follow=False,
            callback='parse_item',
        ),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)

        row = hxs.select('//div[@id="sidebar_textinfo"]')

        arr = ''.join(row[0].select('./text()').extract()).replace('\t','').strip().split('\r\n')
        szp = arr[2].split(' ')


        item = TutItem()

        # Get the address
        item['address'] = arr[0]
        item['city']    = arr[1].replace(',','').strip()

        item['state'] = szp[0]
        item['zip']   = szp[1]
        item['tel']   = szp[2]

        item['store_num'] = parse_qs(response.url)['locationId'][0]

        return item
