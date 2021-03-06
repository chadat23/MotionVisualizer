import numpy as np
from scipy.optimize import fsolve

CTC = 'ctc'
LINEAR = 'linear'


class Rig:
    def __init__(self, rod_mount, lower_pivot, motor_angle=0, motor_torque=0, motor_rpm=0,
                 ctc_length=0, ctc_neutral_angle=0, ctc_total_rotation=0,
                 linear_travel=0, screw_pitch=0, i_pitch=0, i_roll=0,
                 pitch_linear_rad=0, roll_linear_rad=0,
                 drive=''):
        self.lower_pivot1 = lower_pivot
        self.lower_pivot2 = np.copy(lower_pivot)
        self.lower_pivot2[2] *= -1

        plot_steps = 16  # must be even for max speed to be calculated
        if drive == CTC:
            self.motor1_angle = np.radians(motor_angle)
            self.motor2_angle = -np.radians(motor_angle)
            self.ctc_neutral_angle = np.radians(ctc_neutral_angle)

            self.ctc_min_angle = self.ctc_neutral_angle - np.radians(ctc_total_rotation) / 2
            self.ctc_max_angle = self.ctc_neutral_angle + np.radians(ctc_total_rotation) / 2
            self.pushrod_min_length = -100

            self.ctc_length = ctc_length

            ctc_point = self._calc_ctc_location(self.lower_pivot1, self.motor1_angle, self.ctc_neutral_angle)
            self.pushrod_length = self._calc_length(rod_mount, ctc_point)

            self.grid_spacing = np.radians(ctc_total_rotation) / plot_steps

        elif drive == LINEAR:
            self.linear_travel = linear_travel
            self.screw_pitch = screw_pitch

            self.pushrod_nominal_length = self._calc_length(rod_mount, lower_pivot)
            self.pushrod_min_length = self.pushrod_nominal_length - linear_travel / 2
            self.pushrod_max_length = self.pushrod_nominal_length + linear_travel / 2
            self.ctc_min_angle = -10000

            self.travel_per_rad = screw_pitch / (2 * np.pi)

            self.grid_spacing = linear_travel / plot_steps

        self.rod_mount_width = 2 * rod_mount[2]
        self.rod_mount = rod_mount
        self.rod_mount_base_angle = np.arctan(rod_mount[1] / rod_mount[0])
        self.rod_mount_length = self._calc_length(rod_mount)

        self.motor_torque = motor_torque
        self.motor_rpm = motor_rpm

        self.i_pitch = i_pitch
        self.i_roll = i_roll

        self.pitch_linear_rad = pitch_linear_rad
        self.roll_linear_rad = roll_linear_rad

        self.drive = drive

    @staticmethod
    def _calc_length(point1, point2=np.zeros(3)):
        """
        Calculates the Euclidean distance between a single point and the
        origin, or two points.

        :param array[float, float, float] point1: a point of interest
        :param array[float, float, float] point2: an optional point of interest
        :return: The distance between the points as a float.
        """

        point = point1 - point2
        return (point[0] ** 2 + point[1] ** 2 + point[2] ** 2) ** 0.5

    def _calc_ctc_location(self, motor_point, motor_angle, ctc_angle):
        """
        Calculate the location of the end of the ctc that's connected to the pushrod

        :param array[float, float, float] motor_point: The X, Y, Z location of
        the point about which the CTC rotates.
        :param float motor_angle: The angle between the rig's longitudinal centerline
        and the CTC.
        :param float ctc_angle: The angle between the horizontal and the CTC.
        :return: Numpy array with the X, Y, Z location of the point.
        """

        ctc_x = motor_point[0] + self.ctc_length * np.cos(motor_angle) * np.cos(ctc_angle)
        ctc_y = motor_point[1] + self.ctc_length * np.sin(ctc_angle)
        ctc_z = motor_point[2] + self.ctc_length * np.sin(motor_angle) * np.cos(ctc_angle)

        return np.array([ctc_x, ctc_y, ctc_z])

    # def _calc_rod_mount_points(self, position1, position2, estimated_coords):
    def _calc_rod_mount_points(self, position1, position2, estimated_points):
        """
        Calculates the Rod Mount position.

        :param array[float, float, float] position1: The first CTC or linear actuator
        mount location.
        :param array[float, float, float] position2: The second CTC or linear actuator
        mount location.
        :param list[float, float, float, float, float, float] estimated_coords: Estimated
        locations of the two Rod Mount points. The nominal location can be a good option
        if a better one isn't known. It's in the form X1, X2, Y1, Y2, Z1, Z2.
        :return:
        """

        def equations(p, rod_mount_length, pushrod1_length, pushrod2_length, rod_mount_spacing, ctc1, ctc2):
            x1, x2, y1, y2, z1, z2 = p

            return (rod_mount_length ** 2 - (x1 ** 2 + y1 ** 2 + z1 ** 2),
                    rod_mount_length ** 2 - (x2 ** 2 + y2 ** 2 + z2 ** 2),
                    rod_mount_spacing ** 2 - ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2),
                    pushrod1_length ** 2 - ((x1 - ctc1[0]) ** 2
                                            + (y1 - ctc1[1]) ** 2
                                            + (z1 - ctc1[2]) ** 2),
                    pushrod2_length ** 2 - ((x2 - ctc2[0]) ** 2
                                            + (y2 - ctc2[1]) ** 2
                                            + (z2 - ctc2[2]) ** 2),
                    x1 - x2)

        # calc for ctc end positions
        if self.drive == CTC:
            lower_pivot1 = self._calc_ctc_location(self.lower_pivot1, self.motor1_angle, position1)
            lower_pivot2 = self._calc_ctc_location(self.lower_pivot2, self.motor2_angle, position2)
            pushrod1 = self.pushrod_length
            pushrod2 = self.pushrod_length
        elif self.drive == LINEAR:
            lower_pivot1 = self.lower_pivot1
            lower_pivot2 = self.lower_pivot2
            pushrod1 = position1
            pushrod2 = position2

        try:
            ((x1, y1, z1), (x2, y2, z2)) = estimated_points
        except:
            a = 9
        estimated_coords = x1, x2, y1, y2, z1, z2
        estimated_coords = [v if abs(v) > 1e-5 else 0 for v in estimated_coords]
        x1, x2, y1, y2, z1, z2 = fsolve(equations, estimated_coords,
                                        (self.rod_mount_length,
                                         pushrod1,
                                         pushrod2,
                                         self.rod_mount_width,
                                         lower_pivot1,
                                         lower_pivot2)
                                        )

        return np.array([x1, y1, z1]), np.array([x2, y2, z2])

    @staticmethod
    def _calc_pitch_and_roll(rod_mount1, rod_mount2):
        """
        Calculate the pitch and roll given the location of the Rod Mounts.

        Assumes that the Rod Mounts aren't nominally above the pivot point.
        This must be accounted for elsewhere.

        :param array[float, float, float] rod_mount1: The first Rod Mount.
        :param array[float, float, float] rod_mount2: The second Rod Mount.
        :return: A tuple of floats containing the pitch and roll.
        """

        d_mounts = rod_mount1 - rod_mount2
        mounts_avg = (rod_mount1 + rod_mount2) / 2

        roll = np.arctan(d_mounts[1] / d_mounts[2])

        midpoint_height = mounts_avg[1] / np.cos(roll)
        pitch = np.arctan(midpoint_height / mounts_avg[0])

        return pitch, roll

    def _get_starting_points(self):
        """
        Gets estimated locations of the Rod Mounts at an extreme point.

        Allows for looping from one extreme to another so that previously
        solved locations can be used as estimates of future locations.

        Since iterative solving is used by _calc_performance,
        this can make things going faster and more reliably.

        :return: The coordinates of the two rod mounts, as floats, in
        the form X1, X2, Y1, Y2, Z1, Z2.
        """

        rm = self.rod_mount
        estimated_points = np.array([rm[0], rm[1], rm[2]]), np.array([rm[0], rm[1], -rm[2]])

        if self.drive == CTC:
            for angle in np.arange(self.ctc_neutral_angle,
                                   self.ctc_min_angle - self.grid_spacing / 2,
                                   -self.grid_spacing):
                estimated_points = self._calc_rod_mount_points(angle, angle, estimated_points)
        elif self.drive == LINEAR:
            for length in np.arange(self.pushrod_nominal_length,
                                    self.pushrod_min_length - self.grid_spacing / 2,
                                    -self.grid_spacing):
                estimated_points = self._calc_rod_mount_points(length, length, estimated_points)

        return estimated_points

    def _grid_points(self):
        """
        Create a generator to iterate over all of the points of interest.

        Also sets delta, the amount in each direction from each
        point of interest that's used to estimate the gear ratio of the
        sim rig.

        yields: the angles of the two CTCs, or the two Pushrod lengths as a tuple.
        """
        if self.drive == CTC:
            delta = 1  # values will be checked one degree on either side of the nominal position
            self.delta = np.radians(delta)

            for ctc1_angle in np.arange(self.ctc_min_angle,
                                        self.ctc_max_angle + self.grid_spacing / 2,
                                        self.grid_spacing):
                for ctc2_angle in np.arange(self.ctc_min_angle,
                                            self.ctc_max_angle + self.grid_spacing / 2,
                                            self.grid_spacing):
                    yield ctc1_angle, ctc2_angle

        elif self.drive == LINEAR:
            delta = 1  # values will be checked 1 percent of linear travel on either side of the nominal position
            self.delta = self.linear_travel / 100 * delta

            for pushrod1_length in np.arange(self.pushrod_min_length,
                                             self.pushrod_max_length + self.grid_spacing / 2,
                                             self.grid_spacing):
                for pushrod2_length in np.arange(self.pushrod_min_length,
                                                 self.pushrod_max_length + self.grid_spacing / 2,
                                                 self.grid_spacing):
                    yield pushrod1_length, pushrod2_length

    def _numerical_derivative(self, position1_t0, position2_t0, position1_t1, position2_t1, estimated_points):
        """
        Estimates the numerical derivative of pitch and roll as a function
        of either CTC angle or linear actuator length.

        Estimates the effective gear ratio between the motor and the rocker.

        :param float position1_t0: The starting point of either the CTC angle or
        linear actuator position of the respective value on the positive Z side.
        :param float position2_t0: The starting point of either the CTC angle or
        linear actuator position of the respective value on the negative Z side.
        :param float position1_t1: The ending point of either the CTC angle or
        linear actuator position of the respective value on the positive Z side.
        :param float position2_t1: The ending point of either the CTC angle or
        linear actuator position of the respective value on the negative Z side.
        :param tuple[X1, X2, Y1, Y2, Z1, Z2] estimated_points: The estimates
        locations of the points, the last solved set of locations can be a good
        estimate

        :return: The effective gear ratio as a tuple of floats representing
        the pitch and roll ratios.
        """
        rod_mount1_t0, rod_mount2_t0 = self._calc_rod_mount_points(position1_t0, position2_t0, estimated_points)
        rod_mount1_t1, rod_mount2_t1 = self._calc_rod_mount_points(position1_t1, position2_t1, estimated_points)

        pitch1, roll1 = self._calc_pitch_and_roll(rod_mount1_t0, rod_mount2_t0)
        pitch2, roll2 = self._calc_pitch_and_roll(rod_mount1_t1, rod_mount2_t1)

        if self.drive == CTC:
            return (pitch2 - pitch1) / (2 * self.delta), (roll2 - roll1) / (2 * self.delta)
        elif self.drive == LINEAR:
            return ((pitch2 - pitch1) / (2 * self.delta / self.travel_per_rad),
                    (roll2 - roll1) / (2 * self.delta / self.travel_per_rad))

    def _calc_performance(self):
        """
        Calculates the performance metrics of the sim rig.

        Sets values to:
        self.pitch_torque = []
        self.roll_torque = []
        self.pitch_omega = []
        self.roll_omega = []
        self.pitch = []
        self.roll = []

        Values are set in no particular order but are in the same
        order for each list so the Nth item for each list references
        the same point.

        :return: None
        """

        def pushrod_force(torque, position1, position2, estimated_points):
            ((x1, y1, z1), (x2, y2, z2)) = estimated_points
            rod_mount1, rod_mount2 = self._calc_rod_mount_points(position1, position2, estimated_points)

            if self.drive == CTC:
                mount = self._calc_ctc_location(self.lower_pivot1, self.motor1_angle, position1)
            elif self.drive == LINEAR:
                mount = self.lower_pivot1

            unit_vector = (rod_mount1 - mount) / self.rod_mount_length

            return torque / (2 * (-unit_vector[0] * rod_mount1[1] + unit_vector[1] * rod_mount1[0]))

        self.pitch_torque = []
        self.roll_torque = []
        self.pitch_omega = []
        self.roll_omega = []
        self.pitch_alpha = []
        self.roll_alpha = []
        self.pitch = []
        self.roll = []
        self.pitch_linear_speed = []
        self.roll_linear_speed = []
        self.pitch_linear_acc = []
        self.roll_linear_acc = []
        self.max_pushrod_force = []

        motor_speed = self.motor_rpm * 360 / 60
        last_estimated_points = self._get_starting_points()
        for i, (position1, position2) in enumerate(self._grid_points()):
            if np.isclose(position2, self.pushrod_min_length) or np.isclose(position2, self.ctc_min_angle):
                estimated_points = last_estimated_points
            else:
                estimated_points = self._calc_rod_mount_points(position1, position2, estimated_points)

            pitch_ratio, _ = self._numerical_derivative(position1 - self.delta,
                                                        position2 - self.delta,
                                                        position1 + self.delta,
                                                        position2 + self.delta,
                                                        estimated_points)
            _, roll_ratio = self._numerical_derivative(position1 - self.delta,
                                                       position2 + self.delta,
                                                       position1 + self.delta,
                                                       position2 - self.delta,
                                                       estimated_points)

            rod_mount1, rod_mount2 = self._calc_rod_mount_points(position1, position2, estimated_points)
            pitch, roll = self._calc_pitch_and_roll(rod_mount1, rod_mount2)
            self.pitch.append(np.degrees(pitch - self.rod_mount_base_angle))
            self.roll.append(np.degrees(roll))
            self.pitch_torque.append(self.motor_torque / pitch_ratio * 2)
            self.roll_torque.append(self.motor_torque / roll_ratio * 2)
            self.pitch_omega.append(motor_speed * pitch_ratio)
            self.roll_omega.append(motor_speed * roll_ratio)
            self.pitch_alpha.append(np.degrees(self.pitch_torque[-1] / self.i_pitch))
            self.roll_alpha.append(np.degrees(self.roll_torque[-1] / self.i_roll))
            self.pitch_linear_acc.append(self.pitch_alpha[-1] * self.pitch_linear_rad)
            self.roll_linear_acc.append(self.roll_alpha[-1] * self.roll_linear_rad)
            self.pitch_linear_speed.append(np.radians(self.pitch_omega[-1]) * self.pitch_linear_rad)
            self.roll_linear_speed.append(np.radians(self.roll_omega[-1]) * self.roll_linear_rad)
            self.max_pushrod_force.append(pushrod_force(self.pitch_torque[-1] / 2,
                                                        position1,
                                                        position2,
                                                        estimated_points))

            if np.isclose(0, pitch - self.rod_mount_base_angle) and np.isclose(0, roll):
                self.median_pitch_and_roll_torques = (self.pitch_torque[-1], self.roll_torque[-1])
                self.pitch_roll_ratio = self.pitch_torque[-1] / self.roll_torque[-1]

        self.max_pushrod_force = max(self.max_pushrod_force)

        # print(self.pitch)
        # print(self.roll)
        # print(self.pitch_torque)
        # print(self.roll_torque)
        # print(self.pitch_omega)
        # print(self.roll_omega)

    def calculate(self):
        """
        The main function that solves the rig.

        Sets values to:
        self.pitch_torque = []
        self.roll_torque = []
        self.pitch_omega = []
        self.roll_omega = []
        self.pitch = []
        self.roll = []

        Values are set in no particular order but are in the same
        order for each list so the Nth item for each list references
        the same point.

        And:

        Assigns values to:
        self.zx_rodmount_angle_ctc
        self.zx_pushrod_angle_ctc
        self.xy_rodmount_pushrod_angle_ctc
        self.max_ctc_pushrod_angle
        self.min_ctc_pushrod_angle

        Or:
        self.zx_rodmount_angle_linear
        self.zx_pushrod_angle_linear
        self.xy_rodmount_pushrod_angle_linear

        :return: None
        """
        self._calc_performance()

        self._get_angles()

        if self.i_pitch > 0 and self.i_roll > 0:
            self._get_max_speeds()
        else:
            self.max_pitch_speed = -1
            self.max_roll_speed = -1

    def _get_angles(self):
        """
        Gets a few angles of interest.

        Assigns values to:
        self.zx_rodmount_angle_ctc
        self.zx_pushrod_angle_ctc
        self.xy_rodmount_pushrod_angle_ctc
        self.max_ctc_pushrod_angle
        self.min_ctc_pushrod_angle

        Or:
        self.zx_rodmount_angle_linear
        self.zx_pushrod_angle_linear
        self.xy_rodmount_pushrod_angle_linear

        :return: None
        """

        def rodmount_pushrod_inner_angle(pivot_lower_mount, rodmount, rodmount_lower_mount):
            angle = np.arccos((pivot_lower_mount ** 2 - rodmount ** 2 - rodmount_lower_mount ** 2) /
                              (- 2 * rodmount * rodmount_lower_mount))
            return np.degrees(angle)

        if self.drive == CTC:
            self.zx_rodmount_angle_ctc = 2 * np.degrees(np.arctan(self.rod_mount[2] / self.rod_mount[0]))

            ctc_location = self._calc_ctc_location(self.lower_pivot1, self.motor1_angle, self.ctc_neutral_angle)
            self.zx_pushrod_angle_ctc = 2 * np.degrees(np.arctan((self.rod_mount[2] - ctc_location[2]) /
                                                                 (self.rod_mount[0] - ctc_location[0])))

            pivot_ctc = self._calc_length(ctc_location)
            rodmount = self.rod_mount_length
            rodmount_ctc = self._calc_length(self.rod_mount, ctc_location)
            self.xy_rodmount_pushrod_angle_ctc = rodmount_pushrod_inner_angle(pivot_ctc, rodmount, rodmount_ctc)

            rm = self.rod_mount
            estimated_points = np.array([rm[0], rm[1], rm[2]]), np.array([rm[0], rm[1], -rm[2]])

            ctc_location1 = self._calc_ctc_location(self.lower_pivot1, self.motor1_angle, self.ctc_max_angle)
            rodmount_point1, _ = self._calc_rod_mount_points(self.ctc_max_angle, self.ctc_max_angle, estimated_points)
            pushrod_angle1 = np.arctan((rodmount_point1[1] - ctc_location1[1]) /
                                       (rodmount_point1[0] - ctc_location1[0])) + np.pi
            self.max_ctc_pushrod_angle = np.degrees(pushrod_angle1 - self.ctc_max_angle)

            ctc_location2 = self._calc_ctc_location(self.lower_pivot1, self.motor1_angle, self.ctc_min_angle)
            rodmount_point2, _ = self._calc_rod_mount_points(self.ctc_min_angle, self.ctc_min_angle, estimated_points)
            pushrod_angle2 = np.arctan((rodmount_point2[1] - ctc_location2[1]) /
                                       (rodmount_point2[0] - ctc_location2[0]))
            self.min_ctc_pushrod_angle = np.degrees(self.ctc_min_angle - pushrod_angle2)

        elif self.drive == LINEAR:
            self.zx_rodmount_angle_linear = 2 * np.degrees(np.arctan(self.rod_mount[2] / self.rod_mount[0]))

            self.zx_pushrod_angle_linear = 2 * np.degrees(np.arctan((self.rod_mount[2] - self.lower_pivot1[2]) /
                                                                    (self.rod_mount[0] - self.lower_pivot1[0])))

            pivot_ctc = self._calc_length(self.lower_pivot1)
            rodmount = self.rod_mount_length
            pushrod = self.pushrod_nominal_length
            self.xy_rodmount_pushrod_angle_linear = rodmount_pushrod_inner_angle(pivot_ctc, rodmount, pushrod)

    def _get_max_speeds(self):

        def max_speed(angle, torque, inertia):
            acceleration = torque / inertia
            t = (angle * 2 / acceleration) ** 0.5
            return acceleration * t

        try:
            pitch_torque, roll_torque = self.median_pitch_and_roll_torques

            self.max_pitch_speed = max_speed(max(self.pitch) * 2, pitch_torque, self.i_pitch)
            self.max_roll_speed = max_speed(max(self.roll) * 2, roll_torque, self.i_roll)
        except:
            self.max_pitch_speed = -1
            self.max_roll_speed = -1
