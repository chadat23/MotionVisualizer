from rig import Rig

import numpy as np
import pytest


# @pytest.fixture
# def rig_inputs():
#     rod_mount = np.array([2., 1., 10.0])
#     motor_point = np.array([0.0, 0.0, 10.0])
#
#     motor_angle = 0
#
#     ctc_length = 2
#     rest_angle = 0
#     total_rotation = 0
#     motor_torque = 48
#     motor_rpm = 70
#     current_angle = 60
#
#     z_I = 400
#     x_I = 300
#
#     return (rod_mount, motor_point,
#             motor_angle, motor_torque, motor_rpm,
#             ctc_length, rest_angle, total_rotation, current_angle,
#             z_I, x_I)


# @pytest.fixture
# def rig_inputs():
#     rod_mount = np.array([150.0, 600.0, 100.0])
#     motor_point = np.array([450.0, 100.0, 200.0])
#
#     motor_angle = 45
#
#     ctc_length = 100
#     rest_angle = 30
#     total_rotation = 60
#     motor_torque = 40e3
#     motor_rpm = 70
#     current_angle = 60
#
#     z_I = 400
#     x_I = 300
#
#     return (rod_mount, motor_point,
#             motor_angle, motor_torque, motor_rpm,
#             ctc_length, rest_angle, total_rotation, current_angle,
#             z_I, x_I)


@pytest.fixture
def rig_inputs():
    rod_mount = np.array([23., 28.0, 8.5])
    motor_point = np.array([45.5, -8., 13.])

    motor_angle = 10

    ctc_length = 2.5
    rest_angle = 45
    total_rotation = 45
    motor_torque = 40*12
    motor_rpm = 70
    current_angle = 60

    z_I = 400
    x_I = 300

    return (rod_mount, motor_point,
            motor_angle, motor_torque, motor_rpm,
            ctc_length, rest_angle, total_rotation, current_angle,
            z_I, x_I)


@pytest.fixture
def rig_w_I(rig_inputs):
    (rod_mount, motor_point,
     motor_angle, motor_torque, motor_rpm,
     ctc_length, rest_angle, total_rotation, current_angle,
     z_I, x_I) = rig_inputs

    rig = Rig(rod_mount, motor_point,
              motor_angle, motor_torque, motor_rpm,
              ctc_length, rest_angle, total_rotation, current_angle,
              z_I, x_I)

    return rig


@pytest.fixture
def point_w_length():
    point = np.array([3, 4, 5])
    length = 7.0710678118654755

    return point, length


@pytest.fixture
def points_w_length():
    point1 = np.array([3, 4, 5])
    point2 = np.array([8, 10, 12])
    length = 10.488088481701515

    return point1, point2, length


@pytest.fixture
def ctc_location_info():
    motor_point, motor_angle, ctc_angle = np.array([450.0, 100.0, 200.0]), np.radians(45), np.radians(30)

    ctc_location = np.array([511.23724357, 150.0, 261.23724357])
    # ctc_location = np.array([-8., -93.,  -2.])

    return motor_point, motor_angle, ctc_angle, ctc_location


@pytest.fixture
def ctc_angles_w_rod_mount_locations():
    ctc_angle1 = np.radians(30)
    ctc_angle2 = np.radians(30)

    point1 = np.array([150.0, 600.0, 100.0])
    point2 = np.array([150.0, 600.0, -100.0])

    return ctc_angle1, ctc_angle2, point1, point2


@pytest.fixture
def ctc_angles_w_rod_mount_locations():
    ctc_angle1 = np.radians(30)
    ctc_angle2 = np.radians(30)

    point1 = np.array([150.0, 600.0, 100.0])
    point2 = np.array([150.0, 600.0, -100.0])

    return ctc_angle1, ctc_angle2, point1, point2


@pytest.fixture
def point_to_rotate_and_new_point_quad1():
    angle = np.radians(-30)
    origin_point = np.array([4.0, 5.0, 6.0])
    point = np.array([4.0 + 8.660254037844387, 8.0, 6.0 + 5.0])

    destination = np.array([14, 8.0, 6.0])

    return angle, origin_point, point, destination


@pytest.fixture
def point_to_rotate_and_new_point_quad2():
    angle = np.radians(-30)
    origin_point = np.array([4.0, 5.0, 6.0])
    point = np.array([-4.0 - 8.660254037844387, 8.0, 6.0 + 5.0])

    destination = np.array([-7.92820323, 8.0, 18.66025404])

    return angle, origin_point, point, destination


@pytest.fixture
def point_to_rotate_and_new_point_quad3():
    angle = np.radians(30)
    origin_point = np.array([4.0, 5.0, -6.0])
    point = np.array([-4.0 - 8.660254037844387, 8.0, -6.0 - 5.0])

    destination = np.array([-7.92820323, 8.0, -18.66025404])

    return angle, origin_point, point, destination


@pytest.fixture
def point_to_rotate_and_new_point_quad4():
    angle = np.radians(30)
    origin_point = np.array([4.0, 5.0, -6.0])
    point = np.array([4.0 + 8.660254037844387, 8.0, -6.0 - 5.0])

    destination = np.array([14, 8.0, -6.0])

    return angle, origin_point, point, destination

