inventory = []


def katso():
    print("katso ympärillesi")


def liiku():
    print("liiku eteenpäin")


def add_item():
    item = input("Enter item: ")
    inventory.append(item)


def show_inventory():
    print("Inventory:")
    for item in inventory:
        print(item)


def apua():
    print("näytä ohjeet")


name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 12:
    print("you are too young to play")
else:
    print("welcome to the game!")

    print("Main menu:")
    print("katso - katso ympärillesi")
    print("liiku - liiku eteenpäin")
    print("add - add item")
    print("inventory - show inventory")
    print("apua - näytä ohjeet")
    print("lopeta - lopeta peli")

    command = input("Enter command: katso/liiku/add/inventory/apua/lopeta")

    while command != "lopeta":

        if command == "katso":
            katso()
        elif command == "liiku":
            liiku()
        elif command == "add":
            add_item()
        elif command == "inventory":
            show_inventory()
        elif command == "apua":
            apua()
        else:
            print("tuntematon komento")

        print("Main menu:")
        print("katso - katso ympärillesi")
        print("liiku - liiku eteenpäin")
        print("add - add item")
        print("inventory - show inventory")
        print("apua - näytä ohjeet")
        print("lopeta - lopeta peli")

        command = input("Enter command: katso/liiku/add/inventory/apua/lopeta")