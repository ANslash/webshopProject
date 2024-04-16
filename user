class User:
    def __init__(self, name, contact_info, address, bank_balance, card_info):
        self.__name = name
        self.__contact_info = contact_info
        self.__address = address
        self.__bank_balance = bank_balance
        self.__card_info = card_info

    def getName(self):
        return self.__name

    def getContact_info(self):
        return self.__contact_info

    def getAddress(self):
        return self.__address

    def getBank_balance(self):
        return self.__bank_balance

    def getCard_info(self):
        return self.__card_info

    def change_balance(self, amount):
        self.__bank_balance += amount

class Business_user(User):
    def __init__(self, cvr, name, contact_info, address, bank_balance, card_info):
        super().__init__(name= name, contact_info= contact_info, address= address, bank_balance= bank_balance, card_info= card_info)
        self.__cvr = cvr

    def getCVR(self):
        return self.__cvr

class Private_user(User):
    def __init__(self, contacts, name, contact_info, address, bank_balance, card_info):
        super().__init__(name= name, contact_info= contact_info, address= address, bank_balance= bank_balance, card_info= card_info)
        self.__contacts = contacts

    def getContacts(self):
        return self.__contacts
