import random
import sys
import time
import datetime
import numpy as np

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyqtgraph as pq

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import numpy

import pandas as pd

from Visualizing import displayWordCloud, dataGraph
from preprocessing import pre_html, pre_reg, pre_stem, pre_stop

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("test_misong_2.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('DrSong Text Classification Tool')
        self.sb = self.statusBar()
        self.setStatusBar(self.sb)
        self.sb.showMessage('준비중')

        self.result_Label.clear()
        self.train_data.clicked.connect(self.create_data_Function)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.movie = QMovie("./src/myGifSpin.gif")
        # self.loading_label.setMovie(self.movie)

        self.graphWidget.hide()
        self.graphWidget_2.hide()

        self.comboBox.currentIndexChanged.connect(self.comboBoxFunction)
        self.fit_model = self.comboBox.currentText()

        self.groupBox_rad1.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad2.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad3.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad4.clicked.connect(self.groupboxRadFunction)

        self.prepro_applyButton.clicked.connect(self.prepro_apply)
        self.train_start_Button.clicked.connect(self.train_start)

    def comboBoxFunction(self):
        self.fit_model = self.comboBox.currentText()
        print(self.fit_model)

    def create_data_Function(self):
        print('clicked 2')
        # filePath 출력하는 부분 초기화
        self.train_data_lineEdit.clear()

        # # comboBox 출력하는 부분 초기화
        self.comboBox.clear()

        # 선택한 엑셀 파일 경로를 받아옴 : 튜플 타입으로 받아오며 0번재 요소가 주소값 string이다.
        path = QFileDialog.getOpenFileName(self, 'Open File', '', 'csv File(*.csv)')

        # filePath에 현재 읽어온 엑셀 파일 경로를 입력한다.(절대경로)
        self.train_data_lineEdit.setText(path[0])
        #
        self.df = pd.read_csv(path[0])
        self.setTableView(self.df)
        self.totalCount_Label.setText(str(len(self.df)*1.0))
        if len(self.df['label'].unique()) == 2:
            self.labelCount_Label.setText('binary (2)')
        else:
            self.labelCount_Label.setText('multiclass ('+len(self.df['label'].unique())+')')
        self.trainSet_Label.setText(str(len(self.df)*0.8))
        self.validSet_Label.setText(str(len(self.df)*0.2))
        # print('여기',self.fit_model)
        # self.model_Label.setText(str(self.fit_model))

    def setTableView(self, df):
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(df.shape[1])

        test = [self.tableWidget.horizontalHeaderItem(x).text() for x in range(self.tableWidget.columnCount())]

        for index, row in df.iterrows():
            for j, item in enumerate(test):
                self.tableWidget.setItem(index, j, QTableWidgetItem(str(row[item])))
            if index == 10:
                break

        header = self.tableWidget.horizontalHeader()
        twidth = header.width()
        width = [60, 600, 100]

        wfactor = twidth / sum(width)
        for column in range(header.count()):
            header.setSectionResizeMode(column, QHeaderView.Interactive)
            header.resizeSection(column, width[column] * wfactor)

        self.tableWidget.repaint()

    def groupboxRadFunction(self):
        self.prepro = {'html': False, 'stop': False, 'regular': False, 'stemming': False}
        self.default_stopwords = ['이', '있', '하', '것', '들', '그', '되', '수', '이', '보', '않', '없', '나', '사람', '주', '아니', '등', '같', '우리', '때', '년', '가', '한', '지', '대하', '오', '말', '일', '그렇', '위하']


        if self.groupBox_rad1.isChecked():
            self.prepro['html'] = True
        if self.groupBox_rad2.isChecked():
            self.prepro['stop'] = True
            self.stopword_plainTextEdit.setDisabled(False)
            self.stopword_plainTextEdit.setPlainText(str(self.default_stopwords))
        else:
            self.prepro['stop'] = False
            self.stopword_plainTextEdit.setDisabled(True)
        if self.groupBox_rad3.isChecked():
            self.prepro['regular'] = True
        if self.groupBox_rad4.isChecked():
            self.prepro['stemming'] = True

    def prepro_apply(self):
        self.log_textEdit.setText('전처리 시작')

        self.movie.start()
        self.sb.showMessage('전처리 진행 중')
        time.sleep(2)

        self.df = self.df.dropna(axis=0)
        raw_contents = self.df['sentence'].values.tolist()

        if self.prepro['html']:
            # self.sb.repaint()
            # self.sb.showMessage('html 제거 중')
            raw_contents = list(map(lambda x:pre_html(x), raw_contents))
        if self.prepro['stop']:
            # self.sb.repaint()
            # self.sb.showMessage('불용어 제거 중')
            stopwords = self.stopword_plainTextEdit.toPlainText()
            # self.log_textEdit.setText(stopwords)
            raw_contents = list(map(lambda x:pre_stop(x, stopwords), raw_contents))
        if self.prepro['regular']:
            # self.sb.repaint()
            # self.sb.showMessage('특수문자 제거 중')
            raw_contents = list(map(lambda x:pre_reg(x), raw_contents))
        if self.prepro['stemming']:
            # self.sb.repaint()
            # self.sb.showMessage('어간 추출 중')
            raw_contents = list(map(lambda x:pre_stem(x), raw_contents))

        self.df['sentence'] = raw_contents

        self.setTableView(self.df)
        self.sb.showMessage('전처리 완료')

        self.displayWordCloud(raw_contents)
        # self.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], list(map(lambda x:random.randrange(1,20), range(0, 9))))
        self.draw_graph(raw_contents)

        # self.movie.stop()

    def draw_graph(self, reviews):
        dataGraph(reviews)
        pixmap = QPixmap('./src/result/seaborn/seaborn_numword.png')
        self.wordCloud_label_2.setPixmap(pixmap)

    def progressBarTimer(self):
        self.time = self.progressBar.value()
        self.time += 1
        self.progressBar.setValue(self.time)

        # ProgressBar의 값이 최댓값 이상이 되면 Timer를 중단시켜 ProgressBar의 값이 더이상 증가하지 않게 합니다.
        if self.time >= self.progressBar.maximum():
            self.timerVar.stop()

    def printValue(self):
        print(self.progressBar.value(), end=' ')

    def update_label(self):
        cur_time = datetime.strftime(datetime.now(), "%d.%m %H:%M:%S")
        print(cur_time)
        self.log_textEdit.setText(cur_time)

    def train_start(self):
        # ProgressBar의 시그널
        # self.progressBar.valueChanged.connect(self.printValue)

        # QTimer를 이용하여 매초마다 ProgressBar의 값이 1씩 늘어나게 설정합니다.
        # QTimer의Interval을 1000으로 설정한 후, ProgrssBar의 값이 늘어나게 하는 함수를 연결하고 QTimer를 시작합니다.
        # QTimer에 대한 설명은 02.17.01 QTimer에서 보실 수 있습니다.
        self.timerVar = QTimer()
        self.timerVar.setInterval(1)
        self.timerVar.timeout.connect(self.progressBarTimer)
        self.timerVar.start()


        f = open('./src/train_log.txt', 'r')
        line_num = 1
        line = f.readline()
        while line:
            # print('%s' % (line), end='')
            line = f.readline()
            self.log_textEdit.append(line)
            self.log_textEdit.repaint()
            # line_num += 1
            # time.sleep(0.5)
        f.close()

        # timer = QTimer()
        # timer.timeout.connect(self.update_label)
        # timer.start(1)

        y_vloss = [0.13596169148484866, 0.10232374267478785, 0.09159363598103325, 0.08637172984133164,
                   0.09674505230680419, 0.09105636464593311, 0.09010037897935448, 0.09504081677481688,
                   0.09993200332935667, 0.10999317096428277]
        y_loss = [0.2266461635907491, 0.09062119808826181, 0.0589320162879924, 0.04020388817155165,
                  0.027329568712951408,
                  0.02126024063843199, 0.017342214744481155, 0.013346235364758307, 0.012164281833562482,
                  0.009792077704742164]

        self.plot_loss(y_vloss, y_loss)

        accuracy= [0.9335778, 0.9725556, 0.9815556, 0.9874222, 0.9913778, 0.99322224, 0.9945111, 0.99597776,
                      0.99635553, 0.99664444]
        val_accuracy =  [0.95993334, 0.9709333, 0.9734667, 0.976, 0.9734, 0.9754, 0.9766, 0.9781333, 0.9758667, 0.9764]

        self.plot_accurracy(accuracy, val_accuracy)


        self.result_Label.setText('total 40, wrong 23 [57.5%]')


    def plot_loss(self, y_vloss, y_loss):
        self.pen_b = pq.mkPen('b', width = 3)
        self.pen_r = pq.mkPen('r', width = 3)
        # self.graphWidget.plot.rc('font', size=SMALL_SIZE)
        self.graphWidget.setLabel('left', 'loss', fontsize=1)
        self.graphWidget.setLabel('bottom', 'epoch', fontsize=1)
        self.graphWidget.setBackground('N')
        # self.graphWidget.plot(x, y, pen=self.pen)

        x_len = numpy.arange(len(y_loss))
        self.graphWidget.plot(x_len, y_vloss, marker='.',label="Validation-set Loss", pen = self.pen_r)
        self.graphWidget.plot(x_len, y_loss, marker='.',label="Train-set Loss",  pen = self.pen_b)

        # self.graphWidget.legend(loc='upper right')
        plt.show()

        self.graphWidget.show()

    def plot_accurracy(self, y_vloss, y_loss):
        self.pen_b = pq.mkPen('b', width = 3)
        self.pen_r = pq.mkPen('r', width = 3)
        # self.graphWidget.plot.rc('font', size=SMALL_SIZE)
        self.graphWidget_2.setLabel('left', 'accuracy', fontsize=1)
        self.graphWidget_2.setLabel('bottom', 'epoch', fontsize=1)
        self.graphWidget_2.setBackground('N')
        # self.graphWidget.plot(x, y, pen=self.pen)

        x_len = numpy.arange(len(y_loss))
        self.graphWidget_2.plot(x_len, y_vloss, marker='.',label="Validation-set Accu", pen = self.pen_r)
        self.graphWidget_2.plot(x_len, y_loss, marker='.',label="Train-set Accu",  pen = self.pen_b)

        # self.graphWidget.legend(loc='upper right')
        plt.show()

        self.graphWidget_2.show()

    def displayWordCloud(self, data):
        width = 430
        height = 250
        displayWordCloud(' /'.join(data), width, height)
        pixmap = QPixmap('./src/result/wordCloud/wordcloud_w'+str(width)+'.png')
        # pixmap = pixmap.scaled(int(pixmap.width() / 3), int(pixmap.height() / 3))
        # 이미지 관련 클래스와 라벨 연결
        self.wordCloud_label.setPixmap(pixmap)

    # def changeTextFunction(self):
    #     # self.Textbrowser이름.setPlainText()
    #     # Textbrowser에 있는 글자를 가져오는 메서드
    #     self.textBrowser.setPlainText("This is Textbrowser - Change Text")




if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
