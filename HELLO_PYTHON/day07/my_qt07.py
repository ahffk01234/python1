import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("my_qt07.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.number)
        self.pb2.clicked.connect(self.number)
        self.pb3.clicked.connect(self.number)
        self.pb4.clicked.connect(self.number)
        self.pb5.clicked.connect(self.number)
        self.pb6.clicked.connect(self.number)
        self.pb7.clicked.connect(self.number)
        self.pb8.clicked.connect(self.number)
        self.pb9.clicked.connect(self.number)
        self.pb0.clicked.connect(self.number)
        
        self.pbCall.clicked.connect(self.calling)

    def calling(self):
        num = self.le.text()
        QMessageBox.information(self, "calling", num+"으로 전화거는 중...")
        
    def number(self):
        num = self.sender().text()
        self.le.setText(self.le.text() + num)
    
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    
    
