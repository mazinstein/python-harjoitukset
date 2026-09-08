def gallons_to_litres(gallons):
    litres = gallons * 3.785
    return litres


gallons = float(input("Enter gallons: "))

while gallons >= 0:
    result = gallons_to_litres(gallons)
    print(result)

    gallons = float(input("Enter gallons: "))