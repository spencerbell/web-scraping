# Define your item pipelines here
import sys
import hashlib
from scrapy import signals
from scrapy.exceptions import DropItem

class TutPipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicateItemPipeline(object):

    def __init__(self):
        self.address_seen = set()

    def process_item(self, item, spider):
        if item['address']+item['city'] in self.address_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.address_seen.add(item['address'] + item['city'])
            return item
