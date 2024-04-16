class Account:
    def __init__(self, user, username, password, ):
        self.__user: User = user
        self.__username: str = username
        self.__password: str = password
        self.__shopping_cart: list = []
        self.__shopping_history: dict = {}

    def remove_Item(self, item_index):
        self.__shopping_cart.pop(item_index)

    def get_ShoppingCart(self):
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
        for item in self.get_ShoppingCart():
            total += item[0].get_price() * item[1]

        if self.__premium:
            total = total * .95
        else:
            total += currier_fee

        if total <= self.get_user().get_bank_balance():
            self.get_user().draw_from_bank_balance(total)
            different_products = len(self.get_ShoppingCart())
            for i in range(different_products):
                self.remove_Item(0)
        else:
            print("NOT ENOUGH BALANCE TO COMPLETE PURCHASE!!!")

class Buisness_account (Account):
    def __init__(self, user, username, password):
        super().__init__(username= username, password= password)
        self.__type = type
        self.__user: Buisness_user = user

    def getType(self):
        return self.__type

    def buy(self):
        total = 0
        currier_fee = 10

        for item in self.get_ShoppingCart():
            if self.__type in item.getTags():
                total += item.get_price() * 0.85
            else:
                total += item.get_price()

        total += currier_fee

        if self.get_user().get_bank_balance() >= total:
            self.get_user().draw_from_bank_balance(total)
            different_product = len(self.get_ShoppingCart())
            for i in range(different_product):
                self.remove_Item(0)
            else:
                print("NOT ENOUGH BALANCE TO COMPLETE PURCHASE!!!")


