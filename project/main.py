name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 12:
    print("you are too young to play")
else:
    print("welcome to the game!")

    print("Main menu:")
    print("katso - katso ympärillesi")
    print("liiku - liiku eteenpäin")
    print("apua - näytä ohjeet")
    print("lopeta - lopeta peli")

    command = input("Enter command: katso/liiku/apua/lopeta")

    while command != "lopeta":

        if command == "katso":
            print("katso ympärillesi")
        elif command == "liiku":
            print("liiku eteenpäin")
        elif command == "apua":
            print("näytä ohjeet")
        else:
            print("tuntematon komento")

        print("Main menu:")
        print("katso - katso ympärillesi")
        print("liiku - liiku eteenpäin")
        print("apua - näytä ohjeet")
        print("lopeta - lopeta peli")

        command = input("Enter command: katso/liiku/apua/lopeta")
