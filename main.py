from product import *
from user import *
from webShop import *
import PySimpleGUI as sg

ws = Webshop("img\circle_logo.png", "This is a test shop", "Test shop")

b_usr = Buisness_user("84Fg123", "Arla", {"e-mail": "arla@gmail.dk", "tlf": "12345678"}, "Rådhuspladsen 1", 1000000, "1234567890")

t_prod = Textile_product("Nylon", "Pants", "Polo", 4, 10, False, 0, ["Textile"])
sweater_prod = Textile_product("Wool", "Sweater", "Grannt", 10, 32, True, 12, ["Textile"])
m_prod = Product("Milk", "Arla", 4, 14, False, 0, ["Mælk"])

print(f"Inventory: {ws.get_inventory()}")
ws.add_inventory(t_prod)
ws.add_inventory(sweater_prod)
ws.add_inventory(m_prod)
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
        inventory.append(sg.Button(ws.get_inventory()[len(ws.get_inventory()) - (i + 1)].get_name()))
    return inventory

def show_sales():
    sales = []
    for item in ws.get_inventory():
        if item.get_on_sale():
            sales.append(sg.Button(item.get_name()))
    return sales

def personal_search(tag):
    valid_items = [[]]

    for item in ws.get_inventory():
        if tag in item.get_tags() or tag == item.get_name():
            valid_items[0].append(sg.Button(button_text= item.get_name()))
    window = sg.Window(title= f"Search for: {tag}", layout= valid_items, size= (1600, 800))
    event = window.read(close= True)
    return event[0]

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



print(ws.get_inventory())
print(show_inventory())

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

    print(event)

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "search":
        looking_for = sg.popup_get_text("")
        item_name = personal_search(looking_for)
        if item_name != None:
            for item in ws.get_inventory():
                if item.get_name() == item_name:
                    chosen_item = item
            if sg.popup_yes_no(f"Add to cart:\n"
                            f"{chosen_item.get_name()}"
                            f"\n{chosen_item.get_price()}"
                            f"\n{chosen_item.get_rating()}", title= chosen_item.get_name()) == "Yes":
                amount = int(sg.popup_get_text("Amount:"))
                ws.get_accounts()[0].add_to_shoppingcart(chosen_item, amount)
    elif event == "basket":
        choise = display_basket(ws.get_accounts()[0])
        if choise == "buy":
            ws.get_accounts()[0].buy()
        elif choise != "buy" and choise != None:
            for i in range (len(ws.get_accounts()[0].get_shoppingcart())):
                print("-----")
                print(ws.get_accounts()[0].get_shoppingcart()[i][0].get_name())
                    #ws.get_accounts()[0].remove_item(i)




