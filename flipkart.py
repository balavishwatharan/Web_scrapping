# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:38:54 2024

@author: balav
"""

#pip install beautifulsoup4
#pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup
#BeautifulSoup ->html content is converted into required content.
import pandas as pd
driver = webdriver.Chrome()
from webdriver_manager.chrome import ChromeDriverManager









#driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.flipkart.com/search?q=samsung+mobiles&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_8_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_8_na_na_na&as-pos=3&as-type=RECENT&suggestionId=samsung+mobiles&requestId=aca84b60-38b0-4892-a0e1-1e32cf9af5d4&as-searchtext=samsung%20")

content = driver.page_source#used to get the contents of my pages.
soup = BeautifulSoup(content)
products=[] 
prices=[]
ratings=[]
for i in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
    name=i.find('div', attrs={'class':'_4rR01T'})
    price=i.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rate=i.find('div',attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rate.text)
          
#framing my data    
df = pd.DataFrame({'Product_Name':products,
        'Price':prices,'Ratings':ratings})


df 
df.to_csv(r'D:\mobile_data.csv',index=False)