class Product:
    def __init__(self, produced_by, rating, price, on_sale, sale_percentage, tags):
        self.__produced_by = produced_by
        self.__rating = rating
        self.__price = price
        self.__on_sale = on_sale
        self.__sale_percentage = sale_percentage
        self.__tags = tags

    def get_produced_by(self):
        return self.__produced_by

    def get_rating(self):
        return self.__rating

    def get_price(self):
        return self.__price

    def get_on_sale(self):
        return self.__on_sale

    def get_sale_percentage(self):
        return self.__sale_percentage

    def get_tags(self):
        return self.__tags

class Textile_product (Product):
    def __init__(self, material, by, rating, price, sale, percentage, tags):
        super().__init__(produced_by= by, rating= rating, price= price, on_sale= sale, sale_percentage= percentage, tags= tags)
        self.__material = material

    def get_material(self):
        return self.__material