import requests
from parsel import Selector
import json



all_quotes=[]
base_url='https://quotes.toscrape.com/'

for i in range(100):
    r=requests.get(f'https://quotes.toscrape.com/page/{i}/')
    response =Selector(r.text)
    

    for list in response.xpath('//div[@class="quote"]'):
    
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
    # logic for next page
    next_page =response.xpath('//li[@class="next"]/a/@href').get()
    if next_page:
        url=base_url+next_page
    else:
        break


    f = open("quotes.json", "w", encoding="utf-8")
    f.write(json.dumps(all_quotes, indent=4, ensure_ascii=False))
    f.close()
    print("data saved")