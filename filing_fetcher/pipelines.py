# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline

class FilingFetcherPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        filename = super.file_path(self, request, response=None, info=None)
        year = request.meta.get('Accounts.LastMadeUpDate','').split('-')[0]
        return filename.replace("full/", "full/" + year + '_' + request.meta.get('CompanyNumber',''))
