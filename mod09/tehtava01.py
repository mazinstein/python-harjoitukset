class Car:
    def __init__(self,registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.speed = 0
        self.travelled_distance = 0

car = Car("ABC-123",142)

print(car.registration_number)
print(car.speed)
print(car.travelled_distance)
print(car.maximum_speed)