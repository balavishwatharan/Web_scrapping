# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:39:45 2024

@author: balav
"""

#this is done without using selenium 
#amazon product reviews.
from bs4 import BeautifulSoup as bs
import requests























#requests -> used to connect ide and the page.
#because previously did using a web page driver 
#page -> 200 , then it is good to go






link ='https://www.amazon.in/realme-Feather-Segment-Charging-Slimmest/product-reviews/B0C462M7JP/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
page = requests.get(link)
page
page.content





soup = bs(page.content,'html.parser')#only html code 
soup.prettify()
names = soup.find_all('span',class_='a-profile-name')






cust_name = []
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())
cust_name











cust_name.pop(9)






title = soup.find_all('a',class_='review-title')
review_title = []
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title











#to remove we will use strip function.
#list comprehension
review_title[:] = [titles.strip('\n') for titles in review_title]
review_title

review_title[:] = [titles.lstrip('\n') for titles in review_title]
review_title
#lstrip-> left deleting
#rstrip -> right deleting.

review_title[:] = [titles.rstrip('\n') for titles in review_title]
review_title






rating = soup.find_all('span',class_='a-icon-alt')

rate = []
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate









rate.pop(9)

rate





review = soup.find_all("span",{"data-hook":"review-body"})



review_content = []
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
review_content









review_content[:] = [reviews.lstrip('\n') for reviews in review_content]
review_content

review_content[:] = [reviews.rstrip('\n') for reviews in review_content]
review_content


cust_name - 10
review_title -10
rate -10
review_content -10








import pandas as pd

df = pd.DataFrame()

df['Customer_Name']=cust_name

df['Review_title']=review_title
df['Ratings']=rate
df['Reviews']=review_content










df
df.to_csv(r'D:\reviews.csv',index=True)