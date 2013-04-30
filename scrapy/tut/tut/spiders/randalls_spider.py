from scrapy.spider import BaseSpider
from scrapy.selector import XmlXPathSelector
from scrapy.http import FormRequest, Request

from tut.items import TutItem

class RandallsSpider(BaseSpider):
    name = "randalls"
    allowed_domains = ["m.randalls.com"]

    start_urls = ["http://m.randalls.com/StoreLocator/GetClosestStores"]

        #yield FormRequest.from_response( response, method="post", formdata={'{"latitude":"30.24567279999999","longitude":"-97.7688357999999","resultCount":5000,"searchRadius":5000,"department":"stores"}'}, callback=self.parseLocations)

    def make_requests_from_url(self, url):
        """A method that receives a URL and returns a Request object (or a list of Request objects) to scrape.
        This method is used to construct the initial requests in the start_requests() method,
        and is typically used to convert urls to requests.
        """
        return Request(url,
            method="post",
            body='{"latitude":"30.24567279999999","longitude":"-97.7688357999999","resultCount":   5000,"searchRadius":5000,"department":"stores"}',
            headers={'Content-Type':'application/json'},
            meta = {'start_url': url})

    def parse(self, response):
        xxs = XmlXPathSelector(response)
        stores = xxs.select('//poi')
        items = []
        for store in stores:
            item = TutItem()
            item['address']  = store.select('address')
            item['address2'] = store.select('address2')
            items.append(item)

        return items
