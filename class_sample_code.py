class Vehicle:
   
    def __init__(self, body_type, fuel_type):
        self.body = body_type
        self.fuel = fuel_type

    def print_vehicle(self):
        print("Vehicle created")

class truck(Vehicle):
    
    def print_vehicle(self):  #Here we have overridden the method print_vechicle declared in the base class.
        print("Truck created")


class bus(Vehicle):
    
    def print_vehicle(self):  #Here we have overridden the method print_vechicle declared in the base class.
        print("Bus created")


vehicle1 = Vehicle('car', 'petrol')
truck1 = truck('benz', 'diesel')
bus1 = bus('volvo', 'gas')

for item in [vehicle1, truck1, bus1]:
    item.print_vehicle()







