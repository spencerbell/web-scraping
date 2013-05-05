from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from tut.items import TutItem

class MccoysSpider(CrawlSpider):
    name = 'mccoys'
    allowed_domains = ['mccoys.com']
    start_urls = [
        'http://www.mccoys.com/why-mccoys/store-locator?state=TX',
        'http://www.mccoys.com/why-mccoys/store-locator?state=OTH'
    ]

    rules = (
        Rule(
            SgmlLinkExtractor(
                allow=('/store/', ),
                restrict_xpaths=('//div[@class="columns"]')
            ),
            callback='parse_item',
            follow=True),
    )

    def parse_item(self, response):

        hxs = HtmlXPathSelector(response)
        item = TutItem()

        address = hxs.select('//div[@class="column store-info"]/div[2]/text()').extract()
        item['address'] = address[0].strip()
        item['city']    = address[1].strip().split(', ')[0]
        item['state']   = address[1].strip().split(', ')[1]
        item['zip']     = address[1].strip().split(', ')[2]
        item['tel']     = hxs.select('//div[@class="column store-info"]/div[7]/text()').extract()[0].replace('Call: ','')

        return item
