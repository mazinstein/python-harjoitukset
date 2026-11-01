cabin_class = input("Anna hyttiluokka: ").upper()
if cabin_class == "LUX":
    print("Parvekkeellinen hytti yläkannella")
elif cabin_class == "A":
    print("Ikkunallinen hytti autokannen yläpuolella")
elif cabin_class == "B":
    print("Ikkunaton hytti autokannen yläpuolella")
elif cabin_class == "C":
    print("Ikkunaton hytti autokannen alapuolella")
else:
    print("Invalid cabin class")
