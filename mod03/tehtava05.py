leivisk = float(input())
naula = float(input())
luoti = float(input())

total = (luoti * 32 * 20 + naula * 20 + leivisk) * 2

kg = int(total // 1000)
gr = total % 1000

print("massa nykymittojen mukaan:")
print(f"{kg} kilogrammaa ja {gr} grammaa.")