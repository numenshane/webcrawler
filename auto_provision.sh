#!/bin/bash
pip install Scrapy
cp /usr/lib64/python2.6/lib-dynload/_sqlite3.so /usr/local/lib/python2.7/sqlite3/
pip install chardet

# start crawler 
scrapy crawl example  >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "suc"
else
    echo "failed"
fi
