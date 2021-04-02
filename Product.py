class Product:
    def __init__(self, title, price, link,id=None):
        self.id=id
        self.title= title
        self.price=price
        self.link = link  
    
    @staticmethod
    def tupleToObj(t):
        #tuple: (id, title, link, price)
        return Product(t[1],t[3],t[2],t[0])