#!/bin/bash

python manage.py resetar_tabela --drop-all

cd crawling

scrapy crawl adorocinema