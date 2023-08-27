from selenium import webdriver
# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re



url = 'https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq'
response = requests.get(url)

"""  This code create 'content.html' file and save the content to here  """
# fileToWrite = open('content.html', 'w', encoding='utf-8')
# fileToWrite.write(response.text)
# fileToWrite.close()
# fileToRead = open('content.html', 'r')
# print(fileToRead.read())
# fileToRead.close()





# if response.status_code == 200:
#     html_content = response.content
#     print('success')
#     # print(html_content)
# else:
#     print('Failed to fetch the website.')
# exit()

# soup = BeautifulSoup(html_content, 'html.parser')
# # print(soup.prettify)
# text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span'])
# scraped_text = ' '.join(element.get_text() for element in text_elements)
# # print(scraped_text)
# print('1111111')








driver = webdriver.Chrome()
# driver.get("https://www.tutorialspoint.com/index.htm")


products = []
prices = []
ratings = []
driver.get('https://www.flipkart.com/6bo/b5g/~cs-hbtuge4qub/pr?sid=6bo%2Cb5g&collection-tab-name=Gaming&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkdhbWluZyBMYXB0b3BzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=26.productCard.PMU_V2_6')


content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for a in soup.find_all('a', href=True, attrs={'class':'_1fQZEK'}):
    name=a.find('div', attrs={'class':'_4rR01T'})
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div', attrs={'class':'_3LWZlK'}) 
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating)
    fileToWrite = open('main.html', 'w', encoding='utf-8')
    fileToWrite.write(content)
    fileToWrite.close()
    fileToRead = open('main.html', 'r', encoding='utf-8')
    print(fileToRead.read())
    fileToRead.close()
driver.quit()


df = pd.DataFrame({'Product Name ' : products,'Price ' : prices,'Rating ' : ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
print(11)
# print(products)
# print(ratings)


# mydataset = {
#     'cars' : ["BMW", "Volvo", "Ford"],
#     'passings' : [3, 7, 2]
# }


# myvar = pd.DataFrame(mydataset)

# print(myvar)
# print(myvar.loc[0])
# print(pd.__version__)