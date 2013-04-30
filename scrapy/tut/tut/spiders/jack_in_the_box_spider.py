from scrapy.spider import BaseSpider
from scrapy.selector import XmlXPathSelector
from tut.items import TutItem

class JackInTheBoxSpider(BaseSpider):
    name = "jack_in_the_box"
    allowed_domains = ["jackinthebox.com"]
    
    start_urls = []
    
    states = ['NC','SC','TN','IN','IL','MO','LA','KS','OK','TX','CO','NM','UT','AZ','ID','NV', 'WA','OR','CA','HI']
    
#    for s in states:
      #start_urls.append("http://jackinthebox.com/webservices/get_locations.php?state=%s&city=\%" % s)

    def parse(self, response):
        xxs = XmlXPathSelector(response)
        stores = xxs.select('//locationinfo')
        items = []
        for store in stores:
            item = TutItem()
            item['address']  = store.select('address')
            item['address2'] = store.select('address2')
            items.append(item)

        return items
