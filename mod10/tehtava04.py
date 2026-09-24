from mod09.tehtava03 import Car
import random

hours = 0
cars = []

for el in range(1, 11):
    el = Car(f"ABC-{el}", random.randint(100, 200))
    cars.append(el)

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(
                car.registration_number,
                car.maximum_speed,
                car.speed,
                car.travelled_distance
            )


    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True

        return False

race = Race("Grand Demolition Derby", 8000, cars)


while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        race.print_status()

race.print_status()