class Temp:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod

    def from_fahr(cls, fahr):
        celsius = (fahr - 32 ) * 5 / 9
        return cls(celsius)

temp = Temp.from_fahr(98.6)
print(temp.celsius)