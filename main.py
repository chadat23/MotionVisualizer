import sys

# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import numpy as np
import PySide6.QtWidgets as Widgets
from PySide6.QtGui import QPixmap

from main_window import Ui_MainWindow
from rig import Rig


# pyside6-uic main_window.ui > main_window.py
# pyside6-rcc main_window.qrc > main_window_rc.py


class CalcWindow(Widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_calc_ctc.clicked.connect(self.calculate_ctc)
        self.ui.button_calc_linear.clicked.connect(self.calculate_linear)

    def calculate_ctc(self):
        if self.ui.z_I.text():
            z_I = float(self.ui.z_I.text())
        else:
            z_I = -1
        if self.ui.x_I.text():
            x_I = float(self.ui.x_I.text())
        else:
            x_I = -1

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
                       drive='ctc', z_I=z_I, x_I=x_I, )

        self.rig.calculate()

        self.ui.torques_label.setPixmap(QPixmap.fromImage(self.rig.torque_plot))
        self.ui.omegas_label.setPixmap(QPixmap.fromImage(self.rig.omega_plot))

        self.ui.zx_rodmount_angle_ctc.setText(str(round(self.rig.zx_rodmount_angle_ctc, 2)))
        self.ui.zx_pushrod_angle_ctc.setText(str(round(self.rig.zx_pushrod_angle_ctc, 2)))
        self.ui.xy_rodmount_pushrod_angle_ctc.setText(str(round(self.rig.xy_rodmount_pushrod_angle_ctc, 2)))
        self.ui.max_ctc_pushrod_angle.setText(str(round(self.rig.max_ctc_pushrod_angle, 2)))
        self.ui.min_ctc_pushrod_angle.setText(str(round(self.rig.min_ctc_pushrod_angle, 2)))

        # if self.ui.inputs_tab.currentWidget() == self.ui.ctc_tab:
        #     if self.ui.z_I.text():
        #         z_I = float(self.ui.z_I.text())
        #     else:
        #         z_I = -1
        #     if self.ui.x_I.text():
        #         x_I = float(self.ui.x_I.text())
        #     else:
        #         x_I = -1
        #
        #     self.rig = Rig(np.array([float(self.ui.rod_mount_x_ctc.text()),
        #                              float(self.ui.rod_mount_y_ctc.text()),
        #                              float(self.ui.rod_mount_z_ctc.text())]),
        #                    np.array([float(self.ui.motor_x.text()),
        #                              float(self.ui.motor_y.text()),
        #                              float(self.ui.motor_z.text())]),
        #                    motor_angle=float(self.ui.motor_angle.text()),
        #                    motor_torque=float(self.ui.motor_torque_ctc.text()),
        #                    motor_rpm=float(self.ui.motor_rpm_ctc.text()),
        #                    ctc_length=float(self.ui.ctc_length.text()),
        #                    ctc_neutral_angle=float(self.ui.ctc_neutral_angle.text()),
        #                    ctc_total_rotation=float(self.ui.ctc_rotation.text()),
        #                    drive='ctc', z_I=z_I, x_I=x_I, )
        #
        # elif self.ui.inputs_tab.currentWidget() == self.ui.la_tab:
        #     if self.ui.z_I_linear.text():
        #         z_I = float(self.ui.z_I_linear.text())
        #     else:
        #         z_I = -1
        #     if self.ui.x_I_linear.text():
        #         x_I = float(self.ui.x_I_linear.text())
        #     else:
        #         x_I = -1
        #
        #     self.rig = Rig(np.array([float(self.ui.rod_mount_x_linear.text()),
        #                              float(self.ui.rod_mount_y_linear.text()),
        #                              float(self.ui.rod_mount_z_linear.text())]),
        #                    np.array([float(self.ui.lower_mount_x_linear.text()),
        #                              float(self.ui.lower_mount_y_linear.text()),
        #                              float(self.ui.lower_mount_z_linear.text())]),
        #                    motor_torque=float(self.ui.motor_torque_linear.text()),
        #                    motor_rpm=float(self.ui.motor_rpm_linear.text()),
        #                    linear_travel=float(self.ui.linear_travel.text()),
        #                    screw_pitch=float(self.ui.screw_pitch.text()),
        #                    drive='linear', z_I=z_I, x_I=x_I, )
        #
        # self.rig.calculate()
        #
        # self.ui.torques_label.setPixmap(QPixmap.fromImage(self.rig.torque_plot))
        # self.ui.omegas_label.setPixmap(QPixmap.fromImage(self.rig.omega_plot))
        #
        # if self.ui.inputs_tab.currentWidget() == self.ui.ctc_tab:
        #     self.ui.zx_rodmount_angle_ctc.setText(str(round(self.rig.zx_rodmount_angle_ctc, 2)))
        #     self.ui.zx_pushrod_angle_ctc.setText(str(round(self.rig.zx_pushrod_angle_ctc, 2)))
        #     self.ui.xy_rodmount_pushrod_angle_ctc.setText(str(round(self.rig.xy_rodmount_pushrod_angle_ctc, 2)))
        # elif self.ui.inputs_tab.currentWidget() == self.ui.la_tab:
        #     self.ui.zx_rodmount_angle_linear.setText(str(round(self.rig.zx_rodmount_angle_linear, 2)))
        #     self.ui.zx_pushrod_angle_linear.setText(str(round(self.rig.zx_pushrod_angle_linear, 2)))
        #     self.ui.xy_rodmount_pushrod_angle_linear.setText(str(round(self.rig.xy_rodmount_pushrod_angle_linear, 2)))

    def calculate_linear(self):
        if self.ui.z_I_linear.text():
            z_I = float(self.ui.z_I_linear.text())
        else:
            z_I = -1
        if self.ui.x_I_linear.text():
            x_I = float(self.ui.x_I_linear.text())
        else:
            x_I = -1

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
                       drive='linear', z_I=z_I, x_I=x_I, )

        self.rig.calculate()

        self.ui.torques_label.setPixmap(QPixmap.fromImage(self.rig.torque_plot))
        self.ui.omegas_label.setPixmap(QPixmap.fromImage(self.rig.omega_plot))

        self.ui.zx_rodmount_angle_linear.setText(str(round(self.rig.zx_rodmount_angle_linear, 2)))
        self.ui.zx_pushrod_angle_linear.setText(str(round(self.rig.zx_pushrod_angle_linear, 2)))
        self.ui.xy_rodmount_pushrod_angle_linear.setText(str(round(self.rig.xy_rodmount_pushrod_angle_linear, 2)))

        # self.ui.zx_rodmount_angle_ctc
        # self.ui.zx_rodmount_angle_linear
        # self.ui.zx_pushrod_angle_ctc
        # self.ui.zx_pushrod_angle_linear
        # self.ui.xy_rodmount_pushrod_angle_ctc
        # self.ui.xy_rodmount_pushrod_angle_linear


def run():
    app = Widgets.QApplication(sys.argv)

    window = CalcWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
