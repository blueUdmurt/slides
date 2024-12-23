class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0
    
    def describe_car(self):
        return f"{self.year}{self.make}{self.model}"
    
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it"
    
    def update_odometer(self, mileage):
        if mileage >=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("u can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles>0:
            self.odometer_reading +=miles
        else:
            print("u can't increment the odometer by a negative amount")

my_car=Car('Toyota','Corrola', 2020)
#my_car.describe_car()
print(my_car.describe_car())
my_car.update_odometer(1500)
print(my_car.read_odometer())
my_car.increment_odometer(200)
print(my_car.read_odometer())