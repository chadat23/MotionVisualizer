import sys

# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import numpy as np
import PySide6.QtWidgets as Widgets
from PySide6.QtGui import QPixmap

from main_window import Ui_MainWindow
from rig import Rig


# from PySide6.QtGui import QCloseEvent


# pyside6-uic main_window.ui > main_window.py
# pyside6-rcc main_window.qrc > main_window_rc.py

# import os
#
# os.environ['QT_API'] = 'pyside6'
#
# import sys
#
# from PySide6 import QtWidgets
#
# from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas, \
#     NavigationToolbar2QT as NavigationToolbar
#
# from matplotlib.figure import Figure
#
# class ApplicationWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self._main = QtWidgets.QWidget()
#         self.setCentralWidget(self._main)
#         layout = QtWidgets.QVBoxLayout(self._main)
#
#         self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
#         layout.addWidget(self.canvas)
#
#         self.ax = self.canvas.figure.subplots()
#         self.ax2, =self.canvas.figure.get_axes()
#         assert self.ax is self.ax2
#         self.ax.plot([1, 2, 3], [1, 2, 3])
#
#         self.addToolBar(NavigationToolbar(self.canvas, self))


class CalcWindow(Widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_calc.clicked.connect(self.calculate)

    def calculate(self):
        if self.ui.z_I.text():
            z_I = float(self.ui.z_I.text())
        else:
            z_I = -1
        if self.ui.x_I.text():
            x_I = float(self.ui.x_I.text())
        else:
            x_I = -1

        self.rig = Rig(np.array([float(self.ui.rod_mount_x.text()),
                                 float(self.ui.rod_mount_y.text()),
                                 float(self.ui.rod_mount_z.text())]),
                       np.array([float(self.ui.motor_x.text()),
                                 float(self.ui.motor_y.text()),
                                 float(self.ui.motor_z.text())]),
                       float(self.ui.motor_angle.text()),
                       float(self.ui.motor_torque.text()),
                       float(self.ui.motor_rpm.text()),
                       float(self.ui.ctc_length.text()),
                       float(self.ui.ctc_rest_angle.text()),
                       float(self.ui.ctc_rotation.text()),
                       float(self.ui.ctc_current_angle.text()),
                       z_I, x_I)

        self.rig.calculate()

        self.ui.torques_label.setPixmap(QPixmap.fromImage(self.rig.torque_plot))
        self.ui.omegas_label.setPixmap(QPixmap.fromImage(self.rig.omega_plot))


def run():
    app = Widgets.QApplication(sys.argv)

    window = CalcWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
