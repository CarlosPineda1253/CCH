# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'photos.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from qlabelclickable import QLabelClickable
from PyQt5.QtGui import QPixmap
import window_mainloft
import secrets
import os.path


class Ui_Photos(object):
    def setupUi(self, Photos):
        Photos.setObjectName("Photos")
        Photos.resize(800, 400)
        self.photos = QLabelClickable(Photos)
        self.photos.setGeometry(QtCore.QRect(0, 0, 800, 400))
        self.photos.setText("")
        self.photos.setPixmap(QtGui.QPixmap("face1.png"))
        self.photos.setScaledContents(True)
        self.photos.setObjectName("photos")

        self.retranslateUi(Photos)
        QtCore.QMetaObject.connectSlotsByName(Photos)

        self.timer = QtCore.QTimer()
        self.list_photos = os.listdir('photos/')
        self.photos.clicked.connect(lambda local_widget=Photos: self.on_click_tv_window(local_widget))
        self.timer.timeout.connect(self.loop_pictures)
        self.timer.start(30)

    def retranslateUi(self, Photos):
        _translate = QtCore.QCoreApplication.translate
        Photos.setWindowTitle(_translate("Photos", "Form"))

    def loop_pictures(self):
        self.photos.clear()
        local_photo_pix = QPixmap('photos/' + secrets.choice(self.list_photos))
        resized_photo_pix = local_photo_pix.scaled(800, 400, QtCore.Qt.IgnoreAspectRatio)
        self.photos.setPixmap(resized_photo_pix)
        self.timer.start(5*1000)

    def on_click_tv_window(self, Photos):
        mainwindow = Photos.parent()
        self.timer.stop()
        self.timer.deleteLater()
        Photos.destroy()
        local_widget = QtWidgets.QWidget(mainwindow)
        tv_window_local = window_mainloft.Ui_MainLoft()
        tv_window_local.setupUi(local_widget)
        mainwindow.setCentralWidget(local_widget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Photos = QtWidgets.QWidget()
    ui = Ui_Photos()
    ui.setupUi(Photos)
    Photos.show()
    sys.exit(app.exec_())
