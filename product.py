class Product:
    def __init__(self, name, produced_by, rating, price, on_sale, sale_percentage, tags):
        self.__name: str = name
        self.__produced_by: str = produced_by
        self.__rating: int = rating
        self.__price: float = price
        self.__on_sale: bool = on_sale
        self.__sale_percentage: float = sale_percentage
        self.__tags: list = tags

    def __str__(self):
        return self.__name

    def get_produced_by(self):
        return self.__produced_by

    def get_rating(self):
        return self.__rating

    def get_price(self):
        return self.__price

    def get_on_sale(self):
        return self.__on_sale

    def set_sale_percentage(self, persentage):
        self.__sale_percentage = persentage

    def get_sale_percentage(self):
        return self.__sale_percentage

    def get_tags(self):
        return self.__tags

    def add_tag(self, tag):
        self.__tags.append(tag)

    def remove_tag(self, tag):
        self.__tags.remove(tag)

class Textile_product (Product):
    def __init__(self, material, name, by, rating, price, sale, percentage):
        super().__init__(name= name, produced_by= by, rating= rating, price= price, on_sale= sale, sale_percentage= percentage, tags= ["Textile"])
        self.__material: str = material

    def get_material(self):
        return self.__material

class Electronics (Product):
    def __init__(self, components, name, by, rating, price, sale, percentage):
        super().__init__(name= name, produced_by= by, rating= rating, price= price, on_sale= sale, sale_percentage= percentage, tags= ["Electronic"])
        self.__components: list = components

    def get_components(self):
        return self.__components

class Computer (Electronics):
    def __init__(self, component, name, by, rating, price, sale, percentage, system):
        super().__init__(name= name, by= by, rating= rating, price= price, sale= sale, percentage= percentage, components= component)
        self.add_tag("Computer")
        self.__operatingsystem = system

    def get_system(self):
        return self.__operatingsystem

class Toys (Product):
    def __init__(self, age_range, name, by, rating, price, sale, percentage):
        super().__init__(name= name, produced_by= by, rating= rating, price= price, on_sale= sale, sale_percentage= percentage, tags= ["Toy"])
        self.__age_range: tuple = age_range

    def get_age_range(self):
        return self.__age_range

class Lego (Toys):
    def __init__(self, franchise, age_range, name, by, rating, price, sale, percentage):
        super().__init__(franchise= franchise, age_range= age_range, name= name, produced_by= by, rating= rating, price= price, on_sale= sale, sale_percentage= percentage, tags= ["Toy"])
        self.__franchise
        self.__age_range: tuple = age_range

    def get_franchise(self):
        return self.__franchise
