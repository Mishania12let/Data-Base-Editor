# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\misa5\Desktop\work\Data-Base-Editor\mydbeditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 61, 16))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 781, 401))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.frame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 621, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.create_table_push_button = QtWidgets.QPushButton(self.tab)
        self.create_table_push_button.setEnabled(True)
        self.create_table_push_button.setGeometry(QtCore.QRect(10, 310, 591, 61))
        self.create_table_push_button.setObjectName("create_table_push_button")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label_2.setObjectName("label_2")
        self.table_name_line = QtWidgets.QLineEdit(self.tab)
        self.table_name_line.setGeometry(QtCore.QRect(80, 10, 281, 20))
        self.table_name_line.setObjectName("table_name_line")
        self.primaryKeyComboBox = QtWidgets.QComboBox(self.tab)
        self.primaryKeyComboBox.setGeometry(QtCore.QRect(80, 40, 281, 22))
        self.primaryKeyComboBox.setObjectName("primaryKeyComboBox")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label_4.setObjectName("label_4")
        self.fields_list_create_table = QtWidgets.QListWidget(self.tab)
        self.fields_list_create_table.setGeometry(QtCore.QRect(340, 81, 251, 131))
        self.fields_list_create_table.setObjectName("fields_list_create_table")
        self.field_input_frame = QtWidgets.QFrame(self.tab)
        self.field_input_frame.setGeometry(QtCore.QRect(10, 70, 591, 231))
        self.field_input_frame.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.field_input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field_input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field_input_frame.setObjectName("field_input_frame")
        self.field_type_combo_box = QtWidgets.QComboBox(self.field_input_frame)
        self.field_type_combo_box.setGeometry(QtCore.QRect(70, 50, 151, 18))
        self.field_type_combo_box.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.field_type_combo_box.setObjectName("field_type_combo_box")
        self.field_type_combo_box.addItem("")
        self.field_type_combo_box.addItem("")
        self.field_type_combo_box.addItem("")
        self.field_type_combo_box.addItem("")
        self.label_7 = QtWidgets.QLabel(self.field_input_frame)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_7.setObjectName("label_7")
        self.res_sql_statement = QtWidgets.QTextBrowser(self.field_input_frame)
        self.res_sql_statement.setGeometry(QtCore.QRect(10, 80, 211, 51))
        self.res_sql_statement.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.res_sql_statement.setObjectName("res_sql_statement")
        self.label_6 = QtWidgets.QLabel(self.field_input_frame)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_6.setObjectName("label_6")
        self.field_title_input = QtWidgets.QLineEdit(self.field_input_frame)
        self.field_title_input.setGeometry(QtCore.QRect(70, 10, 151, 20))
        self.field_title_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.field_title_input.setText("")
        self.field_title_input.setObjectName("field_title_input")
        self.delete_field_btn = QtWidgets.QPushButton(self.field_input_frame)
        self.delete_field_btn.setEnabled(False)
        self.delete_field_btn.setGeometry(QtCore.QRect(330, 150, 251, 61))
        self.delete_field_btn.setStyleSheet("QPushButton:hover\n"
"{\n"
"background-color:rgb(230, 230, 255);\n"
"color: black;\n"
"}\n"
"")
        self.delete_field_btn.setObjectName("delete_field_btn")
        self.add_field_btn = QtWidgets.QPushButton(self.field_input_frame)
        self.add_field_btn.setGeometry(QtCore.QRect(10, 150, 211, 61))
        self.add_field_btn.setStyleSheet("QPushButton:hover\n"
"{\n"
"background-color:rgb(230, 230, 255);\n"
"color: black;\n"
"}\n"
"")
        self.add_field_btn.setObjectName("add_field_btn")
        self.label_8 = QtWidgets.QLabel(self.field_input_frame)
        self.label_8.setGeometry(QtCore.QRect(280, 10, 41, 16))
        self.label_8.setObjectName("label_8")
        self.field_input_frame.raise_()
        self.create_table_push_button.raise_()
        self.label_2.raise_()
        self.table_name_line.raise_()
        self.primaryKeyComboBox.raise_()
        self.label_4.raise_()
        self.fields_list_create_table.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label_15.setObjectName("label_15")
        self.table_name_line_3 = QtWidgets.QLineEdit(self.tab_2)
        self.table_name_line_3.setGeometry(QtCore.QRect(80, 10, 281, 20))
        self.table_name_line_3.setObjectName("table_name_line_3")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label_16.setObjectName("label_16")
        self.primaryKeyComboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.primaryKeyComboBox_3.setEnabled(False)
        self.primaryKeyComboBox_3.setGeometry(QtCore.QRect(80, 40, 281, 22))
        self.primaryKeyComboBox_3.setObjectName("primaryKeyComboBox_3")
        self.field_input_frame_3 = QtWidgets.QFrame(self.tab_2)
        self.field_input_frame_3.setGeometry(QtCore.QRect(10, 70, 591, 231))
        self.field_input_frame_3.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"background-color: rgb(255, 158, 126);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.field_input_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.field_input_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field_input_frame_3.setObjectName("field_input_frame_3")
        self.field_type_combo_box_4 = QtWidgets.QComboBox(self.field_input_frame_3)
        self.field_type_combo_box_4.setGeometry(QtCore.QRect(70, 70, 151, 18))
        self.field_type_combo_box_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.field_type_combo_box_4.setObjectName("field_type_combo_box_4")
        self.field_type_combo_box_4.addItem("")
        self.field_type_combo_box_4.addItem("")
        self.field_type_combo_box_4.addItem("")
        self.field_type_combo_box_4.addItem("")
        self.label_17 = QtWidgets.QLabel(self.field_input_frame_3)
        self.label_17.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_17.setObjectName("label_17")
        self.res_sql_statement_4 = QtWidgets.QTextBrowser(self.field_input_frame_3)
        self.res_sql_statement_4.setGeometry(QtCore.QRect(10, 100, 211, 41))
        self.res_sql_statement_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.res_sql_statement_4.setObjectName("res_sql_statement_4")
        self.label_18 = QtWidgets.QLabel(self.field_input_frame_3)
        self.label_18.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_18.setObjectName("label_18")
        self.field_title_input_4 = QtWidgets.QLineEdit(self.field_input_frame_3)
        self.field_title_input_4.setGeometry(QtCore.QRect(70, 10, 151, 20))
        self.field_title_input_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.field_title_input_4.setText("")
        self.field_title_input_4.setObjectName("field_title_input_4")
        self.delete_field_btn_4 = QtWidgets.QPushButton(self.field_input_frame_3)
        self.delete_field_btn_4.setEnabled(False)
        self.delete_field_btn_4.setGeometry(QtCore.QRect(330, 150, 251, 61))
        self.delete_field_btn_4.setStyleSheet("QPushButton:hover\n"
"{\n"
"background-color:rgb(230, 230, 255);\n"
"color: black;\n"
"}\n"
"")
        self.delete_field_btn_4.setObjectName("delete_field_btn_4")
        self.add_field_btn_4 = QtWidgets.QPushButton(self.field_input_frame_3)
        self.add_field_btn_4.setGeometry(QtCore.QRect(10, 150, 211, 61))
        self.add_field_btn_4.setStyleSheet("QPushButton:hover\n"
"{\n"
"background-color:rgb(230, 230, 255);\n"
"color: black;\n"
"}\n"
"")
        self.add_field_btn_4.setObjectName("add_field_btn_4")
        self.label_19 = QtWidgets.QLabel(self.field_input_frame_3)
        self.label_19.setGeometry(QtCore.QRect(280, 10, 41, 16))
        self.label_19.setObjectName("label_19")
        self.fields_list_create_table_3 = QtWidgets.QListWidget(self.field_input_frame_3)
        self.fields_list_create_table_3.setGeometry(QtCore.QRect(330, 10, 251, 131))
        self.fields_list_create_table_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.fields_list_create_table_3.setObjectName("fields_list_create_table_3")
        self.update_field_title_btn = QtWidgets.QPushButton(self.field_input_frame_3)
        self.update_field_title_btn.setEnabled(False)
        self.update_field_title_btn.setGeometry(QtCore.QRect(70, 40, 151, 23))
        self.update_field_title_btn.setStyleSheet("QPushButton:hover\n"
"{\n"
"background-color:rgb(230, 230, 255);\n"
"color: black;\n"
"}\n"
"")
        self.update_field_title_btn.setObjectName("update_field_title_btn")
        self.update_table_name_btn = QtWidgets.QPushButton(self.tab_2)
        self.update_table_name_btn.setGeometry(QtCore.QRect(370, 10, 151, 23))
        self.update_table_name_btn.setObjectName("update_table_name_btn")
        self.field_input_frame_3.raise_()
        self.label_15.raise_()
        self.table_name_line_3.raise_()
        self.label_16.raise_()
        self.primaryKeyComboBox_3.raise_()
        self.update_table_name_btn.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.frame)
        self.delete_table_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_table_btn.setEnabled(False)
        self.delete_table_btn.setGeometry(QtCore.QRect(10, 430, 151, 61))
        self.delete_table_btn.setCheckable(False)
        self.delete_table_btn.setDefault(False)
        self.delete_table_btn.setFlat(False)
        self.delete_table_btn.setObjectName("delete_table_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "QListWidget"))
        self.create_table_push_button.setText(_translate("MainWindow", "Create table"))
        self.label_2.setText(_translate("MainWindow", "Table name"))
        self.label_4.setText(_translate("MainWindow", "Primary Key"))
        self.field_type_combo_box.setItemText(0, _translate("MainWindow", "TEXT"))
        self.field_type_combo_box.setItemText(1, _translate("MainWindow", "INTEGER"))
        self.field_type_combo_box.setItemText(2, _translate("MainWindow", "REAL"))
        self.field_type_combo_box.setItemText(3, _translate("MainWindow", "DATE"))
        self.label_7.setText(_translate("MainWindow", "Field type"))
        self.res_sql_statement.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Field title"))
        self.delete_field_btn.setText(_translate("MainWindow", "Delete selected field"))
        self.add_field_btn.setText(_translate("MainWindow", "Add field"))
        self.label_8.setText(_translate("MainWindow", "Fields:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Create table"))
        self.label_15.setText(_translate("MainWindow", "Table name"))
        self.label_16.setText(_translate("MainWindow", "Primary Key"))
        self.field_type_combo_box_4.setItemText(0, _translate("MainWindow", "TEXT"))
        self.field_type_combo_box_4.setItemText(1, _translate("MainWindow", "INTEGER"))
        self.field_type_combo_box_4.setItemText(2, _translate("MainWindow", "REAL"))
        self.field_type_combo_box_4.setItemText(3, _translate("MainWindow", "DATE"))
        self.label_17.setText(_translate("MainWindow", "Field type"))
        self.res_sql_statement_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "Field title"))
        self.delete_field_btn_4.setText(_translate("MainWindow", "Delete selected field"))
        self.add_field_btn_4.setText(_translate("MainWindow", "Add field"))
        self.label_19.setText(_translate("MainWindow", "Fields:"))
        self.update_field_title_btn.setText(_translate("MainWindow", "update field title"))
        self.update_table_name_btn.setText(_translate("MainWindow", "update table name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Edit table"))
        self.delete_table_btn.setText(_translate("MainWindow", "Delete selected table"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
