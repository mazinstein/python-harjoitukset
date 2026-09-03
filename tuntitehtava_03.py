age = int(input("Anna ikä: "))
laji = str(input("Anna laji (ihminen/tonttu/robotti):"))

if age >= 18 and laji == "ihminen":
    print("Voit tilata: kahvi, viini")
elif age >= 100 and laji == "tonttu":
    print("Voit tilata: kahvi, glögi")
elif laji == "robotti":
    print("Voit tilata: kahvi, öljy")