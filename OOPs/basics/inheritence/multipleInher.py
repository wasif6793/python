class Engine:
    def engine(self):
        return "V8"

class Transmission:
    def transmission_type(self):
        return "Automatic"

class SportsCar(Engine,Transmission):
    def sportss(self):
        return True

myCar = SportsCar()
print(myCar.engine())
print(myCar.transmission_type())
print(myCar.sportss())