class Car:
    def __init__(self,colour,company,speed):
        self.col = colour
        self.com = company
        self.speed = speed

    def start(self):
        print('started')

    def Getspeed(self,distance,time):
        print(distance/time)
        #return distance/time
print("start")

car1 = Car('red','abc',30)
print(car1.col)
car1.Getspeed(200,10)