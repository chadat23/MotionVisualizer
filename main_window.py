# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import main_window_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1145, 622)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(10, 10, 671, 541))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 431, 341))
        self.tabs.addTab(self.tab, "")
        self.outputs_tab = QWidget()
        self.outputs_tab.setObjectName(u"outputs_tab")
        self.outputs_table = QTableWidget(self.outputs_tab)
        if (self.outputs_table.columnCount() < 4):
            self.outputs_table.setColumnCount(4)
        if (self.outputs_table.rowCount() < 7):
            self.outputs_table.setRowCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.outputs_table.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.outputs_table.setItem(0, 1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.outputs_table.setItem(0, 2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.outputs_table.setItem(0, 3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.outputs_table.setItem(1, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.outputs_table.setItem(2, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.outputs_table.setItem(3, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.outputs_table.setItem(4, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.outputs_table.setItem(4, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.outputs_table.setItem(5, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.outputs_table.setItem(6, 0, __qtablewidgetitem10)
        self.outputs_table.setObjectName(u"outputs_table")
        self.outputs_table.setEnabled(True)
        self.outputs_table.setGeometry(QRect(10, 10, 411, 221))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputs_table.sizePolicy().hasHeightForWidth())
        self.outputs_table.setSizePolicy(sizePolicy)
        self.outputs_table.setAutoScroll(True)
        self.outputs_table.setAutoScrollMargin(16)
        self.outputs_table.setRowCount(7)
        self.outputs_table.setColumnCount(4)
        self.outputs_table.horizontalHeader().setVisible(False)
        self.outputs_table.horizontalHeader().setMinimumSectionSize(39)
        self.outputs_table.horizontalHeader().setHighlightSections(True)
        self.outputs_table.horizontalHeader().setStretchLastSection(False)
        self.outputs_table.verticalHeader().setVisible(False)
        self.outputs_table.verticalHeader().setStretchLastSection(False)
        self.tabs.addTab(self.outputs_tab, "")
        self.torque_tab = QWidget()
        self.torque_tab.setObjectName(u"torque_tab")
        self.torques_label = QLabel(self.torque_tab)
        self.torques_label.setObjectName(u"torques_label")
        self.torques_label.setGeometry(QRect(10, 10, 651, 481))
        self.tabs.addTab(self.torque_tab, "")
        self.omega_tab = QWidget()
        self.omega_tab.setObjectName(u"omega_tab")
        self.omegas_label = QLabel(self.omega_tab)
        self.omegas_label.setObjectName(u"omegas_label")
        self.omegas_label.setGeometry(QRect(10, 10, 651, 481))
        self.tabs.addTab(self.omega_tab, "")
        self.inputs_tab = QTabWidget(self.centralwidget)
        self.inputs_tab.setObjectName(u"inputs_tab")
        self.inputs_tab.setGeometry(QRect(680, 0, 461, 531))
        self.ctc_tab = QWidget()
        self.ctc_tab.setObjectName(u"ctc_tab")
        self.groupBox = QGroupBox(self.ctc_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 431, 361))
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 20, 131, 331))
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 30, 121, 16))
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 50, 16, 16))
        self.rod_mount_x_ctc = QLineEdit(self.groupBox_3)
        self.rod_mount_x_ctc.setObjectName(u"rod_mount_x_ctc")
        self.rod_mount_x_ctc.setGeometry(QRect(20, 50, 101, 22))
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 80, 16, 16))
        self.rod_mount_y_ctc = QLineEdit(self.groupBox_3)
        self.rod_mount_y_ctc.setObjectName(u"rod_mount_y_ctc")
        self.rod_mount_y_ctc.setGeometry(QRect(20, 80, 101, 22))
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 110, 16, 16))
        self.rod_mount_z_ctc = QLineEdit(self.groupBox_3)
        self.rod_mount_z_ctc.setObjectName(u"rod_mount_z_ctc")
        self.rod_mount_z_ctc.setGeometry(QRect(20, 110, 101, 22))
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 150, 121, 16))
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 230, 16, 16))
        self.motor_y = QLineEdit(self.groupBox_3)
        self.motor_y.setObjectName(u"motor_y")
        self.motor_y.setGeometry(QRect(20, 200, 101, 22))
        self.motor_z = QLineEdit(self.groupBox_3)
        self.motor_z.setObjectName(u"motor_z")
        self.motor_z.setGeometry(QRect(20, 230, 101, 22))
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 170, 16, 16))
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 200, 16, 16))
        self.motor_x = QLineEdit(self.groupBox_3)
        self.motor_x.setObjectName(u"motor_x")
        self.motor_x.setGeometry(QRect(20, 170, 101, 22))
        self.motor_angle = QLineEdit(self.groupBox_3)
        self.motor_angle.setObjectName(u"motor_angle")
        self.motor_angle.setGeometry(QRect(20, 290, 101, 22))
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 270, 121, 16))
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(150, 20, 131, 331))
        self.ctc_length = QLineEdit(self.groupBox_4)
        self.ctc_length.setObjectName(u"ctc_length")
        self.ctc_length.setGeometry(QRect(20, 50, 101, 22))
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 30, 121, 16))
        self.ctc_rest_angle = QLineEdit(self.groupBox_4)
        self.ctc_rest_angle.setObjectName(u"ctc_rest_angle")
        self.ctc_rest_angle.setGeometry(QRect(20, 100, 101, 22))
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 80, 121, 16))
        self.ctc_rotation = QLineEdit(self.groupBox_4)
        self.ctc_rotation.setObjectName(u"ctc_rotation")
        self.ctc_rotation.setGeometry(QRect(20, 150, 101, 22))
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 130, 121, 16))
        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 180, 121, 16))
        self.motor_torque_ctc = QLineEdit(self.groupBox_4)
        self.motor_torque_ctc.setObjectName(u"motor_torque_ctc")
        self.motor_torque_ctc.setGeometry(QRect(20, 200, 101, 22))
        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 230, 121, 16))
        self.motor_rpm_ctc = QLineEdit(self.groupBox_4)
        self.motor_rpm_ctc.setObjectName(u"motor_rpm_ctc")
        self.motor_rpm_ctc.setGeometry(QRect(20, 250, 101, 22))
        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 280, 121, 16))
        self.ctc_current_angle = QLineEdit(self.groupBox_4)
        self.ctc_current_angle.setObjectName(u"ctc_current_angle")
        self.ctc_current_angle.setGeometry(QRect(20, 300, 101, 22))
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(289, 20, 131, 141))
        self.z_I = QLineEdit(self.groupBox_5)
        self.z_I.setObjectName(u"z_I")
        self.z_I.setGeometry(QRect(20, 50, 101, 22))
        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 30, 121, 16))
        self.x_I = QLineEdit(self.groupBox_5)
        self.x_I.setObjectName(u"x_I")
        self.x_I.setGeometry(QRect(20, 100, 101, 22))
        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 80, 121, 16))
        self.groupBox_2 = QGroupBox(self.ctc_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 360, 431, 131))
        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(140, 10, 141, 141))
        self.max_roll_angle = QLineEdit(self.groupBox_6)
        self.max_roll_angle.setObjectName(u"max_roll_angle")
        self.max_roll_angle.setEnabled(False)
        self.max_roll_angle.setGeometry(QRect(10, 20, 121, 22))
        self.max_roll_torque = QLineEdit(self.groupBox_6)
        self.max_roll_torque.setObjectName(u"max_roll_torque")
        self.max_roll_torque.setEnabled(False)
        self.max_roll_torque.setGeometry(QRect(10, 50, 121, 22))
        self.max_roll_acc = QLineEdit(self.groupBox_6)
        self.max_roll_acc.setObjectName(u"max_roll_acc")
        self.max_roll_acc.setEnabled(False)
        self.max_roll_acc.setGeometry(QRect(10, 80, 121, 22))
        self.max_roll_speed = QLineEdit(self.groupBox_6)
        self.max_roll_speed.setObjectName(u"max_roll_speed")
        self.max_roll_speed.setEnabled(False)
        self.max_roll_speed.setGeometry(QRect(10, 110, 121, 22))
        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(289, 10, 141, 141))
        self.max_pitch_angle = QLineEdit(self.groupBox_7)
        self.max_pitch_angle.setObjectName(u"max_pitch_angle")
        self.max_pitch_angle.setEnabled(False)
        self.max_pitch_angle.setGeometry(QRect(10, 20, 121, 22))
        self.max_pitch_torque = QLineEdit(self.groupBox_7)
        self.max_pitch_torque.setObjectName(u"max_pitch_torque")
        self.max_pitch_torque.setEnabled(False)
        self.max_pitch_torque.setGeometry(QRect(10, 50, 121, 22))
        self.max_pitch_acc = QLineEdit(self.groupBox_7)
        self.max_pitch_acc.setObjectName(u"max_pitch_acc")
        self.max_pitch_acc.setEnabled(False)
        self.max_pitch_acc.setGeometry(QRect(10, 80, 121, 22))
        self.max_pitch_speed = QLineEdit(self.groupBox_7)
        self.max_pitch_speed.setObjectName(u"max_pitch_speed")
        self.max_pitch_speed.setEnabled(False)
        self.max_pitch_speed.setGeometry(QRect(10, 110, 121, 22))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 30, 71, 16))
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 90, 101, 20))
        self.label_22 = QLabel(self.groupBox_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 120, 111, 20))
        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 60, 111, 20))
        self.inputs_tab.addTab(self.ctc_tab, "")
        self.la_tab = QWidget()
        self.la_tab.setObjectName(u"la_tab")
        self.groupBox_8 = QGroupBox(self.la_tab)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(10, 0, 431, 361))
        self.groupBox_9 = QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(10, 20, 131, 331))
        self.label_24 = QLabel(self.groupBox_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 30, 121, 16))
        self.label_25 = QLabel(self.groupBox_9)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 50, 16, 16))
        self.rod_mount_x_la = QLineEdit(self.groupBox_9)
        self.rod_mount_x_la.setObjectName(u"rod_mount_x_la")
        self.rod_mount_x_la.setGeometry(QRect(20, 50, 101, 22))
        self.label_26 = QLabel(self.groupBox_9)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 80, 16, 16))
        self.rod_mount_y_la = QLineEdit(self.groupBox_9)
        self.rod_mount_y_la.setObjectName(u"rod_mount_y_la")
        self.rod_mount_y_la.setGeometry(QRect(20, 80, 101, 22))
        self.label_27 = QLabel(self.groupBox_9)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 110, 16, 16))
        self.rod_mount_z_la = QLineEdit(self.groupBox_9)
        self.rod_mount_z_la.setObjectName(u"rod_mount_z_la")
        self.rod_mount_z_la.setGeometry(QRect(20, 110, 101, 22))
        self.label_28 = QLabel(self.groupBox_9)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 150, 121, 16))
        self.label_29 = QLabel(self.groupBox_9)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 230, 16, 16))
        self.motor_y_2 = QLineEdit(self.groupBox_9)
        self.motor_y_2.setObjectName(u"motor_y_2")
        self.motor_y_2.setGeometry(QRect(20, 200, 101, 22))
        self.motor_z_2 = QLineEdit(self.groupBox_9)
        self.motor_z_2.setObjectName(u"motor_z_2")
        self.motor_z_2.setGeometry(QRect(20, 230, 101, 22))
        self.label_30 = QLabel(self.groupBox_9)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 170, 16, 16))
        self.label_31 = QLabel(self.groupBox_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 200, 16, 16))
        self.motor_x_2 = QLineEdit(self.groupBox_9)
        self.motor_x_2.setObjectName(u"motor_x_2")
        self.motor_x_2.setGeometry(QRect(20, 170, 101, 22))
        self.groupBox_10 = QGroupBox(self.groupBox_8)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(150, 20, 131, 331))
        self.la_travel = QLineEdit(self.groupBox_10)
        self.la_travel.setObjectName(u"la_travel")
        self.la_travel.setGeometry(QRect(20, 50, 101, 22))
        self.label_33 = QLabel(self.groupBox_10)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 30, 121, 16))
        self.la_pitch = QLineEdit(self.groupBox_10)
        self.la_pitch.setObjectName(u"la_pitch")
        self.la_pitch.setGeometry(QRect(20, 100, 101, 22))
        self.label_34 = QLabel(self.groupBox_10)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 80, 121, 16))
        self.label_36 = QLabel(self.groupBox_10)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, 130, 121, 16))
        self.motor_torque_ctc_2 = QLineEdit(self.groupBox_10)
        self.motor_torque_ctc_2.setObjectName(u"motor_torque_ctc_2")
        self.motor_torque_ctc_2.setGeometry(QRect(20, 150, 101, 22))
        self.label_37 = QLabel(self.groupBox_10)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 180, 121, 16))
        self.motor_rpm_ctc_2 = QLineEdit(self.groupBox_10)
        self.motor_rpm_ctc_2.setObjectName(u"motor_rpm_ctc_2")
        self.motor_rpm_ctc_2.setGeometry(QRect(20, 200, 101, 22))
        self.groupBox_11 = QGroupBox(self.groupBox_8)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(289, 20, 131, 141))
        self.z_I_2 = QLineEdit(self.groupBox_11)
        self.z_I_2.setObjectName(u"z_I_2")
        self.z_I_2.setGeometry(QRect(20, 50, 101, 22))
        self.label_39 = QLabel(self.groupBox_11)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 30, 121, 16))
        self.x_I_2 = QLineEdit(self.groupBox_11)
        self.x_I_2.setObjectName(u"x_I_2")
        self.x_I_2.setGeometry(QRect(20, 100, 101, 22))
        self.label_40 = QLabel(self.groupBox_11)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 80, 121, 16))
        self.button_calc_2 = QPushButton(self.groupBox_8)
        self.button_calc_2.setObjectName(u"button_calc_2")
        self.button_calc_2.setGeometry(QRect(320, 270, 75, 24))
        self.inputs_tab.addTab(self.la_tab, "")
        self.button_calc = QPushButton(self.centralwidget)
        self.button_calc.setObjectName(u"button_calc")
        self.button_calc.setGeometry(QRect(940, 550, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1145, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)
        self.inputs_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/images/images/whole_isometric.jpg\"/></p></body></html>", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Iso View", None))

        __sortingEnabled = self.outputs_table.isSortingEnabled()
        self.outputs_table.setSortingEnabled(False)
        ___qtablewidgetitem = self.outputs_table.item(0, 1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Front/Back", None));
        ___qtablewidgetitem1 = self.outputs_table.item(0, 2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Left/Right", None));
        ___qtablewidgetitem2 = self.outputs_table.item(0, 3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Middle", None));
        ___qtablewidgetitem3 = self.outputs_table.item(1, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Pitch Angle", None));
        ___qtablewidgetitem4 = self.outputs_table.item(2, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Roll Angle", None));
        ___qtablewidgetitem5 = self.outputs_table.item(3, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Pitch Torque", None));
        ___qtablewidgetitem6 = self.outputs_table.item(4, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Roll Torque", None));
        ___qtablewidgetitem7 = self.outputs_table.item(5, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Pitch Angular Speed", None));
        ___qtablewidgetitem8 = self.outputs_table.item(6, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Roll Angular Speed", None));
        self.outputs_table.setSortingEnabled(__sortingEnabled)

        self.tabs.setTabText(self.tabs.indexOf(self.outputs_tab), QCoreApplication.translate("MainWindow", u"Outputs", None))
        self.torques_label.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.torque_tab), QCoreApplication.translate("MainWindow", u"Torques", None))
        self.omegas_label.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.omega_tab), QCoreApplication.translate("MainWindow", u"Omegas", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Geometry", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rod Mount Position", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.rod_mount_x_ctc.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.rod_mount_y_ctc.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.rod_mount_z_ctc.setText(QCoreApplication.translate("MainWindow", u"8.5", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Motor Mount Position", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.motor_y.setText(QCoreApplication.translate("MainWindow", u"-8", None))
        self.motor_z.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.motor_x.setText(QCoreApplication.translate("MainWindow", u"45.5", None))
        self.motor_angle.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Motor Angle", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"CTC", None))
        self.ctc_length.setText(QCoreApplication.translate("MainWindow", u"2.5", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.ctc_rest_angle.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Rest Angle", None))
        self.ctc_rotation.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Total Rotation", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Motor Max Torque", None))
        self.motor_torque_ctc.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Motor Max RPM", None))
        self.motor_rpm_ctc.setText(QCoreApplication.translate("MainWindow", u"70", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Current Angle", None))
        self.ctc_current_angle.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Moment of Inertia", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"About Z", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"About X", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Outputs", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.max_roll_angle.setText("")
        self.max_roll_torque.setText("")
        self.max_roll_acc.setText("")
        self.max_roll_speed.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.max_pitch_angle.setText("")
        self.max_pitch_torque.setText("")
        self.max_pitch_acc.setText("")
        self.max_pitch_speed.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Max Angle", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Max Angular Acc", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Max Angular Speed", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Max Torque", None))
        self.inputs_tab.setTabText(self.inputs_tab.indexOf(self.ctc_tab), QCoreApplication.translate("MainWindow", u"CTC Based", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Geometry", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Rod Mount Pos.", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.rod_mount_x_la.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.rod_mount_y_la.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.rod_mount_z_la.setText(QCoreApplication.translate("MainWindow", u"8.5", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Actuator Mount Pos.", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.motor_y_2.setText(QCoreApplication.translate("MainWindow", u"-8", None))
        self.motor_z_2.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.motor_x_2.setText(QCoreApplication.translate("MainWindow", u"45.5", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Actuator", None))
        self.la_travel.setText(QCoreApplication.translate("MainWindow", u"2.5", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Travel", None))
        self.la_pitch.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Motor Max Torque", None))
        self.motor_torque_ctc_2.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Motor Max RPM", None))
        self.motor_rpm_ctc_2.setText(QCoreApplication.translate("MainWindow", u"70", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Moment of Inertia", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"About Z", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"About X", None))
        self.button_calc_2.setText(QCoreApplication.translate("MainWindow", u"Calc", None))
        self.inputs_tab.setTabText(self.inputs_tab.indexOf(self.la_tab), QCoreApplication.translate("MainWindow", u"Linear Actuator", None))
        self.button_calc.setText(QCoreApplication.translate("MainWindow", u"Calc", None))
    # retranslateUi

