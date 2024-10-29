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

class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_capacity):
        super().__init__(reg_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, volume):
        super().__init__(reg_number, max_speed)
        self.volume = volume

if __name__ == '__main__':
    e_car=ElectricCar(reg_number="ABC-15", max_speed=180, battery_capacity=52.5)
    e_car.accelerate(50)
    e_car.drive(3)
    g_car= GasolineCar(reg_number="ACD-123", max_speed=165, volume=32.3)
    g_car.accelerate(60)
    g_car.drive(3)
    print(f"Electric car: {e_car.reg_number} travelled {e_car.travelled_distance} km in 3 hours.")
    print(f"Gasoline Car: {g_car.reg_number} travelled {g_car.travelled_distance} km in 3 hours.")