from unittest.mock import patch

import numpy as np


# def test_rig_init(rig_inputs):
#     from rig import Rig
#
#     (rod_mount, motor_point,
#      motor_angle, motor_torque, motor_rpm,
#      ctc_length, ctc_rest_angle, ctc_total_rotation, current_angle,
#      z_I, x_I) = rig_inputs
#
#     motor2_point = np.copy(motor_point)
#     motor2_point[2] *= -1
#
#     rig = Rig(rod_mount, motor_point,
#               motor_angle, motor_torque, motor_rpm,
#               ctc_length, ctc_rest_angle, ctc_total_rotation, current_angle,
#               z_I, x_I)
#
#     assert np.all(rig.motor1_point == motor_point)
#     assert np.all(rig.motor2_point == motor2_point)
#     assert rig.motor1_angle == np.radians(motor_angle)
#     assert rig.motor2_angle == np.radians(-motor_angle)
#     assert rig.ctc_current_angle == np.radians(current_angle)
#     assert rig.ctc_rest_angle == np.radians(ctc_rest_angle)
#     assert rig.ctc_min_angle == np.radians(ctc_rest_angle) - np.radians(ctc_total_rotation) / 2
#     assert rig.ctc_max_angle == np.radians(ctc_rest_angle) + np.radians(ctc_total_rotation) / 2
#     assert rig.rod_mount_width == 2 * rod_mount[2]
#     assert np.isclose(rig.rod_mount_length, 626.4982043070834)
#     assert rig.ctc_length == ctc_length
#     assert np.isclose(rig.push_rod_length, 599.1575709741667)
#     assert rig.motor_torque == motor_torque
#     assert rig.motor_rpm == motor_rpm
#     assert rig.z_I == z_I
#     assert rig.x_I == x_I
#
#
# def test_calc_length_w_one_point(rig_w_I, point_w_length):
#     point, length = point_w_length
#
#     assert np.isclose(rig_w_I.calc_length(point), length)


def test_calc_length_w_two_points(rig_w_I, points_w_length):
    point1, point2, length = points_w_length

    print('length', rig_w_I.calc_length(point1, point2))
    assert False
    assert np.isclose(rig_w_I.calc_length(point1, point2), length)


# def test_calc_ctc_location(rig_w_I, ctc_location_info):
#     point, motor_angle, ctc_angle, ctc_location = ctc_location_info
#
#     actual = rig_w_I.calc_ctc_location(point, motor_angle, ctc_angle)
#
#     assert np.all(np.isclose(actual, ctc_location))
#
#
# def test_calc_ctc_location_2(rig_w_I, ctc_location_info):
#     point, motor_angle, ctc_angle, ctc_location = ctc_location_info
#     point[2] *= - 1
#     ctc_location[2] *= - 1
#
#     actual = rig_w_I.calc_ctc_location(point, -motor_angle, ctc_angle)
#
#     assert np.all(np.isclose(actual, ctc_location))
#
#
# def test_calc_rod_mount_locations(rig_w_I, ctc_angles_w_rod_mount_locations):
#     ctc_angle1, ctc_angle2, expected_point1, expected_point2 = ctc_angles_w_rod_mount_locations
#
#     actual_point1, actual_point2 = rig_w_I.calc_rod_mount_locations(ctc_angle1, ctc_angle2)
#
#     assert np.all(np.isclose(expected_point1, actual_point1, atol=1e-3))
#     assert np.all(np.isclose(expected_point2, actual_point2, atol=1e-3))
#
#
# def test_rotate_about_points_y_axis_quad1(rig_w_I, point_to_rotate_and_new_point_quad1):
#     angle, origin_point, point, destination = point_to_rotate_and_new_point_quad1
#
#     actual = rig_w_I.rotate_about_points_y_axis(angle, origin_point, point)
#
#     assert np.all(np.isclose(actual, destination))
#
#
# def test_rotate_about_points_y_axis_quad2(rig_w_I, point_to_rotate_and_new_point_quad2):
#     angle, origin_point, point, destination = point_to_rotate_and_new_point_quad2
#
#     actual = rig_w_I.rotate_about_points_y_axis(angle, origin_point, point)
#
#     assert np.all(np.isclose(actual, destination))
#
#
# def test_rotate_about_points_y_axis_quad3(rig_w_I, point_to_rotate_and_new_point_quad3):
#     angle, origin_point, point, destination = point_to_rotate_and_new_point_quad3
#
#     actual = rig_w_I.rotate_about_points_y_axis(angle, origin_point, point)
#
#     assert np.all(np.isclose(actual, destination))
#
#
# def test_rotate_about_points_y_axis_quad4(rig_w_I, point_to_rotate_and_new_point_quad4):
#     angle, origin_point, point, destination = point_to_rotate_and_new_point_quad4
#
#     actual = rig_w_I.rotate_about_points_y_axis(angle, origin_point, point)
#
#     assert np.all(np.isclose(actual, destination))
#
#
# def test_calc_torques(rig_w_I):
#     # from rig import Rig
#     # # rig = Rig(np.array([23, 28, 8.5]), np.array([45.5, -8, 13]), 10, 40 * 12, 160, 2.5, 45, 60, 45)
#     # # rig = Rig(np.array([20, 10, 5]), np.array([17.5, 0, 5]), 0, 40 * 12, 160, 2.5, 0, 60, 45)
#     # rig = Rig(np.array([20, 10, 5]), np.array([0, 0, 5]), 0, 40 * 12, 160, 20, 0, 60, 45)
#     # # rig = Rig(np.array([200, 100, 10]), np.array([190, 0, 10]), 0, 50, 160, 10, 0, 60, 45)
#     # ctc1_point = rig.calc_ctc_location(rig.motor1_point, rig.motor1_angle, rig.ctc_rest_angle)
#     # ctc2_point = rig.calc_ctc_location(rig.motor2_point, rig.motor2_angle, rig.ctc_rest_angle)
#     #
#     # rig.calc_force(rig.ctc_rest_angle, rig.ctc_rest_angle, ctc1_point, ctc2_point)
#
#     pitch, roll = rig_w_I.calc_torques(rig_w_I.ctc_rest_angle, rig_w_I.ctc_rest_angle)
#
#     assert np.isclose(pitch, 414425.53073028754)
#     assert np.isclose(roll, 0)
#
#
# def test_calc_pitch_roll_rates(rig_w_I):
#     pitch, roll = rig_w_I.calc_pitch_roll_rates(rig_w_I.ctc_rest_angle, rig_w_I.ctc_rest_angle)
#
#     assert np.isclose(pitch, 14.145303233346462)
#     assert np.isclose(roll, 28.366819108667446)
