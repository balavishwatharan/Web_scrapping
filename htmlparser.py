# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:39:52 2024

@author: balav
"""

from bs4 import BeautifulSoup as bs
import requests

link = 'https://www.amazon.in/realme-5G%EF%BC%88Stellar-External-Segments-Supervooc/product-reviews/B0CGDQRR9Y/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&'

cust_name = []
for i in range(1,5):
    
    payload = {'pageNumber': str(i)}
    page = requests.get(link,params=payload)

    soup = bs(page.content,'html.parser')

    names = soup.find_all('span',class_='a-profile-name')

    for j in range(0,len(names)):
        cust_name .append(names[j].get_text())