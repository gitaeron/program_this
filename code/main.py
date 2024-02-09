# =========================================================== #
# 基础模块
import config as conf
import sys
import os

import pycallgraph2 as pycallgraph
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput

# yolov8
from ultralytics import YOLO
# =========================================================== #

# =========================================================== #
# 通过 cv2 读取 并 展示图片
import cv2
# =========================================================== #

# =========================================================== #
# 用户界面相关模块
# QT interface
from myui import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QMessageBox, QMainWindow, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

# QT sheetstyle
from qt_material import apply_stylesheet
# =========================================================== #


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # set up ui
        self.my_ui_init()

        # Load the model first to increase the running speed.
        self.model = YOLO(conf.BEST_MODEL_PATH, task='detect')

# [ WARN:2@27.604] global cap_msmf.cpp:1759 CvCapture_MSMF::grabFrame videoio(MSMF): can't grab frame. Error: -1072873821



        # signal & slot
        # switch page
        self.pushButton_6.clicked.connect(self.switch_to_home_page)
        self.pushButton_7.clicked.connect(self.switch_to_test_page)
        self.pushButton_8.clicked.connect(self.switch_to_predict_page)

        # in test page
        self.pushButton.clicked.connect(self.path_test)
        self.pushButton_2.clicked.connect(self.load_img_test)
        self.pushButton_3.clicked.connect(self.model_predict_test)

        # in predict page
        self.pushButton_4.clicked.connect(self.camera_snapshot_detect)
        self.pushButton_5.clicked.connect(self.camera_stream_detect)

    # End of init

    def switch_to_home_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_test_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_predict_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def path_test(self):
        tmp = [conf.PROJECT_PATH, conf.CODE_PATH, conf.DATASET_PATH, conf.MODEL_PATH]
        QMessageBox.information(
            self,
            "path_test",
            "{}".format(tmp)
        )

    def load_img_test(self):
        file_name = QFileDialog.getOpenFileName(self)
        # print(name)
        self.show_image_or_predict(file_name[0])

    def model_predict_test(self):
        file_name = QFileDialog.getOpenFileName(self)
        # print(file_name)
        self.show_image_or_predict(file_name[0], is_predict=True)

    def camera_snapshot_detect(self):
        # my_camera.release()
        my_camera = cv2.VideoCapture(0)
        is_video_opened = my_camera.isOpened()

        if is_video_opened:
            success, frame = my_camera.read()
            while success:
                success, frame = my_camera.read()
                cv2.imshow("Press 's' to Save, 'q' to quit", frame)
                keyword = cv2.waitKey(1)

                if keyword == ord('s') or keyword == ord('S'):
                    cv2.imwrite(conf.VIDEO_IMAGE_SAVE_PATH, frame)

                    # show the image that just take
                    # self.show_image_or_predict(conf.VIDEO_IMAGE_SAVE_PATH)

                    # Predict the image
                    self.show_image_or_predict(conf.VIDEO_IMAGE_SAVE_PATH, is_predict=True)
                    break

                elif keyword == ord('q') or keyword == ord('Q'):
                    break

        else:
            QMessageBox.warning(
                self,
                'Camera-0 not found',
                'Open camera(index 0) failed. Please check your hardware is working.'
            )

        my_camera.release()
        cv2.destroyAllWindows()
            
    def camera_stream_detect(self):
        my_camera = cv2.VideoCapture(0)
        is_video_opened = my_camera.isOpened()
        if is_video_opened:
            success, frame = my_camera.read()
            while success:
                success, frame = my_camera.read()
                self.model.predict(source=0, show=True)
                keyword = cv2.waitKey(0)
                
                if keyword:
                    my_camera.release()
                    cv2.destroyAllWindows()

        else:
            QMessageBox.warning(
                self,
                'Camera-0 not found',
                'Open camera(index 0) failed. Please check your hardware is working.'
            )

        my_camera.release()
        cv2.destroyAllWindows()

    def show_image_or_predict(self, img_path='', is_predict=False):
        if img_path != '':
            if is_predict:
                res = self.model.predict(os.path.abspath(img_path))
                res_plotted = res[0].plot()
                cv2.imshow('show img', res_plotted)
            else:
                cv2.namedWindow('show img', cv2.WINDOW_NORMAL)
                cv2.resizeWindow('show img', 800, 800)
                img = cv2.imread(os.path.abspath(img_path))
                cv2.imshow('show img', img)

            # waits for user to press any key
            # (this is necessary to avoid Python kernel form crashing)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        else:
            QMessageBox.information(
                self,
                "No Image Specified",
                "No Image Specified!"
            )

    def my_ui_init(self):
        # from UI file
        self.setupUi(self)

        # reset Icon file
        temp_for_icon = QIcon()
        # home pushbutton icon
        temp_for_icon.addFile(conf.UI_HOME_IMG_PATH, QSize(128, 128), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(temp_for_icon)
        self.pushButton_6.setIconSize(QSize(128, 128))

        # test pushbutton icon
        temp_for_icon1 = QIcon()
        temp_for_icon1.addFile(conf.UI_TEST_IMG_PATH, QSize(128, 128), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(temp_for_icon1)
        self.pushButton_7.setIconSize(QSize(128, 128))

        # predict pushbutton icon
        temp_for_icon2 = QIcon()
        temp_for_icon2.addFile(conf.UI_PREDICT_IMG_PATH, QSize(128, 128), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(temp_for_icon2)
        self.pushButton_8.setIconSize(QSize(128, 128))

        # Home page
        self.stackedWidget.setCurrentIndex(0)

# End of define


# Main
def the_main():
    my_app = QApplication(sys.argv)
    my_window = MyWindow()
    apply_stylesheet(my_app, 'dark_teal.xml')
    my_window.show()
    sys.exit(my_app.exec())

if __name__ == '__main__':
    # Create a GraphvizOutput object
    graph = GraphvizOutput(output_file='callgraph.png')
    # Create a PyCallGraph object and configure the options
    config = pycallgraph.Config(exclude=['pycallgraph', 'builtins', 'shibokensupport'], max_depth=3, groups=True)

    with PyCallGraph(output=graph, config=config):
        the_main()




