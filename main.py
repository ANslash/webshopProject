from product import *
from user import *
from webShop import *
import PySimpleGUI as sg

ws = Webshop("img\Circle_logo.png", "This is a test shop", "Test shop")

b_usr = Buisness_user("84Fg123", "Arla", {"e-mail": "arla@gmail.dk", "tlf": "12345678"}, "Rådhuspladsen 1", 1000000, "1234567890")

from product import *

t_shirt = Textile_product("cotton", "t-shirt with print", "Jack & Jones", 7, 49.99, False, 0)
jeans = Textile_product("denim", "fashionable jeans", "H&M", 6, 299.99, True, 15)
sweater = Textile_product("wool", "comfy sweater", "Only & Sons", 9, 199.99, False, 0)
under_wear = Textile_product("cotton/polyester", "short underpants", "H&M", 6, 89.99, False, 0)
pc_hardware = Electronics("GPU", "ASUS GeForce RTX 4070 Ti SUPER TUF OC - 16GB GDDR6X RAM", "ASUS", 8, 7999.99, True, 10)
console = Electronics("Gaming console", "Playstation 5", "Sony", 10, 3999.99, False, 0)
barbie = Toys((4, 16), "Science Barbie", "Matell", 7, 99.99, True, 25)
millenium_falcon = Lego("Star Wars", (16, 80), "UCS Millenium Falcon set set number 75192", "The Lego Group", 10, 5999.99, False, 0)

print(f"Inventory: {ws.get_inventory()}")
ws.add_inventory(t_shirt)
ws.add_inventory(jeans)
ws.add_inventory(sweater)
ws.add_inventory(under_wear)
ws.add_inventory(pc_hardware)
ws.add_inventory(console)
ws.add_inventory(millenium_falcon)
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

def show_inventory():
    inventory = []
    for i in range(len(ws.get_inventory())):
        inventory.append(sg.Button(ws.get_inventory()[len(ws.get_inventory()) - (i + 1)].get_name(), key= ws.get_inventory()[len(ws.get_inventory()) - (i + 1)].get_name()))
    return inventory

def show_profile(acc):
    layout = []
    layout.append([sg.Image("img\profile.png")])
    layout.append([sg.Text(acc.get_username())])
    layout.append([sg.Text(acc.get_user().get_bank_balance()), sg.Button(button_text= "Add balance", key= "balance")])
    window = sg.Window(title= "Profile info", layout= layout, size= (1600,800))
    event = window.read(close= True)

    if event[0] == "balance":
        amount = None
        while amount == None or amount < 0:
            amount = int(sg.popup_get_text("Add to balance"))
            if amount < 0:
                sg.popup("The amount can't be negative!")
        acc.get_user().change_balance(amount)

def show_sales():
    sales = []
    for item in ws.get_inventory():
        if item.get_on_sale():
            sales.append(sg.Button(item.get_name(), key= item.get_name()))
    return sales

"""Displays all products that contains the given key in their tags or shares a name with the given key"""
def personal_search(key):
    valid_items = [[]]

    for item in ws.get_inventory():
        if key in item.get_tags() or key == item.get_name():
            valid_items[0].append(sg.Button(button_text= item.get_name()))
    window = sg.Window(title= f"Search for: {key}", layout= valid_items, size= (1600, 800))
    event = window.read(close= True)
    return event[0]

def show_item(event):
    chosen_item = None
    for item in ws.get_inventory():
        if item.get_name() == event:
            chosen_item = item
    if sg.popup_yes_no(f"Add to cart:\n"
                       f"{chosen_item.get_name()}"
                       f"\n{chosen_item.get_price()}"
                       f"\n{chosen_item.get_rating()}", title=chosen_item.get_name()) == "Yes":
        amount = int(sg.popup_get_text("Amount:"))
        ws.get_accounts()[0].add_to_shoppingcart(chosen_item, amount)
def display_basket(acc):
    basket = []
    total_price = 0
    for item in acc.get_shoppingcart():
        basket.append([sg.Text(f"{item[0].get_name()}: {item[0].get_price()} kr,-  x {item[1]}"), sg.Button(button_text= "Remove", key= item[0].get_name())])
        total_price += item[0].get_price() * item[1]
    basket.append([sg.Text(f"Total price: {total_price}")])
    basket.append([sg.Button(button_text= "Buy", key= "buy")])
    window = sg.Window(title= "Shopping cart", layout= basket, size= (1600, 800))
    event = window.read(close= True)
    return event[0]

layout = [
    [sg.Image(ws.get_logo()), sg.Text(ws.get_name()), sg.Button(image_filename= "img\search_but.png", key= "search"), sg.Button(image_filename= "img\profile.png", key= "profile"), sg.Button(image_filename= "img\shopping_basket.png", key= "basket")],
    [sg.Text("Nyhedder:")],
    show_inventory(),
    [sg.Text("Tilbud:")],
    show_sales(),
]

window = sg.Window(ws.get_name(), layout, size= (1000,600))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "search":
        looking_for = sg.popup_get_text("")
        item_name = personal_search(looking_for)
        if item_name != None:
            show_item(item_name)
    elif event == "basket":
        choise = display_basket(ws.get_accounts()[0])
        if choise == "buy":
            ws.get_accounts()[0].buy()
        elif choise != "buy" and choise != None:
            for i in range (len(ws.get_accounts()[0].get_shoppingcart())):
                if ws.get_accounts()[0].get_shoppingcart()[i][0].get_name() == choise:
                    ws.get_accounts()[0].remove_item(i)
    elif event == "profile":
        show_profile(ws.get_accounts()[0])
    else:
        print(event)
        show_item(event)




