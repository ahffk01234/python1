import sys
from PyQt5.QtWidgets import QPushButton, QMainWindow,QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.Qt import QSize, QMessageBox

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("my_ttt02.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.flag_over = False
        self.flag_ox = True
        self.arr2d = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        
        self.pb2d = []
        
        self.setupUi(self)
        
        for i in range(3):
            line = []
            for j in range(3):
                btn = QPushButton(self)
                btn.setIcon(QIcon('0.png'))
                btn.setIconSize(QSize(40,40))
                btn.setGeometry(j*41,i*41,40,40)
                btn.setToolTip(str(i)+','+str(j))
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2d.append(line)
        
        self.pb.clicked.connect(self.myreset)
        
        self.myrender()
        
    def myreset(self):
        for i in range(3):
            for j in range(3):
                self.arr2d[i][j] = 0
        self.flag_ox = True
        self.flag_over = False
        self.myrender()
    
    def myrender(self):
        for i in range(3):
            for j in range(3):
                if self.arr2d[i][j] == 0:
                    
                    self.pb2d[i][j].setIcon(QIcon('0.png'))
                    
                elif self.arr2d[i][j] == 1:
                    
                    self.pb2d[i][j].setIcon(QIcon('1.png'))
                    
                else :
                    self.pb2d[i][j].setIcon(QIcon('2.png'))
        
    def myclick(self):
        
        if self.flag_over:
            return
        
        str = self.sender().toolTip().split(",")
        i = int(str[0])
        j = int(str[1])
        if self.arr2d[i][j] > 0:
            return
        else:
            if self.flag_ox :
                self.arr2d[i][j] = 1
            else:
                self.arr2d[i][j] = 2
        
        self.myrender()
        
        flag_over = self.isOver()
        
        if flag_over :
            if self.flag_ox:
                QMessageBox.about(self, "tiktaktoe","X 승리")
            else :
                QMessageBox.about(self, "tiktaktoe","O 승리")
            self.flag_over = True
            
        self.flag_ox = not self.flag_ox    
        
    def isOver(self):
        ox = 2
        if self.flag_ox:
            ox = 1
                
        a2 = self.arr2d
            
        if a2[0][0] == ox and a2[0][1] == ox and a2[0][2] == ox: return True
        if a2[1][0] == ox and a2[1][1] == ox and a2[1][2] == ox: return True
        if a2[2][0] == ox and a2[2][1] == ox and a2[2][2] == ox: return True
            
        if a2[0][0] == ox and a2[1][0] == ox and a2[2][0] == ox: return True
        if a2[0][1] == ox and a2[1][1] == ox and a2[2][1] == ox: return True
        if a2[0][2] == ox and a2[1][2] == ox and a2[2][2] == ox: return True

        if a2[0][0] == ox and a2[1][1] == ox and a2[2][2] == ox: return True
        if a2[0][2] == ox and a2[1][1] == ox and a2[2][0] == ox: return True
            
        return False
    
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    
    
