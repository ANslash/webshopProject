import account

class Webshop:

    def __init__(self, inventory, logo, info, accDB, name):
        self.__inventory: list = inventory
        self.__logo: str = logo
        self.__info: str = info
        self.__accDB: list = accDB
        self.__name: str = name

    def get_inventory(self):
        return self.__inventory

    def get_logo(self):
        return self.__logo

    def get_info(self):
        return self.__info

    def get_accounts(self):
        return self.__accDB

    def get_name(self):
        return self.__name

    def add_inventory(self, product):
        self.__inventory.append(product)

    def create_new_account(self, type, user, username, password):

        match type:
            case "basic":
                new_account = account.Basic_account(user, username, password)
            case "buisness":
                new_account = account.Buisness_account(user, username, password)

        self.__accDB.append(new_account)