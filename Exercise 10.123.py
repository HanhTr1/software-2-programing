class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current +=1
            print(f"you are moving up to floor: {self.current}")

    def floor_down(self):
        if self.current > self.bottom:
            self.current -=1
            print(f"you are moving down to floor: {self.current}")

    def go_to_floor(self, floor):
        while self.current < floor:
            self.floor_up()
        while self.current > floor:
            self.floor_down()
        if self.current == floor:
            print(f"you are at floor: {self.current}")


#exercise 10.2
class Building:
    def __init__(self,bottom, top, num_elevator):
        self.num_elevator = []
        for i in range(num_elevator):
            self.num_elevator.append(Elevator(bottom, top))

    def run_elevator(self, elevator, des_floor):
        print(f"Elevator {elevator} is moving to floor {des_floor}")
        self.num_elevator[elevator-1].go_to_floor(des_floor)

#exercise 10.3
    def fire_alarm(self):
        print("FIRE ALARM!!!")
        for i in self.num_elevator:
            i.go_to_floor(i.bottom)



if __name__ == "__main__":
    e = Elevator(1, 20)
    e.go_to_floor(5)
    target_floor=int(input("Enter the floor number:"))
    e.go_to_floor(target_floor)

    print("------------------------------------------------------------------\n")
    building=Building(1, 20, 2)
    building.run_elevator(1,3)
    building.run_elevator(2,5)
    building.fire_alarm()



