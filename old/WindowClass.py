import matplotlib.pyplot as plt
import openpyxl as op
from PyQt5.QtWidgets import *
import pandas as pd
from PyQt5 import uic

# form_class = uic.loadUiType("./test.ui")[0]

class WindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI Setup

        # fileSelect 버튼 클릭시 selectFunction 메서드 동작
        self.fileSelect.clicked.connect(self.selectFunction)

        # comboBox의 내용 변경시 printShtname 메서드 동작
        # self.comboBox.currentIndexChanged.connect(self.printShtname)

    # selectFunction 메서드 정의
    def selectFunction(self):
        # filePath 출력하는 부분 초기화
        self.filePath.clear()
        # comboBox 출력하는 부분 초기화
        self.comboBox.clear()
        # 선택한 엑셀 파일 경로를 받아옴 : 튜플 타입으로 받아오며 0번재 요소가 주소값 string이다.
        path = QFileDialog.getOpenFileName(self, 'Open File', '', 'All File(*);; xlsx File(*.xlsx)')
        # filePath에 현재 읽어온 엑셀 파일 경로를 입력한다.(절대경로)
        self.filePath.setText(path[0])

        self.df = pd.read_excel(path)
        self.dx = self.df[['x']]
        self.dy = self.df[['y']]

        # 위 절대 경로 활용해 openpyxl workbook 객체 생성
        # wb = op.load_workbook(path[0])
        # 설정한 workbook의 시트리스트를 읽어온다.
        # self.shtlist = wb.sheetnames
        # print(self.shtlist)
        #
        # # 시트리스트를 반복문으로 진행
        # for sht in self.shtlist:
        #     # 콤보박스의 addItem을 사용하여 항목 추가(addItem의 요소는 문자열 타입)
        #     self.comboBox.addItem(sht)

    def setFrame(self):
        lblName = QLabel("원하는 데이터를 선택하시오")
        btX = QPushButton('x axis')
        btY = QPushButton('y axis')
        btT = QPushButton('Total')

        btX.clicked.connect(self.btnXClicked)
        btY.clicked.connect(self.btnYClicked)
        btT.clicked.connect(self.btnTClicked)

        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(btX)
        layout.addWidget(btY)
        layout.addWidget(btT)
        self.setLayout(layout)

    # 콤보박스의 내용 변경시 터미널에 시트명 출력
    def printShtname(self):
        print(self.comboBox.currentText())

    def btnXClicked(self):
        plt.plot(self.dx)
        plt.show()

    def btnYClicked(self):
        plt.plot(self.dy)
        plt.show()

    def btnTClicked(self):
        plt.plot(self.df)
        plt.show()