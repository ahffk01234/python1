import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("my_qt05.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pb.clicked.connect(self.lotto)

    def lotto(self):
        lotto = []
        for i in range(0,5):
            num = int(random()*45)+1
            lotto.append(num)
            if i > 1 and i < 5:
                if lotto[i] == lotto[i-1]:
                    i -= 1
            print(num)
            
            
        self.le1.setText(str(lotto[0]))
        self.le2.setText(str(lotto[1]))
        self.le3.setText(str(lotto[2]))
        self.le4.setText(str(lotto[3]))
        self.le5.setText(str(lotto[4]))
        self.le6.setText(str(lotto[5]))
       
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    
    
