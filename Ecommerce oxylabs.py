import requests
from parsel import Selector
import json


all_Game=[]
for i in range(1,95):
    r=requests.get(f'https://sandbox.oxylabs.io/products?page={i}')
    response=Selector(r.text)


    script_json=response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
    data = json.loads(script_json)  
    products = data['props']['pageProps']['products']

# maping={"A":1,"B":2,"C":3,"D":4,"E":5}


    for product in products:
        title = product.get('game_name')
        genere = product.get('genre')
        description = product.get('description')
        url= product.get('url')
        type= product.get('type')
        # rating = product.get('rating')
        instock= product.get('inStock')

        if instock:
            instock = "In Stock"
        else:
            instock = "Out of Stock"


        online = {
            "title": title,
            "genere": genere,
            "description": description, 
            "url": url,
            "type": type,
            "instock": instock
            
        }
        all_Game.append(online)

    print(f'{i} saved')

with open('oxylabs_games.json', 'w' , encoding="utf-8") as f:
    json.dump(all_Game, f, indent=4, ensure_ascii=False)

    
    























# using xpath 
# for i in range(1,2):
#     r=requests.get(f'https://sandbox.oxylabs.io/products?page={i}')
#     response=Selector(r.text)

#     for list in response.xpath('//div[@class="product-card css-e8at8d eag3qlw10"]'):
#         # img_url=list.xpath('.//img/@src').get()
#         # url = 'https://sandbox.oxylabs.io/' +img_url 

#         title=list.xpath('.//a/h4[@class="title css-7u5e79 eag3qlw7"]/text()').get()

#         genere=list.xpath('.//p/span[@class="css-1pewyd6 eag3qlw8"]/text()').getall()

#         description=list.xpath('.//p[@class="description css-cput12 eag3qlw5"]/text()').get()

#         price=list.xpath('.//div[@class="price-wrapper css-li4v8k eag3qlw4"]/text()').get()

#         script_json=list.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        

#         # print(f"URL: {img_url}")        
#         print(f"TITLE: {title}")
#         print(f"GENERE: {genere}")  
#         print(f"DESCRIPTION: {description}")
#         print(f"PRICE: {price}")
#         # print(f"RATING: {rating}")
#         # print(f"AVAILABILITY: {availability}")
#         print(" ")