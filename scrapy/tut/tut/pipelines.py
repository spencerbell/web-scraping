# Define your item pipelines here
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem

class TutPipeline(object):
    def process_item(self, item, spider):
        return item

class MySQLStorePipeline(object):
  def __init__(self):
    self.conn = MySQLdb.connect(user='user', 'passwd', 'dbname', 'host', charset="utf8", use_unicode=True)
    self.cursor = self.conn.cursor()

def process_item(self, item, spider):    
    try:
        self.cursor.execute("""INSERT INTO store_location (
          store_name, 
          store_id,
          address,
          address2,
          city,
          state,
          zip,
          lat,
          lng,
          tel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)""", 
                       (item['book_name'].encode('utf-8'), 
                        item['price'].encode('utf-8')))

        self.conn.commit()


    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])


    return item