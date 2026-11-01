sex = input("Anna biologinen sukupuoli (nainen/mies): ").lower()
hemoglobin = int(input("Anna hemoglobin: "))
if sex == "nainen":
    if 117 <= hemoglobin <= 155:
        print("Hemoglobiiniarvo on normaali")
    elif hemoglobin > 155:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on matala")
elif sex == "mies":
    if 134 <= hemoglobin <= 167:
        print("Hemoglobiiniarvo on normaali")
    elif hemoglobin > 167:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on matala")
