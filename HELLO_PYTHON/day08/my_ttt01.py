import sys
from PyQt5.QtWidgets import QPushButton, QMainWindow,QApplication
from PyQt5 import uic
from random import random
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.Qt import QSize

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("my_ttt01.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.flag_xo = True
        self.setupUi(self)
        for i in range(3):
            for j in range(3):
                btn = QPushButton(self)
                btn.setIcon(QIcon('0.png'))
                btn.setIconSize(QSize(40,40))
                btn.setGeometry(i*41,j*41,40,40)
                btn.clicked.connect(self.myclick)
            
        
        self.pb.clicked.connect(self.myreset)
        
    def myreset(self):
        print("myreset")
        
        
    def myclick(self):
        if self.flag_xo :
            self.sender().setIcon(QIcon('1.png'))
            self.flag_xo = False
        else :
            self.sender().setIcon(QIcon('2.png'))
            self.flag_xo = True
    
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    
    
