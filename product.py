class Product:
    def __init__(self):
        self.__produced_by = produced_by
        self.__rating = rating
        self.__price = price
        self.__on_sale = on_sale
        self.__sale_percentage = sale_percentage
        self.__tags = tags

    def getProduced_by(self):
        return self.__produced_by

    def getRating(self):
        return self.__rating

    def getPrice(self):
        return self.__price

    def getOn_sale(self):
        return self.__on_sale

    def getSale_percentage(self):
        return self.__sale_percentage

    def getTags(self):
        return self.__tags

class Textile_product:
    def __init__(self, material):
        self.__material = material

    def getMaterial(self):
        return self.__material
