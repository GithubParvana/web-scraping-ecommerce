from selenium import webdriver
# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re



# url = 'https://www.flipkart.com/clothing-and-accessories/bottomwear/jeans/women-jeans/pr?sid=clo,vua,k58,4hp&otracker=categorytree&otracker=nmenu_sub_Women_0_Jeans'
# response = requests.get(url)

# # """  This code create 'content.html' file and save the content to here  """
# fileToWrite = open('products-1.html', 'w', encoding='utf-8')
# fileToWrite.write(response.text)
# fileToWrite.close()
# fileToRead = open('products-1.html', 'r', encoding='utf-8')
# print(fileToRead.read())
# fileToRead.close()





# if response.status_code == 200:
#     html_content = response.content
#     print('success')
#     # print(html_content)
# else:
#     print('Failed to fetch the website.')
# exit()







driver = webdriver.Chrome()
# # driver.get("https://www.tutorialspoint.com/index.htm")


products = []
prices = []
ratings = []


driver.get("https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DSamsung&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Samsung")


content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")



for a in soup.find_all('a', href=True, attrs={'class':'_1fQZEK'}):
    name=a.find('div', attrs={'class':'_4rR01T'})
    print(name)
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div', attrs={'class':'_3LWZlK'})
   
    products.append(name.text)
    prices.append(price.text)
    # use .get_text() instead of .text
    ratings.append(rating.get_text() if rating else '')
 
    fileToWrite = open('products-1.html', 'w', encoding='utf-8')
    fileToWrite.write(content)
    fileToWrite.close()
    fileToRead = open('products-1.html', 'r', encoding='utf-8')
    print(fileToRead.read())
    fileToRead.close()
driver.quit()


df = pd.DataFrame({'Product Name ' : products, 'Price ' : prices, 'Rating ' : ratings}) 
df.to_csv('techs.csv', index=False, encoding='utf-8')
print('finished')


