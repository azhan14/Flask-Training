import requests
from bs4 import BeautifulSoup as bs
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
