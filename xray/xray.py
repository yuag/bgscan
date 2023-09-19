import sys
import os
import hashlib
import threading
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QVBoxLayout, QWidget, QPushButton
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.central_layout = QVBoxLayout(self.centralwidget)
        self.central_layout.setObjectName("central_layout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.central_layout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.central_layout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.central_layout.addWidget(self.label)
        self.xray_path_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.xray_path_entry.setObjectName("xray_path_entry")
        self.central_layout.addWidget(self.xray_path_entry)
        self.url_listwidget = QtWidgets.QListWidget(self.centralwidget)
        self.url_listwidget.setObjectName("url_listwidget")
        self.central_layout.addWidget(self.url_listwidget)
        self.button_widget = QWidget(self.centralwidget)
        self.button_layout = QVBoxLayout(self.button_widget)
        self.pushButton_3 = QtWidgets.QPushButton(self.button_widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.button_layout.addWidget(self.pushButton_3)
        self.central_layout.addWidget(self.button_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "选择xray路径"))
        self.pushButton_2.setText(_translate("MainWindow", "选择url文件"))
        self.label.setText(_translate("MainWindow",        "xray批量扫描"))
        self.pushButton_3.setText(_translate("MainWindow", "开始扫描"))

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.select_xray_path)
        self.ui.pushButton_2.clicked.connect(self.select_url_file)
        self.ui.pushButton_3.clicked.connect(self.start_scan)

    def select_xray_path(self):
        xray_path = QFileDialog.getOpenFileName(self, "选择Xray路径")[0]
        if xray_path:
            self.ui.xray_path_entry.setText(xray_path)

    def select_url_file(self):
        file_path = QFileDialog.getOpenFileName(self, "选择包含URL的文件")[0]
        if file_path:
            with open(file_path, 'r') as file:
                for line in file:
                    self.add_url_to_list(line.strip())

    def start_scan(self):
        target_urls = [self.ui.url_listwidget.item(i).text() for i in range(self.ui.url_listwidget.count())]
        if not target_urls:
            print("请添加目标URL")
            return

        xray_path = self.ui.xray_path_entry.text()
        if not os.path.isfile(xray_path):
            print("Xray路径无效，请重新选择")
            return

        for target_url in target_urls:
            target_url = target_url.strip()
            if not target_url:
                continue

            self.scan_url(target_url, xray_path)

        print("所有扫描任务已完成")

    def scan_url(self, target_url, xray_path=None):
        if xray_path is None:
            xray_path = ""

        output_filename = "xray.html"
        scan_command = f"{xray_path} webscan --basic-crawler {target_url} --html-output {output_filename}"
        os.system(scan_command)

    def add_url_to_list(self, url):
        item = QListWidgetItem(url)
        self.ui.url_listwidget.addItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())