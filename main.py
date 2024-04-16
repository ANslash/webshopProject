from account import *
from product import *
from user import *
from webShop import *

ws = Webshop("img\circle_logo.png", "This is a test shop", "Test shop")

b_usr = Buisness_user("84Fg123", "Arla", {"e-mail": "arla@gmail.dk", "tlf": "12345678"}, "Rådhuspladsen 1", 1000000, "1234567890")

t_prod = Textile_product("Nylon", "Polo", 4, 10, False, 0, ["Textile"])

print(f"Inventory: {ws.get_inventory()}")
ws.add_inventory(t_prod)
print(f"Inventory: {ws.get_inventory()}")

ws.create_new_account("buisness", b_usr, "Arla", "Vi_elsker_ko")

print(ws.get_accounts()[0].get_user().get_CVR())

print("shopping")
print(ws.get_accounts()[0].get_shoppingcart())
ws.get_accounts()[0].add_to_shoppingcart(ws.get_inventory()[0], 10)
print(ws.get_accounts()[0].get_shoppingcart())

print("buying")
print(ws.get_accounts()[0].get_user().get_bank_balance())
ws.get_accounts()[0].buy()
print(ws.get_accounts()[0].get_user().get_bank_balance())