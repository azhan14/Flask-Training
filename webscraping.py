# we can scrape through element tagname or class name
import requests
from bs4 import BeautifulSoup as bs
# link = "http://quotes.toscrape.com/"
# res = requests.get(link)
# # print(res.text)
# beautify = bs(res.text,'html.parser')
# # print(beautify.find('a'))
# # print(beautify.find('a').prettify())
# for list_a in beautify.findAll('span',class_='text'):
#     # print(list_a.span)
#     print(list_a.text)

# my testing
# import requests
# from bs4 import BeautifulSoup as bs
# base_link = "http://quotes.toscrape.com/"
# def scrape():       
#         i = 1
#         all_quotes = []
#         while i != 3:                
#                 page = f"page/{i}"
#                 link = f"{base_link}{page}"
#                 res = requests.get(link)
#                 beautify = bs(res.text,'html.parser') 
#                 quotes = beautify.find_all('span',class_='text')
#                 print(quotes)
#                 for quotes in beautify.find_all('span',class_='text'):
#                         all_quotes = quotes.text
#                 # for quote in quotes:
#                 #         all_quotes.append(quote.find(class_='text').get_text)                
#                 print(all_quotes)
#                 i += 1
# scrape()

#sumeet
# import requests
# from bs4 import BeautifulSoup as bs
# base_link = "http://quotes.toscrape.com/"
# def scrape():       
#         i = 1
#         all_quotes = []
#         while i != 3:                
#                 page = f"page/{i}"
#                 link = f"{base_link}{page}"
#                 res = requests.get(link)
#                 beautify = bs(res.text,'html.parser') 
#                 quotes = beautify.find_all(class_='quote')
#                 for quote in quotes:
#                         all_quotes.append(quote.find(class_='text').get_text)
#                 print(all_quotes)                                                
#                 i += 1
# scrape()

# error solving
base_link = "http://quotes.toscrape.com"
def scrape():               
        page = f"/page/1"                       
        while page:    
            link = f"{base_link}{page}"                       
            all_quotes = []                      
            res = requests.get(link)
            beautify = bs(res.text,'html.parser') 
            quotes = beautify.find_all('span',class_='text')              
            for j in quotes:                                                                                        
                    all_quotes.append(j.text)                                                            
            next_btn = beautify.find(class_='next')                              
            page = next_btn.find('a')['href'] if next_btn else None                
            print(all_quotes)
            del all_quotes            
scrape()
