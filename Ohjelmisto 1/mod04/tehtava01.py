length = int(input("Anna kuhan pituus senttimetreinä: "))
if length < 42:
    print("Kuha on liian pieni. Laske se takaisin järveen")
    erotus = 42 - length
    print(f"Kuha on {erotus} cm alamittainen")