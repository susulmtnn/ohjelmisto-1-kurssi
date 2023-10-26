'''Jatka edellisen tehtävän ohjelmaa siten, että Talo-
luokassa on parametriton metodi palohälytys, joka käskee kaikki
hissit pohjakerrokseen.
 Jatka pääohjelmaa siten, että talossasi tulee palohälytys.'''


class Elevator:

    count = 0
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.location = bottom_floor
        Elevator.count += 1
        self.name = Elevator.count
        print(f"new elevator is born! Elevator is number {self.name}. Its bottom floor {self.bottom_floor}, top floor {self.top_floor} and location {self.location}")

    def move_up(self):
        self.location += 1
        print(f"You have moved up one floor. Now you're at {self.location}")

    def move_down(self):
        self.location -= 1
        print(f"You have down one floor. Now you're at {self.location}")

    def travel_to_floor(self, target_floor):
        while self.location != target_floor:
            if target_floor > self.location:
                self.move_up()
            elif target_floor < self.location:
                self.move_down()
            else:
                print("You are in the target floor! Congrats")
        else:
            print(f"You have arrived to the target floor: {target_floor}")

class House:
    def __init__(self, bottom_floor, top_floor, nbr_of_elevators):
        self.bottom_floor_of_house = bottom_floor
        self.top_floor_of_house = top_floor
        self.nbr_of_elevators = nbr_of_elevators
        i = nbr_of_elevators
        elevators = []
        while i > 0:
            new_elevator = Elevator(self.bottom_floor_of_house, self.top_floor_of_house)
            elevators.append(new_elevator)
            i -= 1
        self.elevators_list = elevators

    def drive_elevator(self, nbr, target):
        self.elevator_nbr = nbr
        self.target_floor = target
        self.current_location = self.elevators_list[nbr-1].location
        print(f"So you wish to drive the elevator {nbr}. Target floor is {self.target_floor}. Current floor is {self.elevators_list[nbr-1].location}")
        self.elevators_list[nbr-1].travel_to_floor(target)

    def fire_alarm(self):
        print("Fire alarm - All elevators go down")
        for i in self.elevators_list:
            self.drive_elevator(i.name, self.bottom_floor_of_house)
            print(f"{i.name} has escaped the fire.")




talo = House(0, 5, 3)
#talo.drive_elevator(2, 5)
#talo.drive_elevator(1, 4)
talo.drive_elevator(3, 0)
talo.fire_alarm()

