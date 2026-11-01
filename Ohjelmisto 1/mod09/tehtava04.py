import random
from tehtava03 import Car

cars = []

for el in range(1, 11):
    el = Car(f"ABC-{el}", random.randint(100, 200))
    cars.append(el)


race_finished = False

while not race_finished:

    for el in cars:
        el.accelerate(random.randint(-10, 15))
        el.drive(1)

    for el in cars:
        if el.travelled_distance >= 10000:
            race_finished = True

for el in cars:
    print(el.registration_number)
    print(el.maximum_speed)
    print(el.speed)
    print(el.travelled_distance)