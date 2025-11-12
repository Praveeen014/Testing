# import requests
# from parsel import Selector


# for i in range(1,3):
#     r=requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')

#     response=Selector(r.text)
#     for list in response.xpath('//li/article'):
#       title=list.xpath('.//h3/a/text()').get()
     
#       img_url=list.xpath('.//img/@src').get()
#       url = "https://books.toscrape.com/" +img_url 
      
#       price=list.xpath('.//p[@class="price_color"]/text()').get()
      
#       rating=list.xpath('.//p/@class').get().split(" ")[1]

#       avaialble=list.xpath('.//p[@class="instock availability"]/text()').getall()[1].strip()

#       print(f"TITLE: {title}")
#       print(f"PRICE: {price}")
#       print(f"RATING: {rating}")
#       print(f"URL: {url}")
#       print(f"AVAILABLE: {avaialble}")
#       print(" ")




print("hello world")