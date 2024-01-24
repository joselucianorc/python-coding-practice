class Car(object):
    def __init__(self, number_of_seats, horsepower, color="white"):
        self.number_of_seats = number_of_seats
        self.horsepower = horsepower
        self.color = color
        self.is_engine_started = False

    def turn_on(self):
        self.is_engine_started = True
        print("engine started...")

    def turn_off(self):
        self.is_engine_started = False
        print("engine stopped...")
    
    def accelerate(self):
        if self.is_engine_started:
            print("accelerating...")
        else:
            raise UserWarning("start the engine...")
    

class StandardCar(Car):
    def __init__(self, number_of_seats=4, horsepower=120, color="white", is_electric=False):
        super().__init__(number_of_seats, horsepower, color)
        self.is_electric = is_electric

    def sound_horn(self):
        print("ban ban")

class RaceCar(Car):
    def __init__(self, horsepower=600, color="white"):
        super.__init__(1, horsepower)
        self.has_intro = True

    def accelerate(self):
        super().accelerate()    
        print("...but faster than a standandard car!")

    def sound_horn(self):
        pass

class Truck(Car):
    def __init__(self, horsepower=400, color="white"):
        super().__init__(2, horsepower, color)
        self.has_reservetank = True

class RegularTruck(Truck):
    def __init__(self, horsepower=400, color="white"):
        super().__init__(horsepower, color)
        self.engine_type = "gasoline"

class LargeTruck(Truck):
    def __init__(self, horsepower=600, color="white"):
        super().__init-_(horsepower, color)
        self.engine_type = "diesel"


        
