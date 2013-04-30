from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
import re
from tut.items import TutItem

class TargetSpider(CrawlSpider):
    name = 'target'
    allowed_domains = ['target.com']
    start_urls = ['http://www.target.com/store-locator/state-listing']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        # Rule(SgmlLinkExtractor(allow=('state-result?stateCode=[A-Z]{2}', ), deny=('subsection\.php', ))),

        # Extract links matching '' and parse them with the spider's method parse_item
        Rule(SgmlLinkExtractor(allow=('/store-locator/state-result\?stateCode=', )), callback='parse_item', follow=True),)

    def parse_item(self, response):

        hxs = HtmlXPathSelector(response)

        rows = hxs.select('//tr[@class="data-row"]')

        items = []
        for row in rows:
            item = TutItem()


            # Get the address
            item['address'] = row.select('td[3]/text()').extract()


            # Get the city,state,zip output: [u'Albany', u' CA94710']
            ctz = row.select('td[4]/text()').extract()[0].split(',')

            item['city']  = ctz[0]
            item['state'] = ctz[1].strip()[0:2] # get the first two characters
            item['zip']   = ctz[1].strip()[2:] # get the remaining chars

            sn = row.select('td[2]/a/@href').extract()[0]
            item['store_num'] = re.search('storeNumber=(\d+)',sn).group(1)
            items.append(item)

        return items
