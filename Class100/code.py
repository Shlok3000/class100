#def areaOfSquare(a):
    #return a*a
#print(areaOfSquare(25))
class Car(object):
    def __init__(self, speed, steering, model, color, company, gas, wheelType):
        self.speed = speed
        self.steering = steering
        self.model = model
        self.color = color
        self.company = company
        self.gas = gas
        self.wheelType = wheelType

    def start(self):
        print("started")
    
    def stop(self):
        print("Car Stop!")

    def accelerate(self):
        print("Car, go faster")

Tesla = Car("60", "3", "Model X", "blue", "Tesla", "Electricity", "Michilen")
print(Tesla.gas)
Tesla.start()
Tesla.accelerate()
Tesla.stop()