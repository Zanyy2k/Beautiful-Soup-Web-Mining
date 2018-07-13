# -*- coding: utf-8 -*-
import csv
import time 
import datetime
import urllib2
from bs4 import BeautifulSoup

# Show the starting time of the program
start_time = time.time()
print "Time Started :", datetime.datetime.time(datetime.datetime.now())


x = 0
filename="datasets.csv" #saving data as csv
f=open(filename,"w")
headers="Name,Friend Count,Photo Count,Review Count,Elite Member,Funny Count,Cool Count,Useful Count,Review Stars,Review Length,Reviews\n" #these are the features that are scraped 
f.write(headers)

for _ in range(5):
    print _
    # specify the url
    quote_page = 'https://www.yelp.com/biz/jo-malone-london-costa-mesa?start='+str(x)
    reviews = urllib2.urlopen(quote_page)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(reviews, 'html.parser')

    container=soup.findAll("div",{"class":"review review--with-sidebar"})#the class name where all the features are contained
    
    for i in container:
        
        friend_counter=i.findAll("li",{"class":"friend-count responsive-small-display-inline-block"})
        friend_count=friend_counter[0].b.text
        print 'friend_count',friend_count

        review_counter=i.findAll("li",{"class":"review-count responsive-small-display-inline-block"})
        review_count=review_counter[0].b.text
        print 'review_count',review_count

        photo_counter=i.findAll("li",{"class":"photo-count responsive-small-display-inline-block"})
        if photo_counter:
            photo_count=photo_counter[0].b.text
        else:
            photo_count=0
        print 'photo_count',photo_count

        elite_counter=i.findAll("li",{"class":"is-elite responsive-small-display-inline-block"})
        if elite_counter:
            elite_count=1
        else:
            elite_count=0

        funny_counter=i.findAll("a",{"class":"ybtn ybtn--small funny js-analytics-click"})
        funny_count1=funny_counter[0].findAll("span",{"class":"count"})
        funny_count=funny_count1[0].text
        if funny_count:
            funny_count=funny_count
        else:
            funny_count=0

        cool_counter=i.findAll("a",{"class":"ybtn ybtn--small cool js-analytics-click"})
        cool_count1=cool_counter[0].findAll("span",{"class":"count"})
        cool_count=cool_count1[0].text
        if cool_count:
            cool_count=cool_count
        else:
            cool_count=0

        useful_counter=i.findAll("a",{"class":"ybtn ybtn--small useful js-analytics-click"})
        useful_count1=useful_counter[0].findAll("span",{"class":"count"})
        useful_count=useful_count1[0].text
        if useful_count:
            useful_count=useful_count
        else:
            useful_count=0

        user_counter=i.findAll("a",{"class":"user-display-name js-analytics-click"})
        user_count=user_counter[0].text

        rating_counter=i.findAll("div",{"class":"biz-rating biz-rating-large clearfix"})
        rating_count=rating_counter[0].div.div["title"]
        rating_count=(int(rating_count[0]))

        review_counter=i.findAll("p",{"lang":"en"})
        print review_counter[0]
        review=str(review_counter[0])

        f.write(str(user_count) + "," + str(friend_count) + "," + str(photo_count) + "," + str(review_count)+","+str(elite_count)+","+str(funny_count)+","+str(cool_count)+","+str(useful_count)+","+str(rating_count)+","+str(length_count)+","+str(review)+"\n")

    x=x+20
f.close()


# Show the total time taken for the program
end_time = time.time() - start_time
print "Time Ended", datetime.datetime.time(datetime.datetime.now())
m, s = divmod(end_time, 60)
h, m = divmod(m, 60)
print "%d:%02d:%02d" % (h, m, s)
