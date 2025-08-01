
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "Petrol or diesel" 
    def full_name(self):
        return f"{self.model} , {self.__brand}"
    
    @staticmethod
    def general_description():
        return "this is car object"
        
my_car = Car("Toyota", "Corolla")

print(my_car.get_brand())
print(my_car.model)

second_car = Car("suzuki","alto 800")

print(second_car.get_brand())
print(second_car.model)

print(my_car.full_name())

print(second_car.fuel_type())

class ElectriCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"

electric_car = ElectriCar("TATA",'Tiago',"5 Battery")

print(electric_car.get_brand())
print(electric_car.model)
print(electric_car.battery_size)


print(electric_car.full_name())

print(electric_car.fuel_type())

print(my_car.general_description())