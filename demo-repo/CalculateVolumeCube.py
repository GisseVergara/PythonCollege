class Cube:
    def __init__(self, wide, high, long):
        self.wide=wide
        self.high=high
        self.long=long
    
    def calculate_volume(self):
        return (self.wide*self.high*self.long)
    
wide=int(input("Provide the width: "))
high=int(input("Provide the height: "))
long=int(input("Provide the lenght: "))

cube1=Cube(wide,high,long)
print("The cube's volume is: ", cube1.calculate_volume())