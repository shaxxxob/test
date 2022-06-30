class product():
    def __init__(self):
        self.n = []
    def add(self, a):
        return self.n.append(a)
    def remove(self, b):
        self.n.remove(b)
    def dis(self):
        return (self.n)
 
obj = product()
 
choice = 1
while choice != 0:
    print("0. Выход")
    print("1. Добавить продукт")
    print("2. Добавить цену")
    print("3. Удалить")
    print("4. Вывести на экран")
    choice = int(input("Выберите одно из этих значений: "))
    if choice == 1:
        n=str(input("Введите продукт для добавления в список: "))
        obj.add(n)
        print("Список: ", obj.dis())
    elif choice == 2:
        n=int(input("Введите цену добавленного продукта для добавления в список: "))
        obj.add(n)
        print("Список: ", obj.dis())
 
    elif choice == 3:
        n=int(input("Введите продукт/цену, которое хотите удалить: "))
        obj.remove(n)
        print("Список: ", obj.dis())
 
    elif choice == 4:
        print("Список: ", obj.dis())
    elif choice == 0:
        print("Выход")
    else:
        print("Неверный выбор")
 
print()

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