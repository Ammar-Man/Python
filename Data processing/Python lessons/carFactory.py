class Car:
    def __init__(self,make,color):
        self.__make = make
        self.__color = color
    
    def toString(self):
        print("Car is a", self.__color,self.__make)
        # return("Bilen är en", self.__color,self.__make)

