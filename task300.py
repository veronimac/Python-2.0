class Product:
    def __init__(self, name_pr, name_shop, price):
        self.__name_pr = name_pr
        self.__name_shop = name_shop
        self.__price = price

class Sklad:
    def __init__(self, products):
        self.products = []

    def add_pr(self):
        self.products.append(Product(name_pr, name_shop, price))


    def print_info(self, value):
        print(self.products[value])

    def print_info2(self,name):
        info = input('Название товара:')
        print()

    def SortirovkaPoNazvaniyuMagazina(self):
            sorted(products)


    def __add__(self, product2):
        return (self.price + product2.price)
