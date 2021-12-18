# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from filme.models import Filme

def clean_sinopse(param):
    return param.strip()

class CrawlingPipeline:
    
    
    def process_item(self, item, spider):
        
        sinopse = clean_sinopse(item['sinopse'])
        
        Filme.objects.create(
            titulo= item['titulo'],
            sinopse= sinopse,
            link= item['link']
        )
        return item
