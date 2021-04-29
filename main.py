import sys

# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from PIL import Image
from PIL import ImageQt
import numpy as np
import PySide6.QtWidgets as Widgets
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
# QSizePolicy

from main_window import Ui_MainWindow
from rig import Rig


class CalcWindow(Widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_calc_ctc.clicked.connect(self.calculate_ctc)
        self.ui.button_calc_linear.clicked.connect(self.calculate_linear)

    def plot(self, title1, title2, data1, data2):
        fig = Figure(figsize=(6, 6), dpi=100)
        canvas = FigureCanvasAgg(fig)

        axs = fig.subplots(2, 1)
        fig.set_figheight(5)

        img1 = axs[0].scatter(self.rig.roll, self.rig.pitch, s=50, c=data1)
        axs[0].set_aspect('equal', 'box')
        axs[0].set_title(title1, fontsize=10)
        axs[0].set_xlabel('Degrees of Roll')
        axs[0].set_ylabel('Degrees of Pitch')
        fig.colorbar(img1, ax=axs[0])

        img2 = axs[1].scatter(self.rig.roll, self.rig.pitch, s=50, c=data2)
        axs[1].set_aspect('equal', 'box')
        axs[1].set_title(title2, fontsize=10)
        axs[1].set_xlabel('Degrees of Roll')
        axs[1].set_ylabel('Degrees of Pitch')
        fig.colorbar(img2, ax=axs[1])

        fig.tight_layout()

        canvas.draw()
        buf = canvas.buffer_rgba()
        X = np.asarray(buf)
        return ImageQt.ImageQt(Image.fromarray(X))

    def calculate_ctc(self):
        self.rig = Rig(np.array([float(self.ui.rod_mount_x_ctc.text()),
                                 float(self.ui.rod_mount_y_ctc.text()),
                                 float(self.ui.rod_mount_z_ctc.text())]),
                       np.array([float(self.ui.motor_x.text()),
                                 float(self.ui.motor_y.text()),
                                 float(self.ui.motor_z.text())]),
                       motor_angle=float(self.ui.motor_angle.text()),
                       motor_torque=float(self.ui.motor_torque_ctc.text()),
                       motor_rpm=float(self.ui.motor_rpm_ctc.text()),
                       ctc_length=float(self.ui.ctc_length.text()),
                       ctc_neutral_angle=float(self.ui.ctc_neutral_angle.text()),
                       ctc_total_rotation=float(self.ui.ctc_rotation.text()),
                       drive='ctc')

        self.rig.calculate()

        torque_plot = self.plot('Pitch Torque', 'Roll Torque', self.rig.pitch_torque, self.rig.roll_torque)
        omega_plot = self.plot('Pitch Torque', 'Roll Torque', self.rig.pitch_omega, self.rig.roll_omega)
        self.ui.torques_label.setPixmap(QPixmap.fromImage(torque_plot))
        self.ui.omegas_label.setPixmap(QPixmap.fromImage(omega_plot))

        self.ui.zx_rodmount_angle_ctc.setText(str(round(self.rig.zx_rodmount_angle_ctc, 2)))
        self.ui.zx_pushrod_angle_ctc.setText(str(round(self.rig.zx_pushrod_angle_ctc, 2)))
        self.ui.xy_rodmount_pushrod_angle_ctc.setText(str(round(self.rig.xy_rodmount_pushrod_angle_ctc, 2)))
        self.ui.max_ctc_pushrod_angle.setText(str(round(self.rig.max_ctc_pushrod_angle, 2)))
        self.ui.min_ctc_pushrod_angle.setText(str(round(self.rig.min_ctc_pushrod_angle, 2)))

    def calculate_linear(self):
        self.rig = Rig(np.array([float(self.ui.rod_mount_x_linear.text()),
                                 float(self.ui.rod_mount_y_linear.text()),
                                 float(self.ui.rod_mount_z_linear.text())]),
                       np.array([float(self.ui.lower_mount_x_linear.text()),
                                 float(self.ui.lower_mount_y_linear.text()),
                                 float(self.ui.lower_mount_z_linear.text())]),
                       motor_torque=float(self.ui.motor_torque_linear.text()),
                       motor_rpm=float(self.ui.motor_rpm_linear.text()),
                       linear_travel=float(self.ui.linear_travel.text()),
                       screw_pitch=float(self.ui.screw_pitch.text()),
                       drive='linear')

        self.rig.calculate()

        torque_plot = self.plot('Pitch Torque', 'Roll Torque', self.rig.pitch_torque, self.rig.roll_torque)
        omega_plot = self.plot('Pitch Torque', 'Roll Torque', self.rig.pitch_omega, self.rig.roll_omega)
        self.ui.torques_label.setPixmap(QPixmap.fromImage(torque_plot))
        self.ui.omegas_label.setPixmap(QPixmap.fromImage(omega_plot))

        self.ui.zx_rodmount_angle_linear.setText(str(round(self.rig.zx_rodmount_angle_linear, 2)))
        self.ui.zx_pushrod_angle_linear.setText(str(round(self.rig.zx_pushrod_angle_linear, 2)))
        self.ui.xy_rodmount_pushrod_angle_linear.setText(str(round(self.rig.xy_rodmount_pushrod_angle_linear, 2)))


def run():
    app = Widgets.QApplication(sys.argv)

    window = CalcWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
