import math


def pizza_price(diameter, price):
    radius = diameter / 2
    radius_m = radius / 100
    area = math.pi * radius_m ** 2
    result = price / area

    return result


diameter1 = float(input("Enter diameter of pizza 1: "))
price1 = float(input("Enter price of pizza 1: "))

diameter2 = float(input("Enter diameter of pizza 2: "))
price2 = float(input("Enter price of pizza 2: "))

pizza1 = pizza_price(diameter1, price1)
pizza2 = pizza_price(diameter2, price2)

print("Pizza 1:", pizza1, "€/m²")
print("Pizza 2:", pizza2, "€/m²")

if pizza1 < pizza2:
    print("Pizza 1 is cheaper")
else:
    print("Pizza 2 is cheaper")