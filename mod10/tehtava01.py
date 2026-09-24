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


