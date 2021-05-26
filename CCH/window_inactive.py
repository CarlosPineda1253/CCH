from PyQt5 import QtCore, QtWidgets
import window_photos


class WindowTimer:
    # TIMEOUT_WINDOW = (4*60)*1000
    TIMEOUT_WINDOW = 10*1000

    def __init__(self, CurrentWidget):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda cw=CurrentWidget: self.timeout_inactive(cw))
        self.timer.setSingleShot(True)
        self.timer.start(self.TIMEOUT_WINDOW)

    def timeout_inactive(self, CurrentWidget):
        mainwindow = CurrentWidget.parent()
        self.timer.deleteLater()
        CurrentWidget.destroy()
        local_widget = QtWidgets.QWidget(mainwindow)
        photos_window_local = window_photos.Ui_Photos()
        photos_window_local.setupUi(local_widget)
        mainwindow.setCentralWidget(local_widget)

    def stop(self):
        self.timer.stop()

    def destroy(self):
        self.timer.deleteLater()
