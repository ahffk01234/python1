class Xi:
    def __init__(self):
        self.money = 10000
        
    def bitcoin(self):
        self.money *= 2
        
    
class Musk:
    def __init__(self):
        self.companys = []
    
    def tell(self,c_name):
        self.companys.append(c_name)
        
    def show(self):
        for c in self.companys:
            print(c)

class LeeSS:
    def __init__(self):
        self.tuttle = 12
    
    def nadaeyong(self):
        self.tuttle += 1
        

class WooTaeWon(Xi,Musk,LeeSS):
    def __init__(self):
        Xi.__init__(self)
        Musk.__init__(self)
        LeeSS.__init__(self)
        

if __name__ == '__main__':
    wtw = WooTaeWon()
    print(wtw.money)
    print(wtw.tuttle)
    
    wtw.show()
    wtw.bitcoin()
    wtw.nadaeyong()
    wtw.tell("테슬라")
    wtw.tell("스페이스X")
    print(wtw.money)
    print(wtw.tuttle)
    wtw.show()
