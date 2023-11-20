class drone:
    def __init__(self): # 생성자
        self.height = 0
        print("constructor")
    
    def fly(self):
        self.height += 1
        print("fly")
    
    def __del__(self): # 소멸자
        print("destroyer")
    
    def __str__(self): # toString()
        return str(self.height)

if __name__ == '__main__':
    d = drone()
    print(d.height)
    d.fly()
    print(d)
