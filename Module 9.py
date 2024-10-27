class Car:
    def __init__(self, reg_number, max_speed, current_speed=0, travelled_distance=0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
#exercise 9.2
    def accelerate(self, change_speed: int):
        self.current_speed += change_speed
        if self.current_speed >= self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed <= 0:
            self.current_speed = 0
#exercise 9.3
    def drive(self, hours):
        self.travelled_distance +=(self.current_speed* hours)
#Exercise 9.1
if __name__ == '__main__':

    new_car = Car(reg_number='ABC-123', max_speed=142)
    print("-----------exercise 9.1--------------")
    print(f"Car {new_car.reg_number} has maximum speed of {new_car.max_speed}km/h,"
          f" current speed is {new_car.current_speed}km/h and travelled distance is {new_car.travelled_distance}km")

    print("-----------exercise 9.2--------------")
    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)
    print(f"Current speed after change is {new_car.current_speed} km/h, travel distance is {new_car.travelled_distance}")
    new_car.accelerate(-200)
    print(f"Current speed after brake is {new_car.current_speed} km/h, travel distance is {new_car.travelled_distance}")

    print("-----------exercise 9.3--------------")
    new_car.travelled_distance = 2000
    new_car.accelerate(60)
    new_car.drive(1.5)
    print(f"The travelled distance is {new_car.travelled_distance} km")
#exercise 9.4
    print("-----------exercise 9.4--------------")
    import random
    car_list=[]
    for i in range(10):
        car_list.append(Car(f"Car ABC-"+str(i+1), random.randint(100, 200)))
    travelled_distance=0
    while travelled_distance < 10000:
        for car in car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1.)
            travelled_distance = max(car.travelled_distance,travelled_distance)
    print(f'|{"Registered Number"}\t|\t{"Max Speed":<6}\t|\t{"Current Speed":<6}\t|\t{"Travel Distance"}\t|\t')
    print("----------------------------------------------------------------------------")
    for car in car_list:

        print(f"|\t\t{car.reg_number:<5}\t|\t\t {car.max_speed:<5}\t|\t\t{car.current_speed:<10}\t|\t\t {car.travelled_distance:<10}\t|\t")
        print("----------------------------------------------------------------------------")

