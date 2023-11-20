import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("my_qt08.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.com = int(random()*99+1)
        
        self.pb.clicked.connect(self.myclick)

   
    def myclick(self):
        num = int(self.le.text())
        
        str_old = self.te.toPlainText()
        str_new = self.le.text()
        if self.com > num :
            self.te.setText(str_old + str_new + " UP\n")
        elif self.com < num:
            self.te.setText(str_old + str_new+ " DOWN\n")
        else:
            self.te.setText(str_old + str_new+ " OK\n")
        self.le.setText("")
        
              
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    
    
