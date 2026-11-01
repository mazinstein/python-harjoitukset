airports = {}


def add_airport():
    code = input("ICAO: ")
    name = input("Airport: ")
    airports[code] = name


def get_airport():
    code = input("ICAO: ")
    if code in airports:
        print(airports[code])
    else:
        print("Airport not found")

command = input("Command: ")

while command != "quit":
    if command == "add":
        add_airport()
    elif command == "get":
        get_airport()
    else:
        print("Unknown command")

    command = input("Command: ")