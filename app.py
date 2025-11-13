import requests
from parsel import Selector
import json


all_books=[]

for i in range(1,51):
    r=requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')

    response=Selector(r.text)
    for list in response.xpath('//li/article'):
      title=list.xpath('.//h3/a/text()').get()
     
      img_url=list.xpath('.//img/@src').get()
      url = "https://books.toscrape.com/" +img_url 
      
      price=list.xpath('.//p[@class="price_color"]/text()').get()
      
      rating=list.xpath('.//p/@class').get().split(" ")[1]

      available=list.xpath('.//p[@class="instock availability"]/text()').getall()[1].strip()

      # print(f"TITLE: {title}")
      # print(f"PRICE: {price}")
      # print(f"RATING: {rating}")
      # print(f"URL: {url}")
      # print(f"AVAILABLE: {available}")
      # print(" ")
      book={
        "title":title,
        "price":price,
        "rating":rating,
        "url":url,
        "available":available
      }
      all_books.append(book)
      f = open("books.json", "w", encoding="utf-8")
      f.write(json.dumps(all_books, indent=4, ensure_ascii=False))
      f.close()
      print("data saved")