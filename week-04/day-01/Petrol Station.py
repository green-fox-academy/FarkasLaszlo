#Create Station and Car classes
#Station
#gas_amount
#refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
#Car
#gas_amount
#capacity
#create constructor for Car where:
#initialize gas_amount -> 0
#initialize capacity -> 100
class Station(object):

    def __init__(self, gas_amount):
        self.gas_amount = gas_amount

    def refill(self, car):
        if self.gas_amount >= car.capacity:
            self.gas_amount -= (car.capacity - car.gas_amount)
            car.gas_amount += (car.capacity - car.gas_amount)
            return car.gas_amount
        else:
            car.gas_amount = self.gas_amount
            self.gas_amount = 0
            return car.gas_amount


class Car(object):

    def __init__(self, gas_amount=0, capacity=100):
        self.gas_amount = gas_amount
        self.capacity = capacity


car1 = Car()
station1 = Station(150)

car1.gas_amount = station1.refill(car1)
print("The amount of gas the car has: "+str(car1.gas_amount)+"\n"+"The capacity of the car: "+str(car1.capacity)+"\n"+"The gas left on the station: "+str(station1.gas_amount))
