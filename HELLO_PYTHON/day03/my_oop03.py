class Vehicle:
    def __init__(self):
        self.cnt_wheel = 4
        
    def funk(self,cnt):
        self.cnt_wheel -= cnt
        
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.volume_speaker = 20
        
    def turnRight(self,cnt):
        self.volume_speaker += cnt
    def turnLeft(self,cnt):
        self.volume_speaker -= cnt
        
    
car = Car()
print(car.cnt_wheel)
print(car.volume_speaker)

car.funk(2)
car.turnLeft(10)
print(car.volume_speaker)
car.turnRight(5)

print("------------------")
print(car.cnt_wheel)
print(car.volume_speaker)
