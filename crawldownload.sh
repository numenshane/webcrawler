#!/bin/bash
if [ $# -lt 1 ]; then
    echo "input search_keyword"
    exit
fi

# steps
# call scrapy to crawl web pages, pipeline metadata to files
# processing files to abstract href links 
# use download tools to pull data into local storage
# mv local files to certain dir to sync to pcs

keyword=$1
scrapy crawl youtube -a search_flag="$1" -o "$1.json"
sed -i.bak '/googleads/d' "$1.json"
awk -F"\"" '{print $8}' $1.json >> $1.out
for i in `cat $1.out`; do 
    /usr/bin/dl "$i" 
    echo "$i" >> "$1.completed"; 
done
