# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tv.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from qlabelclickable import QLabelClickable
import tvremote
import window_mainloft
import window_inactive


class Ui_TV_widget(object):
    def setupUi(self, TV_widget):
        TV_widget.setObjectName("TV_widget")
        TV_widget.resize(800, 480)
        self.background = QtWidgets.QLabel(TV_widget)
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
        self.power = QLabelClickable(TV_widget)
        self.power.setGeometry(QtCore.QRect(380, 40, 40, 40))
        self.power.setText("")
        self.power.setPixmap(QtGui.QPixmap("icons/baseline_power_settings_new_black_18dp.png"))
        self.power.setScaledContents(True)
        self.power.setObjectName("power")
        self.up_tv = QLabelClickable(TV_widget)
        self.up_tv.setGeometry(QtCore.QRect(380, 110, 40, 40))
        self.up_tv.setText("")
        self.up_tv.setPixmap(QtGui.QPixmap("icons/baseline_keyboard_arrow_up_black_18dp.png"))
        self.up_tv.setScaledContents(True)
        self.up_tv.setObjectName("up_tv")
        self.ok_tv = QLabelClickable(TV_widget)
        self.ok_tv.setGeometry(QtCore.QRect(380, 160, 40, 40))
        self.ok_tv.setText("")
        self.ok_tv.setPixmap(QtGui.QPixmap("icons/baseline_done_black_18dp.png"))
        self.ok_tv.setScaledContents(True)
        self.ok_tv.setObjectName("ok_tv")
        self.left_tv = QLabelClickable(TV_widget)
        self.left_tv.setGeometry(QtCore.QRect(320, 160, 40, 40))
        self.left_tv.setText("")
        self.left_tv.setPixmap(QtGui.QPixmap("icons/baseline_keyboard_arrow_left_black_18dp.png"))
        self.left_tv.setScaledContents(True)
        self.left_tv.setObjectName("left_tv")
        self.down_tv = QLabelClickable(TV_widget)
        self.down_tv.setGeometry(QtCore.QRect(380, 210, 40, 40))
        self.down_tv.setText("")
        self.down_tv.setPixmap(QtGui.QPixmap("icons/baseline_keyboard_arrow_down_black_18dp.png"))
        self.down_tv.setScaledContents(True)
        self.down_tv.setObjectName("down_tv")
        self.right_tv = QLabelClickable(TV_widget)
        self.right_tv.setGeometry(QtCore.QRect(440, 160, 40, 40))
        self.right_tv.setText("")
        self.right_tv.setPixmap(QtGui.QPixmap("icons/baseline_keyboard_arrow_right_black_18dp.png"))
        self.right_tv.setScaledContents(True)
        self.right_tv.setObjectName("right_tv")
        self.home_tv = QLabelClickable(TV_widget)
        self.home_tv.setGeometry(QtCore.QRect(380, 290, 40, 40))
        self.home_tv.setText("")
        self.home_tv.setPixmap(QtGui.QPixmap("icons/baseline_home_black_18dp.png"))
        self.home_tv.setScaledContents(True)
        self.home_tv.setObjectName("home_tv")
        self.return_tv = QLabelClickable(TV_widget)
        self.return_tv.setGeometry(QtCore.QRect(290, 260, 40, 40))
        self.return_tv.setText("")
        self.return_tv.setPixmap(QtGui.QPixmap("icons/baseline_keyboard_backspace_black_18dp.png"))
        self.return_tv.setScaledContents(True)
        self.return_tv.setObjectName("return_tv")
        self.play_tv = QLabelClickable(TV_widget)
        self.play_tv.setGeometry(QtCore.QRect(470, 260, 40, 40))
        self.play_tv.setText("")
        self.play_tv.setPixmap(QtGui.QPixmap("icons/baseline_play_arrow_black_18dp.png"))
        self.play_tv.setScaledContents(True)
        self.play_tv.setObjectName("play_tv")
        self.volumen_down_tv = QLabelClickable(TV_widget)
        self.volumen_down_tv.setGeometry(QtCore.QRect(450, 400, 40, 40))
        self.volumen_down_tv.setText("")
        self.volumen_down_tv.setPixmap(QtGui.QPixmap("icons/baseline_volume_down_black_18dp.png"))
        self.volumen_down_tv.setScaledContents(True)
        self.volumen_down_tv.setObjectName("volumen_down_tv")
        self.volumen_up_tv = QLabelClickable(TV_widget)
        self.volumen_up_tv.setGeometry(QtCore.QRect(310, 400, 40, 40))
        self.volumen_up_tv.setText("")
        self.volumen_up_tv.setPixmap(QtGui.QPixmap("icons/baseline_volume_up_black_18dp.png"))
        self.volumen_up_tv.setScaledContents(True)
        self.volumen_up_tv.setObjectName("volumen_up_tv")
        self.return_home = QLabelClickable(TV_widget)
        self.return_home.setGeometry(QtCore.QRect(20, 430, 40, 40))
        self.return_home.setText("")
        self.return_home.setPixmap(QtGui.QPixmap("icons/baseline_keyboard_return_black_18dp.png"))
        self.return_home.setScaledContents(True)
        self.return_home.setObjectName("return_home")

        self.retranslateUi(TV_widget)
        QtCore.QMetaObject.connectSlotsByName(TV_widget)

        self.timer = window_inactive.WindowTimer(TV_widget)
        self.tv = tvremote.TVRemote()
        for i in TV_widget.children():
            if isinstance(i, QLabelClickable) and i.objectName() != 'return_home':
                i.clicked.connect(lambda name=i.objectName(): self.on_click_buttons(name))
        self.return_home.clicked.connect(lambda local_widget=TV_widget: self.on_click_return_home(local_widget))

    def retranslateUi(self, TV_widget):
        _translate = QtCore.QCoreApplication.translate
        TV_widget.setWindowTitle(_translate("TV_widget", "Form"))

    def on_click_return_home(self, TV_widget):
        mainwindow = TV_widget.parent()
        self.timer.stop()
        self.timer.destroy()
        TV_widget.destroy()
        local_widget = QtWidgets.QWidget(mainwindow)
        tv_window_local = window_mainloft.Ui_MainLoft()
        tv_window_local.setupUi(local_widget)
        mainwindow.setCentralWidget(local_widget)

    def on_click_buttons(self, name):
        self.timer.stop()
        self.timer.setInterval(window_inactive.WindowTimer.TIMEOUT_WINDOW)
        self.timer.start()
        getattr(tvremote.TVRemote, name)(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TV_widget = QtWidgets.QWidget()
    ui = Ui_TV_widget()
    ui.setupUi(TV_widget)
    TV_widget.show()
    sys.exit(app.exec_())
