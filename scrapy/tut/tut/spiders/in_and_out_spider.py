from scrapy.spider import BaseSpider
from scrapy.selector import XmlXPathSelector
from tut.items import TutItem

class InAndOutSpider(BaseSpider):
    name = "in_and_out"
    allowed_domains = ["in-and-out.com"]

    start_urls = ["http://hosted.where2getit.com/innout/newdesign/ajax?&xml_request=%3Crequest%3E%3Cappkey%3E409AAB8A-E1C4-11DD-9152-B8EE3B999D57%3C%2Fappkey%3E%3Cgeoip%3E1%3C%2Fgeoip%3E%3Cformdata+id%3D%22getlist%22%3E%3Corder%3Ecity%3C%2Forder%3E%3Cobjectname%3EStoreLocator%3C%2Fobjectname%3E%3Cwhere%3E%3Cuid%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fuid%3E%3Cstate%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fstate%3E%3Cstore%3E%3Cin%3E%3C%2Fin%3E%3C%2Fstore%3E%3C%2Fwhere%3E%3C%2Fformdata%3E%3C%2Frequest%3E"]

    def parse(self, response):
        xxs = XmlXPathSelector(response)
        stores = xxs.select('//poi')
        items = []
        for store in stores:
            item = TutItem()
            item['address']   = store.select('address1/text()').extract()
            item['address2']  = store.select('address2/text()').extract()
            item['city']      = store.select('city/text()').extract()
            item['state']     = store.select('state/text()').extract()
            item['zip']       = store.select('postalcode/text()').extract()
            item['tel']       = store.select('phone/text()').extract()
            item['store_num'] = store.select('clientkey/text()').extract()
            item['lat']       = store.select('latitude/text()').extract()
            item['lng']       = store.select('longitude/text()').extract()
            items.append(item)

        return items
