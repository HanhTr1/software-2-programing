class Car:
    def __init__(self, reg_number, max_speed, current_speed=0, travelled_distance=0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_speed: int):
        self.current_speed += change_speed
        if self.current_speed >= self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed <= 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance +=(self.current_speed* hours)

import random
class Race:
    def __init__(self, name, kilometer, car_list):
        self.name = name
        self.distance = kilometer
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10,15))
            car.drive(1.)

    def print_status(self):
        print(self.name+": ")
        print(f'|{"Registered Number"}\t|\t{"Current Speed"}\t|\t{"Travel Distance"}\t|\t')
        print("------------------------------------------------------------")
        for car in self.car_list:
            print(f"|\t\t{car.reg_number:<10}\t|\t\t{car.current_speed:<10}\t|\t\t {car.travelled_distance:<10}\t|\t")
            print("--------------------------------------------------------")
    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance>= self.distance:
                return True
            return False
if __name__ == "__main__":
    car_list=[]
    for i in range(10):
        car_list.append(Car("ABC-"+str(i+i), random.randint(100,200)))

    race1 = Race("Grand  demolition Derby", 8000., car_list)
    h=0
    while not race1.race_finished():
        race1.hour_passes()
        h+=1
        if h % 10 == 0:
            print(f"After {h} hours")
            race1.print_status()
    print(f"Final results after {h} hours")
    race1.print_status()
