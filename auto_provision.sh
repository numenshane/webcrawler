#!/bin/bash
echo "Make sure the pip tool installed already!!!"
pip3 install Scrapy

# start crawler 
scrapy crawl example  >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "suc"
else
    echo "failed"
fi
