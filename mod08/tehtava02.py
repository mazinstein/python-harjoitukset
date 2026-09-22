names = set()
user_input = input("Enter name: ")

def check_name(user_input):
    if user_input in names:
        print("Existing name")
    else:
        names.add(user_input)
        print("New name!")

while user_input != "":

    check_name(user_input)
    user_input = input("Enter name: ")


for el in names:
    print(el)
