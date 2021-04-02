#01/04/2021 00:53 bismillah
#02/04/2021 11.51 kemik tamam
#https://miro.medium.com/max/601/1*O_PEPxbh_9OqdkMtOU4jkA.png böyle bişe yap
from Scraper import Scraper
import initDb
import db

print("sea")

db.initDatabase()

sc= Scraper()
#p1= sc.scrape("https://www.etsy.com/uk/listing/906009346/silver-daisy-adjustable-ring?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-1&plkey=16c356a37204a9dff8271e579030c7c1d2665f36%3A906009346&frs=1&bes=1")

db.getAllProducts()
db.getProductById(4124123)