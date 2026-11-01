class Car:
    def __init__(self,registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.speed + change
        self.speed = new_speed
        if new_speed < 0:
            self.speed = 0
        elif new_speed > self.maximum_speed:
            self.speed = self.maximum_speed

    def drive(self, hours):
        distance = self.speed * hours
        self.travelled_distance += distance

class ElectricalCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

ElectricCar = ElectricalCar("ABC-15", 180, 52.5)
gasolineCar = GasolineCar("ACD-123", 165, 32.3)

ElectricCar.accelerate(80)
gasolineCar.accelerate(70)

ElectricCar.drive(3)
gasolineCar.drive(3)

print(ElectricCar.travelled_distance)
print(gasolineCar.travelled_distance)
