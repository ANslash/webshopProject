from user import *
class Account:
    def __init__(self, user, username, password):
        self.__user: User = user
        self.__username: str = username
        self.__password: str = password
        self.__shopping_cart: list = []
        self.__shopping_history: dict = {}

    def remove_item(self, item_index):
        self.__shopping_cart.pop(item_index)

    def get_shoppingcart(self):
        return self.__shopping_cart

    def decrease_item_ammount(self, item_index):
        amount = self.__shopping_cart[item_index][1]
        if amount == 1:
            self.remove_Item(item_index)
        else:
            self.__shopping_cart[item_index][1] -= 1

    def increase_item_amount(self, item_index):
        amount =  self.__shopping_cart[item_index][1]
        self.__shopping_cart[item_index][1] += 1

    def get_shopping_history(self):
        return self.__shopping_history

    def get_username(self):
        return self.__username

    def add_to_shoppingcart(self, product, amount):
        index = 0
        already_in_cart = False
        for item in self.get_shoppingcart():
            if item[0].get_name() == product.get_name():
                already_in_cart = True
                for i in range (amount):
                    self.increase_item_amount(index)
            index += 1
        if not already_in_cart:
            self.__shopping_cart.append([product, amount])

    def get_user(self):
        return self.__user

    def __get_password(self):
        return self.__password

class Basic_account (Account):
    def __init__(self, user, username, password, premium):
        super().__init__(user= user, username= username, password= password)
        self.__premium: bool = premium

    def is_premium(self):
        return self.__premium

    def buy(self):
        total = 0
        currier_fee = 10
        for item in self.get_shoppingcart():
            total += item[0].get_price() * item[1]

        if self.__premium:
            total = total * .95
        else:
            total += currier_fee

        if total <= self.get_user().get_bank_balance():
            self.get_user().change_balance(-total)
            different_products = len(self.get_shoppingcart())
            for i in range(different_products):
                self.remove_item(0)
        else:
            print("NOT ENOUGH BALANCE TO COMPLETE PURCHASE!!!")

class Buisness_account (Account):
    def __init__(self, user, username, password, type):
        super().__init__(user= user,username= username, password= password)
        self.__type = type
        self.__user: Buisness_user = user

    def get_type(self):
        return self.__type

    def buy(self):
        total = 0
        currier_fee = 10

        for item in self.get_shoppingcart():
            if self.__type in item[0].get_tags():
                total += item[0].get_price() * item[1] * 0.85
            else:
                total += item[0].get_price() * item[1]

        total += currier_fee

        if self.get_user().get_bank_balance() >= total:
            self.get_user().change_balance(-total)
            different_product = len(self.get_shoppingcart())
            for i in range(different_product):
                self.remove_item(0)
        else:
            print("NOT ENOUGH BALANCE TO COMPLETE PURCHASE!!!")


