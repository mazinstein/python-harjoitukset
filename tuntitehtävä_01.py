height = float(input("Anna seinän korkeus: "))
width = float(input("Anna seinän leveys: "))
coverage = float(input("Anna maalin peittoala: "))
S = height * width
paint = S / coverage

print(paint)