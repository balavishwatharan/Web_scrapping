# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:41:21 2024

@author: balav
"""

import requests   
# Importing requests to extract content from a url
from bs4 import BeautifulSoup as bs 
#pip install bs4
# Beautifulsoup is for web scrapping...used to scrap specific content 
import re 


import matplotlib.pyplot as plt
import wordcloud

from wordcloud import WordCloud,STOPWORDS


# creating empty reviews list 
amazon_reviews=[]


for i in range(1,5):
  ip=[]  
  
  url = "https://www.amazon.in/Mi-163-9-Inches-Ultra-Android/product-reviews/B08B9GQMHZ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
  response = requests.get(url)
  soup = bs(response.content,"html.parser")
  # creating soup object to iterate over the extracted content 
  reviews = soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"})# Extracting the content under specific tags  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)  
  amazon_reviews=amazon_reviews+ip  # adding the reviews of one page to empty list which in future contains all the reviews


# writng reviews in a text file 
with open(r"C:\Users\Ranjith\Desktop\IMAGECON\MACHINE LEARNING\ML -CODING\webscrape_text mining\webscrape_text mining\Reviews.tsv","w",encoding='utf8') as output:
    output.write(str(amazon_reviews))
    
    
    
# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(amazon_reviews)


# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ",ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ",ip_rev_string)
ip_rev_string


# words that contained in 
ip_reviews_words = ip_rev_string.split(" ")
ip_reviews_words

#here we are going to eliminate the stoping words
ip_reviews_words = [w for w in ip_reviews_words if not w in STOPWORDS]
ip_reviews_words


# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(ip_reviews_words)
ip_rev_string
# WordCloud can be performed on the string inputs. That is the reason we have combined 
# entire reviews into single paragraph
# Simple word cloud

plt.figure(dpi=300)
wordcloud_ip = WordCloud(
                      background_color='white',
                      width=1920,
                      height=1080
                     ).generate(ip_rev_string)

plt.imshow(wordcloud_ip)