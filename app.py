from markupsafe import escape
from flask import Flask, url_for, redirect
from flask import render_template
import logging
from flask import request
from Scraper import Scraper

import db

app = Flask(__name__,static_folder="web/static",template_folder='web/templates')

@app.route('/scrape',methods=['GET', 'POST'])
def scrapeProduct(name=None):
    if request.method == 'GET':
        return render_template('scrape.html',name=name)
    elif request.method == 'POST':
        request.form["product-url"]
        sc= Scraper()
        product= sc.scrape(request.form["product-url"])
        return redirect('/product-details/'+str(product.id)+"/")  


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/product-details/<int:product_id>/')
def getProduct(product_id):
    #TODO: CACHINg
    product= db.getProductById(product_id)
    return render_template('product-details.html', product=product)


PRODUCTS_PER_PAGE=50
#TODO: cache and use repo pattern
#https://betterprogramming.pub/simple-flask-pagination-example-4190b12c2e2e
@app.route('/products')
def getAllProducts():
    products= db.getAllProducts()
    print(products)
    return render_template('products.html',products=products)

