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

