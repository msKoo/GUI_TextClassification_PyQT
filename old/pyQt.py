import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initFrame()
        # self.initUI()

    def initFrame(self):
        main_layout = QVBoxLayout()

        frame_basic = QFrame()
        frame_basic.setFrameShape(QFrame.Panel | QFrame.Sunken)
        frame_type = QFrame()
        frame_type.setFrameShape(QFrame.Panel | QFrame.Sunken)
        frame_param = QFrame()
        frame_param.setFrameShape(QFrame.Panel | QFrame.Sunken)
        frame_log = QFrame()
        frame_log.setFrameShape(QFrame.Panel | QFrame.Sunken)
        frame_data = QFrame()
        frame_data.setFrameShape(QFrame.Panel | QFrame.Sunken)
        frame_visual = QFrame()
        frame_visual.setFrameShape(QFrame.Panel | QFrame.Sunken)

        layout_basic = QVBoxLayout()
        layout_basic_top = QHBoxLayout()
        layout_basic_bot = QHBoxLayout()

        layout_basic_top.addWidget(QLabel('기본 모델:'))
        layout_basic_bot.addWidget(QLabel('학습 모델:'))
        layout_basic_top.addWidget(QLineEdit())
        layout_basic_bot.addWidget(QLineEdit())

        button_1 = QPushButton("신규")
        button_2 = QPushButton("리네임")

        layout_basic.addLayout(layout_basic_top)
        layout_basic.addLayout(layout_basic_bot)

        layout_basic_top.addWidget(button_1)
        layout_basic_bot.addWidget(button_2)

        frame_basic.setLayout(layout_basic)
        # frame_type.setLayout(layout_2)

        spliter_left = QSplitter(Qt.Vertical)
        spliter_left.addWidget(frame_basic)
        spliter_left.addWidget(frame_type)
        spliter_left.addWidget(frame_param)
        spliter_left.addWidget(frame_log)

        spliter_right = QSplitter(Qt.Vertical)
        spliter_right.addWidget(frame_data)
        spliter_right.addWidget(frame_visual)

        # spliter_left.setSizes([1, 1])
        spliter_right.setSizes([1, 2])

        spliter_main = QSplitter(Qt.Horizontal)
        spliter_main.addWidget(spliter_left)
        spliter_main.addWidget(spliter_right)

        main_layout.addWidget(spliter_main)

        self.setLayout(main_layout)
        self.resize(1000, 600)
        self.show()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        frame_1 = QFrame()
        frame_1.setFrameShape(QFrame.Panel | QFrame.Sunken)
        frame_2 = QFrame()
        frame_2.setFrameShape(QFrame.Panel | QFrame.Sunken)

        btn1 = QPushButton(self)
        btn1.setText('신규')

        btn2 = QPushButton(self)
        btn2.setText('리네임')

        cb_tag = QCheckBox('html 태그 제거', self)
        cb_tag.stateChanged.connect(self.boxChecked)

        cb_reg = QCheckBox('특수 문자 제거', self)
        cb_reg.stateChanged.connect(self.boxChecked)

        cb_morph = QCheckBox('단어 분리', self)
        cb_morph.stateChanged.connect(self.boxChecked)

        cb_stop = QCheckBox('불용어 제거', self)
        cb_stop.stateChanged.connect(self.boxChecked)

        cb_stem = QCheckBox('어간 추출', self)
        cb_stem.stateChanged.connect(self.boxChecked)

        btn_fine = QPushButton(self)
        btn_fine.setText('Fine Tuning')

        btn_class = QPushButton(self)
        btn_class.setText('Class Matching')


        grid.addWidget(QLabel('기본 모델:'), 0, 0)
        grid.addWidget(QLabel('학습 모델:'), 1, 0)
        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(btn1, 0, 2)
        grid.addWidget(btn2, 1, 2)
        grid.addWidget(QTextEdit(), 0, 3, 2, 1)
        grid.addWidget(cb_tag, 2, 0)
        grid.addWidget(cb_reg, 2, 1)
        grid.addWidget(cb_morph, 2, 2)
        grid.addWidget(cb_stop, 3, 0)
        grid.addWidget(cb_stem, 3, 1)
        grid.addWidget(btn_fine, 2, 3)
        grid.addWidget(btn_class, 3, 3)


        grid.setColumnStretch(3, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def boxChecked(self):
        print('checked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())