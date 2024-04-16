class User:
    def __init__(self, name, contact_info, address, bank_balance, card_info):
        self.__name = name
        self.__contact_info = contact_info
        self.__address = address
        self.__bank_balance = bank_balance
        self.__card_info = card_info

    def get_name(self):
        return self.__name

    def get_contact_info(self):
        return self.__contact_info

    def get_address(self):
        return self.__address

    def get_bank_balance(self):
        return self.__bank_balance

    def get_card_info(self):
        return self.__card_info

    def change_balance(self, amount):
        self.__bank_balance += amount

class Buisness_user(User):
    def __init__(self, cvr, name, contact_info, address, bank_balance, card_info):
        super().__init__(name= name, contact_info= contact_info, address= address, bank_balance= bank_balance, card_info= card_info)
        self.__cvr = cvr

    def get_CVR(self):
        return self.__cvr

class Private_user(User):
    def __init__(self, contacts, name, contact_info, address, bank_balance, card_info):
        super().__init__(name= name, contact_info= contact_info, address= address, bank_balance= bank_balance, card_info= card_info)
        self.__contacts = contacts

    def get_contacts(self):
        return self.__contacts