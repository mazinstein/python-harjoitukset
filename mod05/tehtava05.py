count = 0


while count < 5:

    Käyttäjätunnus = input("Käyttäjätunnus:")
    Salasana = input("Salasana:")
    count += 1

    if Käyttäjätunnus == "python" and Salasana == "rules":
        print("Welcome")
        break
else:
    print("Access denied")