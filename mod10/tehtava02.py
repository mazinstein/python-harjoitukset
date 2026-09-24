class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f"Floor is {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Floor is {self.current_floor}")

    def go_to_floor(self, destination):
        if destination > self.current_floor:
            while self.current_floor != destination:
                self.floor_up()


        else:
            while self.current_floor != destination:
                self.floor_down()




class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = []

        for _ in range(number_of_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination):
        index = elevator_number - 1
        elevator = self.elevators[index]
        elevator.go_to_floor(destination)

building = Building(1, 10, 3)
building.run_elevator(2, 5)