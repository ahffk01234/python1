import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("my_qt09.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.com = self.ranC()
        
        self.pb.clicked.connect(self.myclick)

    def ranC(self):
        list = ["0","1","2","3","4","5","6","7","8","9"]
        for i in range(0,1000) :
            
            rnd = int(random()*9)+1
            
            temp = list[0]
            list[0] = list[rnd]
            list[rnd] = temp
        
        self.com = list[0]+list[1]+list[2]
        print(self.com)
        return self.com
        
        
    def getB(self,num,com):
        ret = 0;
        m1 = num[0:1]
        m2 = num[1:2]
        m3 = num[2:3]
        
        c1 = self.com[0:1]
        c2 = self.com[1:2]
        c3 = self.com[2:3]
        
        if m1 == c2 or m1 == c3 :ret+=1
        if m2 == c1 or m2 == c3 :ret+=1
        if m3 == c1 or m3 == c2 :ret+=1
        

        return ret
        
    def getS(self,num,com):
        ret = 0;
        m1 = num[0:1]
        m2 = num[1:2]
        m3 = num[2:3]
        
        c1 = self.com[0:1]
        c2 = self.com[1:2]
        c3 = self.com[2:3]
        
        if m1 == c1 : ret+=1
        if m2 == c2 : ret+=1
        if m3 == c3 : ret+=1
        
        
        return ret
        
    def myclick(self):
     
        num = self.le.text()
        s = self.getS(num,self.com)
        b = self.getB(num,self.com)
        
        str_old = self.te.toPlainText()
        str_new = num + "----" +str(s)+"S"+ str(b)+"B\n"
       
        self.te.setText(str_old + str_new)
        
        if s == 3:
            QMessageBox.information(self,"축하합니다", num)
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    
    
