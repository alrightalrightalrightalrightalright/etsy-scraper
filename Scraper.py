import requests
from bs4 import BeautifulSoup
import re
import db
import psycopg2
import Product
"""proxies={
    18.133.228.20:80
138.68.176.163:3128
81.134.57.82:3128
68.183.252.171:3128
193.36.33.3:8080
138.68.141.150:8080
178.62.95.218:8080
94.177.255.108:3128
}
"""
proxies = {
    'http': 'http://178.62.95.218:8080',
    'https': 'https://178.62.95.218:8080',
}
class Scraper:
    _session= requests.Session()
    _baseUrl="https://www.etsy.com"
    _partialUrl="/uk/listing/593579116/plant-enthusiast-bookmarks"
    _requestUrl="https://www.etsy.com/uk/listing/772695061/brass-or-silver-leaf-bookmark-set"
    _headers = { 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7",
        'Host': 'www.etsy.com',      
        'Connection': 'keep-alive', 
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control":"max-age=0",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.441"
        }

    def __init__(self):
        self._session.headers=self._headers
        self._session.proxies= proxies

        r= self._session.get(self._baseUrl) 
        print( 'initial get: ', r.status_code)
  
    def __scrapeProduct(self,soup):
        '''Internal method of the scraping method where pure scraping 
        process happens. It returns the product object.

        :param soup: A bs4 object for scraping source
        :return: The product object that's data has been scraped. '''

        #more pictures of the product can be scraped easily with using find_all.
        #there are also 2 versions of the image, one is normal the other is 2x zoomed
        link= soup.find_all("img",class_="wt-max-width-full"+
        " wt-horizontal-center wt-vertical-center carousel-image wt-rounded")[0]["src"]
        title=soup.find("h1",{"data-listing-id":True}).text.replace("\n","").strip()
        price=soup.find("p",class_="wt-text-title-03 wt-mr-xs-2").text.replace("\n","").strip()
        raw_price= re.findall( "\\d*\\.\\d*",price)[0].replace(".",",") 

        product= Product.Product(title, raw_price,link) 
        return product
        
    def scrape(self,fullUrl):
        '''Scrapes a product with the partial url. Scrapes the image link, title,
        price of the product and stores in a "Product" object. The object is then
        in database with existing configuration. 

        :param partialUrl: The partial url of the product's url to be scraped.
        '''
        fullUrl = fullUrl if fullUrl.startswith('https') else ('https://' + fullUrl)
        r= self._session.get(fullUrl) 
        
        print( 'get: ', r.status_code)
        soup = BeautifulSoup(r.text, 'html.parser')

        product= self.__scrapeProduct(soup)

        db.insertProduct(product)
        #expensive, slow and not thread-safe
        product.id=db.getNextIndex()#can use UUID for id and get rid of this

        return product
