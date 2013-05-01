from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
import re
from tut.items import TutItem

class KohlsSpider(CrawlSpider):
    name = 'kohls'
    allowed_domains = ['kohls.com']
    start_urls = ['http://www.kohls.com/stores.shtml']
    #start_urls = ['http://www.kohls.com/stores/az.shtml']
    #start_urls = ['http://www.kohls.com/stores/az/bullheadcity.shtml']

    rules = (

        # these two are special cases. I know this is brittle, so what...
        Rule( SgmlLinkExtractor( allow=('/stores/ny/olean\.shtml', ),), callback='parse_item_special'),
        Rule( SgmlLinkExtractor( allow=('/stores/nh/bedford\.shtml', ),), callback='parse_item_special'),
        Rule(
            SgmlLinkExtractor(
               allow=('/stores/.{2}/.+\.shtml', ),
            ),
            callback='parse_item'
        ),
        Rule(
            SgmlLinkExtractor(
                allow=('/stores/', ),
                restrict_xpaths=('//a[@class="regionlist"]|//a[@class="citylist"]')
            ),
            follow=True
        ),
    )

    def parse_item(self, response):

        hxs = HtmlXPathSelector(response)

        rows = hxs.select('//div[@class="side_location"]')

        items = []

        for row in rows:
            item = TutItem()

            sn = row.select('./span[@class="location-title"]/a/@href').extract()[0]
            ad = row.select('.//span[@class="location-info"]/text()').extract()[1]
            csz = row.select('.//span[@class="location-info"]/text()').extract()

            item['store_num'] = re.search('\d+',sn).group(0)
            item['address']      = csz[0].replace('\n',' ').replace('"','').strip()
            item['city']         = csz[1].split(',')[0]
            item['state']        = re.split('\W',csz[1].split(',')[1].strip())[0]
            item['zip']          = re.split('\W',csz[1].split(',')[1].strip())[1]
            item['tel']          = csz[2]

            items.append(item)

        return items

    def parse_item_special(self, response):

        hxs = HtmlXPathSelector(response)

        rows = hxs.select('//div[@class="side_location"]')

        items = []

        for row in rows:
            item = TutItem()

            sn = row.select('./span[@class="location-title"]/a/@href').extract()[0]
            ad = row.select('.//span[@class="location-info"]/text()').extract()[1]
            csz = row.select('.//span[@class="location-info"]/text()').extract()

            item['store_num'] = re.search('\d+',sn).group(0)
            item['address']      = csz[0].replace('\n',' ').replace('"','').strip()
            item['address2']     = csz[1].replace('\n',' ').replace('"','').strip()
            item['city']         = csz[2].split(',')[0]
            item['state']        = re.split('\W',csz[2].split(',')[1].strip())[0]
            item['zip']          = re.split('\W',csz[2].split(',')[1].strip())[1]
            item['tel']          = csz[3]

            items.append(item)

        return items
