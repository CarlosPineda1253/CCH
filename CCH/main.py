import sys
import threading
import time
from PyQt5 import QtCore, QtWidgets
import GetPhotos
import window_photos
import router
import window_main
import window_mainloft


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = window_main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    #MainWindow.showFullScreen()
    MainWindow.showNormal()
    main_widget = QtWidgets.QWidget(MainWindow)
    main_window_local = window_mainloft.Ui_MainLoft()
    main_window_local.setupUi(main_widget)
    MainWindow.setCentralWidget(main_widget)
    sys.exit(app.exec_())


def app_inactive():
    pass


def photo_main():
    app_photos = GetPhotos.FacePhotosVideos()
    photo_thread = threading.Thread(target=photo_loop, args=(app_photos,))
    photo_thread.start()


def photo_loop(photos_obj):
    time.sleep(900)
    photos_obj.update_photos()


def router_main():
    app_router = RouterLoft()


if __name__ == '__main__':
    main()
