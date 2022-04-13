from scrapy import Item, Field



class GearvnItem(Item):
    # define the fields for your item here like:
    name = Field()
    images = Field()
    image_urls = Field()
