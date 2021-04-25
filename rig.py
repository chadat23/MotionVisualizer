import numpy as np
from scipy.optimize import fsolve

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from PIL import Image
from PIL import ImageQt


class Rig:
    def __init__(self, rod_mount, lower_pivot, motor_angle=0, motor_torque=0, motor_rpm=0,
                 ctc_length=0, ctc_rest_angle=0, ctc_total_rotation=0,
                 linear_travel=0, screw_pitch=0,
                 drive='', z_I=-1, x_I=-1):
        self.lower_pivot1 = lower_pivot
        self.lower_pivot2 = np.copy(lower_pivot)
        self.lower_pivot2[2] *= -1

        if drive == 'ctc':
            self.motor1_angle = np.radians(motor_angle)
            self.motor2_angle = -np.radians(motor_angle)
            self.ctc_rest_angle = np.radians(ctc_rest_angle)

            self.ctc_min_angle = self.ctc_rest_angle - np.radians(ctc_total_rotation) / 2
            self.ctc_max_angle = self.ctc_rest_angle + np.radians(ctc_total_rotation) / 2

            self.ctc_length = ctc_length

            ctc_point = self.calc_ctc_location(self.lower_pivot1, self.motor1_angle, self.ctc_rest_angle)
            self.push_rod_length = self.calc_length(rod_mount, ctc_point)

        elif drive == 'linear':
            self.linear_travel = linear_travel
            self.screw_pitch = screw_pitch

        self.rod_mount_width = 2 * rod_mount[2]
        self.rod_mount = rod_mount
        self.rod_mount_base_angle = np.arctan(rod_mount[1] / rod_mount[0])
        self.rod_mount_length = self.calc_length(rod_mount)

        self.motor_torque = motor_torque
        self.motor_rpm = motor_rpm

        # self.grid_spacing = np.radians(2.5)
        plot_steps = 15
        self.grid_spacing = np.radians(ctc_total_rotation) / plot_steps

        self.z_I = z_I
        self.x_I = x_I

        self.drive = drive

    @staticmethod
    def calc_length(point1, point2=np.zeros(3)):
        point = point1 - point2
        return (point[0] ** 2 + point[1] ** 2 + point[2] ** 2) ** 0.5

    def calc_ctc_location(self, motor_point, motor_angle, ctc_angle):
        ctc_x = motor_point[0] + self.ctc_length * np.cos(motor_angle) * np.cos(ctc_angle)
        ctc_y = motor_point[1] + self.ctc_length * np.sin(ctc_angle)
        ctc_z = motor_point[2] + self.ctc_length * np.sin(motor_angle) * np.cos(ctc_angle)

        return np.array([ctc_x, ctc_y, ctc_z])

    def calc_rod_mount_locations(self, ctc1_angle=0, ctc2_angle=0, pushrod1=0, pushrod2=0):
        def equations(p, rod_mount_length, push_rod1_length, push_rod2_length, rod_mount_spacing, ctc1, ctc2):
            x1, x2, y1, y2, z1, z2 = p

            return (rod_mount_length ** 2 - (x1 ** 2 + y1 ** 2 + z1 ** 2),
                    rod_mount_length ** 2 - (x2 ** 2 + y2 ** 2 + z2 ** 2),
                    rod_mount_spacing ** 2 - ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2),
                    push_rod1_length ** 2 - ((x1 - ctc1[0]) ** 2
                                            + (y1 - ctc1[1]) ** 2
                                            + (z1 - ctc1[2]) ** 2),
                    push_rod2_length ** 2 - ((x2 - ctc2[0]) ** 2
                                            + (y2 - ctc2[1]) ** 2
                                            + (z2 - ctc2[2]) ** 2),
                    x1 - x2)

        # calc for ctc end positions
        if ctc1_angle:
            lower_pivot1 = self.calc_ctc_location(self.lower_pivot1, self.motor1_angle, ctc1_angle)
            lower_pivot2 = self.calc_ctc_location(self.lower_pivot2, self.motor2_angle, ctc2_angle)
            pushrod1 = self.push_rod_length
            pushrod2 = self.push_rod_length
        elif pushrod1:
            lower_pivot1 = self.lower_pivot1
            lower_pivot2 = self.lower_pivot1

        rm = self.rod_mount
        x1, x2, y1, y2, z1, z2 = fsolve(equations, (rm[0], rm[0], rm[1], rm[1], rm[2], -rm[2]),
                                        (self.rod_mount_length,
                                         pushrod1,
                                         pushrod2,
                                         self.rod_mount_width,
                                         lower_pivot1,
                                         lower_pivot2)
                                        )

        return np.array([x1, y1, z1]), np.array([x2, y2, z2])

    # def calc_max_pitch_and_roll(self):
    #     """
    #
    #     This tends to slightly underestimate the max roll given how it works but it is close.
    #
    #     :return:
    #     """
    #     rod_mount_point1, rod_mount_point2 = self.calc_rod_mount_locations(self.ctc_max_angle, self.ctc_max_angle)
    #     pitch, _ = self.calc_pitch_and_roll(rod_mount_point1, rod_mount_point2)
    #
    #     rod_mount_point1, rod_mount_point2 = self.calc_rod_mount_locations(self.ctc_max_angle, self.ctc_min_angle)
    #     _, roll = self.calc_pitch_and_roll(rod_mount_point1, rod_mount_point2)
    #
    #     return pitch - self.rod_mount_base_angle, roll

    @staticmethod
    def calc_pitch_and_roll(rod_mount1, rod_mount2):
        d_mounts = rod_mount1 - rod_mount2
        mounts_avg = (rod_mount1 + rod_mount2) / 2

        roll = np.arctan(d_mounts[1] / d_mounts[2])

        h = mounts_avg[1] / np.cos(roll)
        pitch = np.arctan(h / mounts_avg[0])

        return pitch, roll

    def calc_performance(self, d_angle):
        d_angle = np.radians(d_angle)

        def numerical_derivative(ctc_angle1_t0, ctc_angle2_t0, ctc_angle1_t1, ctc_angle2_t1):
            rod_mount1_t0, rod_mount2_t0 = self.calc_rod_mount_locations(ctc_angle1_t0, ctc_angle2_t0)
            rod_mount1_t1, rod_mount2_t1 = self.calc_rod_mount_locations(ctc_angle1_t1, ctc_angle2_t1)

            pitch1, roll1 = self.calc_pitch_and_roll(rod_mount1_t0, rod_mount2_t0)
            pitch2, roll2 = self.calc_pitch_and_roll(rod_mount1_t1, rod_mount2_t1)

            return (pitch2 - pitch1) / (2 * d_angle), (roll2 - roll1) / (2 * d_angle)

        def torques(pitch_ratio, roll_ratio):
            pitch = self.motor_torque / pitch_ratio * 2
            roll = self.motor_torque / roll_ratio * 2

            return pitch, roll

        def omegas(pitch_ratio, roll_ratio):
            motor_speed = self.motor_rpm * 360 / 60

            pitch = motor_speed * pitch_ratio
            roll = motor_speed * roll_ratio

            return pitch, roll

        def angles(ctc1_angle, ctc2_angle):
            rod_mount1, rod_mount2 = self.calc_rod_mount_locations(ctc1_angle, ctc2_angle)

            return self.calc_pitch_and_roll(rod_mount1, rod_mount2)

        self.pitch_torque = []
        self.roll_torque = []
        self.pitch_omega = []
        self.roll_omega = []
        self.pitch = []
        self.roll = []

        for i, ctc1_angle in enumerate(np.arange(self.ctc_min_angle,
                                                 self.ctc_max_angle + self.grid_spacing,
                                                 self.grid_spacing)):
            for j, ctc2_angle in enumerate(np.arange(self.ctc_min_angle,
                                                     self.ctc_max_angle + self.grid_spacing,
                                                     self.grid_spacing)):
                pitch_ratio, _ = numerical_derivative(ctc1_angle - d_angle,
                                                      ctc2_angle - d_angle,
                                                      ctc1_angle + d_angle,
                                                      ctc2_angle + d_angle)
                _, roll_ratio = numerical_derivative(ctc1_angle - d_angle,
                                                     ctc2_angle + d_angle,
                                                     ctc1_angle + d_angle,
                                                     ctc2_angle - d_angle)
                pitch_torque, roll_torque = torques(pitch_ratio, roll_ratio)
                pitch_omega, roll_omega = omegas(pitch_ratio, roll_ratio)
                pitch, roll = angles(ctc1_angle, ctc2_angle)

                self.pitch.append(np.degrees(pitch - self.rod_mount_base_angle))
                self.roll.append(np.degrees(roll))
                self.pitch_torque.append(pitch_torque)
                self.roll_torque.append(roll_torque)
                self.pitch_omega.append(pitch_omega)
                self.roll_omega.append(roll_omega)

                if i == 0 and j == 18:
                    a = 0

        break_point = 0

    def calculate(self):
        def plot(title1, title2, data1, data2):
            fig = Figure(figsize=(5, 4), dpi=100)
            canvas = FigureCanvasAgg(fig)

            axs = fig.subplots(2, 1)

            img1 = axs[0].scatter(self.roll, self.pitch, s=50, c=data1)
            axs[0].set_aspect('equal', 'box')
            axs[0].set_title(title1, fontsize=10)
            fig.colorbar(img1, ax=axs[0])
            # axs[0].legend(['2', '4'])
            # axs[0].legend(sorted(data1)[::int(len(data1) / 4)])

            img2 = axs[1].scatter(self.roll, self.pitch, s=50, c=data2)
            axs[1].set_aspect('equal', 'box')
            axs[1].set_title(title2, fontsize=10)
            fig.colorbar(img2, ax=axs[1])

            fig.tight_layout()

            canvas.draw()
            buf = canvas.buffer_rgba()
            X = np.asarray(buf)
            return ImageQt.ImageQt(Image.fromarray(X))

        # pitch and roll
        # self.max_pitch, self.max_roll = self.calc_max_pitch_and_roll()

        self.calc_performance(2)

        # p1, _ = self.calc_rod_mount_locations(np.radians(90), np.radians(90))
        # p2, _ = self.calc_rod_mount_locations(np.radians(0), np.radians(0))
        # p1, _ = self.calc_rod_mount_locations(np.radians(90), np.radians(0))
        # p2, _ = self.calc_rod_mount_locations(np.radians(0), np.radians(90))

        self.torque_plot = plot('Pitch Torque', 'Roll Torque', self.pitch_torque, self.roll_torque)
        self.omega_plot = plot('Pitch Omega', 'Roll Omega', self.pitch_omega, self.roll_omega)
