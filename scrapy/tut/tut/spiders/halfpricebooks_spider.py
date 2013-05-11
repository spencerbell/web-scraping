from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
import re
from tut.items import TutItem

class TargetSpider(CrawlSpider):
    name = "halfpricebooks"
    allowed_domains = ["hpb.com"]
    start_urls = ["http://www.hpb.com/stores/"]

    rules = (
        Rule(SgmlLinkExtractor(allow=('/\d{3}\.html', )), callback='parse_item', follow=True),)

    def parse_item(self, response):

        hxs = HtmlXPathSelector(response)

        item = TutItem()
        acsz = hxs.select('//div[@id="storeAddress"]/p[1]/text()').extract()

        item['address']   = acsz[0].strip()
        item['city']      = acsz[1].strip().split(', ')[0]
        item['state']     = acsz[1].strip().split(', ')[1].split(' ')[0]
        item['zip']       = acsz[1].strip().split(', ')[1].split(' ')[1] 
        item['tel']       = hxs.select('//div[@id="storeHours"]/p[2]/text()')[0].extract().strip()
        item['store_num'] = re.findall(r'\d+',response.url)[0]

        return item
