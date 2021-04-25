import numpy as np
from scipy.optimize import fsolve

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from PIL import Image
from PIL import ImageQt

CTC = 'ctc'
LINEAR = 'linear'


class Rig:
    def __init__(self, rod_mount, lower_pivot, motor_angle=0, motor_torque=0, motor_rpm=0,
                 ctc_length=0, ctc_rest_angle=0, ctc_total_rotation=0,
                 linear_travel=0, screw_pitch=0,
                 drive='', z_I=-1, x_I=-1):
        self.lower_pivot1 = lower_pivot
        self.lower_pivot2 = np.copy(lower_pivot)
        self.lower_pivot2[2] *= -1

        plot_steps = 15
        if drive == CTC:
            self.motor1_angle = np.radians(motor_angle)
            self.motor2_angle = -np.radians(motor_angle)
            self.ctc_rest_angle = np.radians(ctc_rest_angle)

            self.ctc_min_angle = self.ctc_rest_angle - np.radians(ctc_total_rotation) / 2
            self.ctc_max_angle = self.ctc_rest_angle + np.radians(ctc_total_rotation) / 2

            self.ctc_length = ctc_length

            ctc_point = self.calc_ctc_location(self.lower_pivot1, self.motor1_angle, self.ctc_rest_angle)
            self.push_rod_length = self.calc_length(rod_mount, ctc_point)

            self.grid_spacing = np.radians(ctc_total_rotation) / plot_steps

        elif drive == LINEAR:
            self.linear_travel = linear_travel
            self.screw_pitch = screw_pitch

            pushrod_length = self.calc_length(rod_mount, lower_pivot)
            self.pushrod_min_length = pushrod_length - linear_travel / 2
            self.pushrod_max_length = pushrod_length + linear_travel / 2

            self.travel_per_rad = screw_pitch / (2 * np.pi)

            self.grid_spacing = linear_travel / plot_steps

        self.rod_mount_width = 2 * rod_mount[2]
        self.rod_mount = rod_mount
        self.rod_mount_base_angle = np.arctan(rod_mount[1] / rod_mount[0])
        self.rod_mount_length = self.calc_length(rod_mount)

        self.motor_torque = motor_torque
        self.motor_rpm = motor_rpm

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

    def calc_rod_mount_locations(self, position1, position2):
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
        if self.drive == CTC:
            lower_pivot1 = self.calc_ctc_location(self.lower_pivot1, self.motor1_angle, position1)
            lower_pivot2 = self.calc_ctc_location(self.lower_pivot2, self.motor2_angle, position2)
            pushrod1 = self.push_rod_length
            pushrod2 = self.push_rod_length
        elif self.drive == LINEAR:
            lower_pivot1 = self.lower_pivot1
            lower_pivot2 = self.lower_pivot1
            pushrod1 = position1
            pushrod2 = position2

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

    def calc_performance(self):
        if self.drive == CTC:
            delta = 1  # values will be checked one degree on either side of the nominal position
            delta = np.radians(delta)

            def grid_points():
                for ctc1_angle in np.arange(self.ctc_min_angle,
                                            self.ctc_max_angle + self.grid_spacing / 2,
                                            self.grid_spacing):
                    for ctc2_angle in np.arange(self.ctc_min_angle,
                                                self.ctc_max_angle + self.grid_spacing / 2,
                                                self.grid_spacing):
                        yield ctc1_angle, ctc2_angle

        elif self.drive == LINEAR:
            delta = 1  # values will be checked 1 percent of linear travel on either side of the nominal position
            delta = self.linear_travel / 100 * delta

            def grid_points():
                for pushrod1_length in np.arange(self.pushrod_min_length,
                                                 self.pushrod_max_length + self.grid_spacing / 2,
                                                 self.grid_spacing):
                    for pushrod2_length in np.arange(self.pushrod_min_length,
                                                     self.pushrod_max_length + self.grid_spacing / 2,
                                                     self.grid_spacing):
                        yield pushrod1_length, pushrod2_length

        def numerical_derivative(position1_t0, position2_t0, position1_t1, position2_t1):
            rod_mount1_t0, rod_mount2_t0 = self.calc_rod_mount_locations(position1_t0, position2_t0)
            rod_mount1_t1, rod_mount2_t1 = self.calc_rod_mount_locations(position1_t1, position2_t1)

            pitch1, roll1 = self.calc_pitch_and_roll(rod_mount1_t0, rod_mount2_t0)
            pitch2, roll2 = self.calc_pitch_and_roll(rod_mount1_t1, rod_mount2_t1)

            if self.drive == CTC:
                return (pitch2 - pitch1) / (2 * delta), (roll2 - roll1) / (2 * delta)
            elif self.drive == LINEAR:
                return (pitch2 - pitch1) / (2 * delta / self.travel_per_rad), \
                       (roll2 - roll1) / (2 * delta / self.travel_per_rad)

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

        for position1, position2 in grid_points():
            pitch_ratio, _ = numerical_derivative(position1 - delta,
                                                  position2 - delta,
                                                  position1 + delta,
                                                  position2 + delta)
            _, roll_ratio = numerical_derivative(position1 - delta,
                                                 position2 + delta,
                                                 position1 + delta,
                                                 position2 - delta)
            pitch_torque, roll_torque = torques(pitch_ratio, roll_ratio)
            pitch_omega, roll_omega = omegas(pitch_ratio, roll_ratio)
            pitch, roll = angles(position1, position2)

            self.pitch.append(np.degrees(pitch - self.rod_mount_base_angle))
            self.roll.append(np.degrees(roll))
            self.pitch_torque.append(pitch_torque)
            self.roll_torque.append(roll_torque)
            self.pitch_omega.append(pitch_omega)
            self.roll_omega.append(roll_omega)

        # print(self.pitch)
        # print(self.roll)
        # print(self.pitch_torque)
        # print(self.roll_torque)
        # print(self.pitch_omega)
        # print(self.roll_omega)

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

        self.calc_performance()

        # p1, _ = self.calc_rod_mount_locations(np.radians(90), np.radians(90))
        # p2, _ = self.calc_rod_mount_locations(np.radians(0), np.radians(0))
        # p1, _ = self.calc_rod_mount_locations(np.radians(90), np.radians(0))
        # p2, _ = self.calc_rod_mount_locations(np.radians(0), np.radians(90))

        self.torque_plot = plot('Pitch Torque', 'Roll Torque', self.pitch_torque, self.roll_torque)
        self.omega_plot = plot('Pitch Omega', 'Roll Omega', self.pitch_omega, self.roll_omega)
