# -*- coding: utf-8 -*-
import csv
import time 
import datetime
import urllib3
from bs4 import BeautifulSoup

# Show the starting time of the program
start_time = time.time()
print("Time Started : ", datetime.datetime.time(datetime.datetime.now()))

filename="book.csv" #saving data as csv
f=open(filename,"w")
headers="Title\n" #these are the features that are scraped 
f.write(headers)

# specify the url
quote_page = 'https://www.bookdepository.com/'

req = urllib3.PoolManager()
books = req.request('GET', quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(books.data, 'html.parser')

container=soup.findAll("div",{"class":"item-info"})#the class name where all the features are contained

for i in container:
    
    title_counter=i.find("h3",{"class":"title"})
    title_count=title_counter.text
    print('title_count : ',title_count)

    f.write(str(title_count))

f.close()

# Show the total time taken for the program
end_time = time.time() - start_time
print("Time Ended", datetime.datetime.time(datetime.datetime.now()))
m, s = divmod(end_time, 60)
h, m = divmod(m, 60)
print("%d:%02d:%02d" % (h, m, s))
