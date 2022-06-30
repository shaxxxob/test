import pickle
class Products:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def sum(self):
        print(list[1].sum + list[3].sum + list[5].sum + list[7].sum)
    
my_products = [ ]        
my_products.append(Products('Tomato', 15))
my_products.append(Products('Apple', 12))
my_products.append(Products('Banana', 20))
my_products.append(Products('Oil', 130))


for obj in my_products:
    print(obj.name, obj.price, sep =' ')

with open('d:/products.txt', 'wb+' ) as f:
    pickle.dump(my_products, f)
    
# ser = pickle.dumps(my_products)
#print(ser)
#deser = pickle.loads(ser)
#print(deser, t)
#deser.show()


#f = open('products.bin', 'wb')
#pickle.dump(my_products, f)
#f.close()
#f = open('products.bin', 'rb')
#my_products2 = pickle.load(f)
#print('my_products2 = ', my_products2 )
#f.close()