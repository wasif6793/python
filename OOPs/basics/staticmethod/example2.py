class TempConv:
    @staticmethod

    def cels_to_fahr(celsius):
        return (celsius * 9/5) + 32

temp_fahr = TempConv.cels_to_fahr(25)
print(temp_fahr)