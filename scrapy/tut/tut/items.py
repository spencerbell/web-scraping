# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TutItem(Item):
    # define the fields for your item here like:
    # name = Field()
    store_num = Field()
    address   = Field()
    address2  = Field()
    city      = Field()
    state     = Field()
    zip       = Field()
    tel       = Field()
    lat       = Field()
    lng       = Field()