import requests
from parsel import Selector
import json



all_quotes=[]
base_url='https://quotes.toscrape.com/'
page =1
while True:
    url=f'{base_url}/page/{page}/'


    r=requests.get(url)
    response =Selector(r.text)

    var= response.xpath('//div[@class="quote"]')

    if not var:
        print ("no more page")
        break
    

    for list in var:
    
        text = list.xpath('.//span[@class="text"]/text()').get()
        author = list.xpath('.//small[@class="author"]/text()').get()
        tags = list.xpath('.//div/a[@class="tag"]/text()').getall()
        about_link = list.xpath('.//span/a/@href').get()

        # print(f"QUOTE: {text}")
        # print(f"AUTHOR: {author}")
        # print(f"TAGS: {tags}")
        # print(f"ABOUT LINK: {base_url}{about_link}")
        # print(" ")

        
        quote = {
            "text": text,
            "author": author,
            "tags": tags,
            "about_link": base_url+about_link
            
        } 
    
        all_quotes.append(quote)
    page += 1


    f = open("quotes.json", "w", encoding="utf-8")
    f.write(json.dumps(all_quotes, indent=4, ensure_ascii=False))
    f.close()
    print("data saved")