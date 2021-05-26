# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainloft.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from qlabelclickable import QLabelClickable
import window_tv
import window_inactive
import lights


class Ui_MainLoft(object):
    def setupUi(self, MainLoft):
        MainLoft.setObjectName("MainLoft")
        MainLoft.resize(793, 466)
        self.frame = QtWidgets.QFrame(MainLoft)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.background = QtWidgets.QLabel(self.frame)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        self.background.setText("")
        self.background.setTextFormat(QtCore.Qt.RichText)
        self.background.setPixmap(QtGui.QPixmap("icons/wallpaper.jpg"))
        self.background.setScaledContents(True)
        self.background.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.background.setWordWrap(False)
        self.background.setObjectName("background")
        self.climate = QLabelClickable(self.frame)
        self.climate.setGeometry(QtCore.QRect(350, 160, 81, 71))
        self.climate.setText("")
        self.climate.setPixmap(QtGui.QPixmap("icons/ic_home_thermometer_outline_black_48dp.png"))
        self.climate.setScaledContents(True)
        self.climate.setObjectName("climate")
        self.tv = QLabelClickable(self.frame)
        self.tv.setGeometry(QtCore.QRect(600, 160, 81, 71))
        self.tv.setText("")
        self.tv.setPixmap(QtGui.QPixmap("icons/ic_television_black_48dp.png"))
        self.tv.setScaledContents(True)
        self.tv.setObjectName("tv")
        self.lights = QLabelClickable(self.frame)
        self.lights.setGeometry(QtCore.QRect(100, 160, 81, 71))
        self.lights.setText("")
        self.lights.setTextFormat(QtCore.Qt.AutoText)
        self.lights.setPixmap(QtGui.QPixmap("icons/ic_lightbulb_black_48dp.png"))
        self.lights.setScaledContents(True)
        self.lights.setObjectName("lights")
        self.settings = QLabelClickable(self.frame)
        self.settings.setGeometry(QtCore.QRect(740, 420, 51, 51))
        self.settings.setText("")
        self.settings.setPixmap(QtGui.QPixmap("icons/baseline_settings_black_18dp.png"))
        self.settings.setScaledContents(True)
        self.settings.setObjectName("settings")

        self.retranslateUi(MainLoft)
        QtCore.QMetaObject.connectSlotsByName(MainLoft)
        MainLoft.destroy()

        self.timer = window_inactive.WindowTimer(MainLoft)
        self.tv.clicked.connect(lambda local_widget=MainLoft: self.on_click_tv_window(local_widget))
        self.lights.clicked.connect(lambda local_widget=MainLoft: self.on_click_lights_window(local_widget))

    def retranslateUi(self, MainLoft):
        _translate = QtCore.QCoreApplication.translate
        MainLoft.setWindowTitle(_translate("MainLoft", "Form"))

    def on_click_tv_window(self, MainLoft):
        mainwindow = MainLoft.parent()
        self.timer.stop()
        self.timer.destroy()
        MainLoft.destroy()
        local_widget = QtWidgets.QWidget(mainwindow)
        tv_window_local = window_tv.Ui_TV_widget()
        tv_window_local.setupUi(local_widget)
        mainwindow.setCentralWidget(local_widget)

    def on_click_lights_window(self, MainLoft):
        mainwindow = MainLoft.parent()
        self.timer.stop()
        self.timer.destroy()
        MainLoft.destroy()
        local_widget = QtWidgets.QWidget(mainwindow)
        tv_window_lights = lights.Ui_Lights()
        tv_window_lights.setupUi(local_widget)
        mainwindow.setCentralWidget(local_widget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainLoft = QtWidgets.QWidget()
    ui = Ui_MainLoft()
    ui.setupUi(MainLoft)
    MainLoft.show()
    sys.exit(app.exec_())
