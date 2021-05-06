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

import json

from main_window import Ui_MainWindow
from rig import Rig


class CalcWindow(Widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_calc_ctc.clicked.connect(self.calculate_ctc)
        self.ui.button_calc_linear.clicked.connect(self.calculate_linear)

        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionOpen.triggered.connect(self.open)

    def save(self):
        file = Widgets.QFileDialog.getSaveFileName(parent=self, caption='Save File',
                                                   filter='MotionVisualizer Files (*.mv)')

        info = {'rod_mount_x_ctc': str(self.ui.rod_mount_x_ctc.text()),
                'rod_mount_y_ctc': str(self.ui.rod_mount_y_ctc.text()),
                'rod_mount_z_ctc': str(self.ui.rod_mount_z_ctc.text()),
                'motor_x': str(self.ui.motor_x.text()),
                'motor_y': str(self.ui.motor_y.text()),
                'motor_z': str(self.ui.motor_z.text()),
                'motor_angle': str(self.ui.motor_angle.text()),
                'ctc_length': str(self.ui.ctc_length.text()),
                'ctc_neutral_angle': str(self.ui.ctc_neutral_angle.text()),
                'ctc_rotation': str(self.ui.ctc_rotation.text()),
                'motor_torque_ctc': str(self.ui.motor_torque_ctc.text()),
                'motor_rpm_ctc': str(self.ui.motor_rpm_ctc.text()),
                'i_pitch_ctc': str(self.ui.i_pitch_ctc.text()),
                'i_roll_ctc': str(self.ui.i_roll_ctc.text()),
                'pitch_linear_rad_ctc': str(self.ui.pitch_linear_rad_ctc.text()),
                'roll_linear_rad_ctc': str(self.ui.roll_linear_rad_ctc.text()),
                'rod_mount_x_linear': str(self.ui.rod_mount_x_linear.text()),
                'rod_mount_y_linear': str(self.ui.rod_mount_y_linear.text()),
                'rod_mount_z_linear': str(self.ui.rod_mount_z_linear.text()),
                'lower_mount_x_linear': str(self.ui.lower_mount_x_linear.text()),
                'lower_mount_y_linear': str(self.ui.lower_mount_y_linear.text()),
                'lower_mount_z_linear': str(self.ui.lower_mount_z_linear.text()),
                'linear_travel': str(self.ui.linear_travel.text()),
                'screw_pitch': str(self.ui.screw_pitch.text()),
                'motor_torque_linear': str(self.ui.motor_torque_linear.text()),
                'motor_rpm_linear': str(self.ui.motor_rpm_linear.text()),
                'i_pitch_linear': str(self.ui.i_pitch_linear.text()),
                'i_roll_linear': str(self.ui.i_roll_linear.text()),
                'pitch_linear_rad_linear': str(self.ui.pitch_linear_rad_linear.text()),
                'roll_linear_rad_linear': str(self.ui.roll_linear_rad_linear.text()),
                'inputs_tab_index': str(self.ui.inputs_tab.currentIndex()),
                'outputs_tab_index': str(self.ui.outputs_tab.currentIndex()),
                }

        info = json.dumps(info)
        with open(file[0], 'w') as f:
            f.write(info)

    def open(self):
        file = Widgets.QFileDialog.getOpenFileName(parent=self, caption='Open file',
                                                   filter='MotionVisualizer Files (*.mv)')

        with open(file[0], 'r') as f:
            info = json.loads(f.read())

        self.ui.rod_mount_x_ctc.setText(info['rod_mount_x_ctc'])
        self.ui.rod_mount_y_ctc.setText(info['rod_mount_y_ctc'])
        self.ui.rod_mount_z_ctc.setText(info['rod_mount_z_ctc'])
        self.ui.motor_x.setText(info['motor_x'])
        self.ui.motor_y.setText(info['motor_y'])
        self.ui.motor_z.setText(info['motor_z'])
        self.ui.motor_angle.setText(info['motor_angle'])
        self.ui.ctc_length.setText(info['ctc_length'])
        self.ui.ctc_neutral_angle.setText(info['ctc_neutral_angle'])
        self.ui.ctc_rotation.setText(info['ctc_rotation'])
        self.ui.motor_torque_ctc.setText(info['motor_torque_ctc'])
        self.ui.motor_rpm_ctc.setText(info['motor_rpm_ctc'])
        self.ui.i_pitch_ctc.setText(info['i_pitch_ctc'])
        self.ui.i_roll_ctc.setText(info['i_roll_ctc'])
        self.ui.pitch_linear_rad_ctc.setText(info['pitch_linear_rad_ctc'])
        self.ui.roll_linear_rad_ctc.setText(info['roll_linear_rad_ctc'])
        self.ui.rod_mount_x_linear.setText(info['rod_mount_x_linear'])
        self.ui.rod_mount_y_linear.setText(info['rod_mount_y_linear'])
        self.ui.rod_mount_z_linear.setText(info['rod_mount_z_linear'])
        self.ui.lower_mount_x_linear.setText(info['lower_mount_x_linear'])
        self.ui.lower_mount_y_linear.setText(info['lower_mount_y_linear'])
        self.ui.lower_mount_z_linear.setText(info['lower_mount_z_linear'])
        self.ui.linear_travel.setText(info['linear_travel'])
        self.ui.screw_pitch.setText(info['screw_pitch'])
        self.ui.motor_torque_linear.setText(info['motor_torque_linear'])
        self.ui.motor_rpm_linear.setText(info['motor_rpm_linear'])
        self.ui.i_pitch_linear.setText(info['i_pitch_linear'])
        self.ui.i_roll_linear.setText(info['i_roll_linear'])
        self.ui.pitch_linear_rad_linear.setText(info['pitch_linear_rad_linear'])
        self.ui.roll_linear_rad_linear.setText(info['roll_linear_rad_linear'])
        self.ui.inputs_tab.setCurrentIndex(int(info['inputs_tab_index']))
        self.ui.outputs_tab.setCurrentIndex(int(info['outputs_tab_index']))

        if int(info['inputs_tab_index']) == 0:
            self.calculate_ctc()
        elif int(info['inputs_tab_index']) == 1:
            self.calculate_linear()

    def plot(self, title1, title2, data1, data2, figure_title):
        fig = Figure(figsize=(6, 8), dpi=100)
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

        fig.suptitle(figure_title)

        fig.subplots_adjust(wspace=0.4, hspace=0.4)

        canvas.draw()
        buf = canvas.buffer_rgba()
        X = np.asarray(buf)
        return ImageQt.ImageQt(Image.fromarray(X))

    def make_plots(self):
        torque_plot = self.plot('Pitch Torque', 'Roll Torque', self.rig.pitch_torque, self.rig.roll_torque,
                                'Rocker Torque Calculated from Motor Torque Spec')
        omega_plot = self.plot('Pitch Omega (deg / sec)', 'Roll Omega (deg / sec)', self.rig.pitch_omega, self.rig.roll_omega,
                               'Rocker Omega Calculated from Motor RPM Spec')
        alpha_plot = self.plot('Pitch Alpha (deg / sec^2)', 'Roll Alpha (deg / sec^2)', self.rig.pitch_alpha, self.rig.roll_alpha,
                               'Rocker Alpha Calculated from Motor Torque Spec & Inertias')
        acc_plot = self.plot('Pitch Acceleration', 'Roll Acceleration',
                             self.rig.pitch_linear_acc, self.rig.roll_linear_acc,
                             'Linear Acc Calculated from Motor Torque Spec, Inertias, and Inspect. Rad.')
        speed_plot = self.plot('Pitch Speed', 'Roll Speed', self.rig.pitch_linear_speed, self.rig.roll_linear_speed,
                               'Linear Speed Calculated from Motor Torque Spec, Inertias, and Inspect. Rad.')
        self.ui.torques_label.setPixmap(QPixmap.fromImage(torque_plot))
        self.ui.omegas_label.setPixmap(QPixmap.fromImage(omega_plot))

        if (float(self.ui.i_pitch_ctc.text()) > 0 or float(self.ui.i_roll_ctc.text()) > 0 or
                float(self.ui.i_pitch_linear.text()) > 0 or float(self.ui.i_roll_linear.text()) > 0):
            self.ui.alphas_label.setPixmap(QPixmap.fromImage(alpha_plot))
            self.ui.linear_acc_label.setPixmap(QPixmap.fromImage(acc_plot))
            self.ui.linear_speed_label.setPixmap(QPixmap.fromImage(speed_plot))

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
                       i_pitch=float(self.ui.i_pitch_ctc.text()),
                       i_roll=float(self.ui.i_roll_ctc.text()),
                       pitch_linear_rad=float(self.ui.pitch_linear_rad_ctc.text()),
                       roll_linear_rad=float(self.ui.roll_linear_rad_ctc.text()),
                       drive='ctc')

        self.rig.calculate()

        self.make_plots()

        self.ui.zx_rodmount_angle_ctc.setText(str(round(self.rig.zx_rodmount_angle_ctc, 2)))
        self.ui.zx_pushrod_angle_ctc.setText(str(round(self.rig.zx_pushrod_angle_ctc, 2)))
        self.ui.xy_rodmount_pushrod_angle_ctc.setText(str(round(self.rig.xy_rodmount_pushrod_angle_ctc, 2)))
        self.ui.pushrod_length_ctc.setText(str(round(self.rig.pushrod_length, 2)))
        self.ui.max_ctc_pushrod_angle.setText(str(round(self.rig.max_ctc_pushrod_angle, 2)))
        self.ui.min_ctc_pushrod_angle.setText(str(round(self.rig.min_ctc_pushrod_angle, 2)))
        self.ui.max_pitch_omega_ctc.setText(str(round(self.rig.max_pitch_speed, 2)))
        self.ui.max_roll_omega_ctc.setText(str(round(self.rig.max_roll_speed, 2)))
        self.ui.pushrod_force_ctc.setText(str(round(self.rig.max_pushrod_force, 2)))

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
                       i_pitch=float(self.ui.i_pitch_linear.text()),
                       i_roll=float(self.ui.i_roll_linear.text()),
                       pitch_linear_rad=float(self.ui.pitch_linear_rad_linear.text()),
                       roll_linear_rad=float(self.ui.roll_linear_rad_linear.text()),
                       drive='linear')

        self.rig.calculate()

        self.make_plots()

        self.ui.zx_rodmount_angle_linear.setText(str(round(self.rig.zx_rodmount_angle_linear, 2)))
        self.ui.zx_pushrod_angle_linear.setText(str(round(self.rig.zx_pushrod_angle_linear, 2)))
        self.ui.xy_rodmount_pushrod_angle_linear.setText(str(round(self.rig.xy_rodmount_pushrod_angle_linear, 2)))
        self.ui.nominal_pushrod_length_linear.setText(str(round(self.rig.pushrod_nominal_length, 2)))
        self.ui.max_pitch_omega_linear.setText(str(round(self.rig.max_pitch_speed, 2)))
        self.ui.max_roll_omega_linear.setText(str(round(self.rig.max_roll_speed, 2)))
        self.ui.pushrod_force_linear.setText(str(round(self.rig.max_pushrod_force, 2)))


def run():
    app = Widgets.QApplication(sys.argv)

    window = CalcWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
