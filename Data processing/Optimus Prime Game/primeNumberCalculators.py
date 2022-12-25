class PrimeCalculators:
    def __init__(self,number=0):
        self.__number = number
        
    # setter method
    def set_num(self, x):
        self.__number = x

    # getter method
    def get_num(self):
        return self.__number
    
    def isPrimeOrNot(self):
        n = self.__number
        print("Your number chose was: " +str(n))
        primtNumber = True   
        for i in range(2, n):
            if (n % i == 0):
                print (str(n)+" % "+ str(i)+" = 0")
                print(str(n)+ " is not a prime number")
                primtNumber = False
                break
        if primtNumber:
            for i in range(2, n+1):
                if (n % i != 0):
                    print (str(n)+" % "+ str(i)+" = 1")
                    print(str(n)+ " is a prime number ")
                    primtNumber = False
                    break