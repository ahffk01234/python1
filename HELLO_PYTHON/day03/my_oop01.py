
class Animal:
    def __init__(self):
        self.cnt_hair = 1000
        
    def tsshampoo(self):
        self.cnt_hair += 100

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.flag_dev = False
        
    def principle_voice(self):
        self.flag_dev = True
    
    def human_hair(self):
        print(self.cnt_hair)
            
if __name__ == '__main__':
    hum = Human()
    print(hum.flag_dev)
    print(hum.cnt_hair)
    
    hum.principle_voice()
    hum.tsshampoo()
    print(hum.flag_dev)
    print(hum.cnt_hair)
    