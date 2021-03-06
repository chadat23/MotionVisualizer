from unittest.mock import patch

import numpy as np


def test_rig_ctc_init(rig_ctc_inputs):
    from rig import Rig

    (rod_mount, lower_pivot,
     motor_angle, motor_torque, motor_rpm,
     ctc_length, ctc_rest_angle, ctc_total_rotation,
     drive) = rig_ctc_inputs

    motor2_point = np.copy(lower_pivot)
    motor2_point[2] *= -1

    rig = Rig(rod_mount, lower_pivot,
              motor_angle=motor_angle, motor_torque=motor_torque, motor_rpm=motor_rpm,
              ctc_length=ctc_length, ctc_neutral_angle=ctc_rest_angle, ctc_total_rotation=ctc_total_rotation,
              drive=drive)

    assert np.all(rig.lower_pivot1 == lower_pivot)
    assert np.all(rig.lower_pivot2 == motor2_point)
    assert rig.motor1_angle == np.radians(motor_angle)
    assert rig.motor2_angle == np.radians(-motor_angle)
    assert rig.ctc_neutral_angle == np.radians(ctc_rest_angle)
    assert rig.ctc_min_angle == np.radians(ctc_rest_angle) - np.radians(ctc_total_rotation) / 2
    assert rig.ctc_max_angle == np.radians(ctc_rest_angle) + np.radians(ctc_total_rotation) / 2
    assert rig.rod_mount_width == 2 * rod_mount[2]
    assert np.isclose(rig.rod_mount_length, 37.218946787892854)
    assert rig.ctc_length == ctc_length
    assert np.isclose(rig.pushrod_length, 42.22054573322952)
    assert rig.motor_torque == motor_torque
    assert rig.motor_rpm == motor_rpm


def test_rig_la_init(rig_la_inputs):
    from rig import Rig

    (rod_mount, lower_pivot,
     motor_torque, motor_rpm,
     travel, screw_pitch,
     drive) = rig_la_inputs

    motor2_point = np.copy(lower_pivot)
    motor2_point[2] *= -1

    rig = Rig(rod_mount, lower_pivot,
              motor_torque=motor_torque, motor_rpm=motor_rpm,
              linear_travel=travel, screw_pitch=screw_pitch,
              drive=drive)

    assert np.all(rig.lower_pivot1 == lower_pivot)
    assert np.all(rig.lower_pivot2 == motor2_point)
    assert rig.linear_travel == travel
    assert rig.screw_pitch == screw_pitch
    assert rig.rod_mount_width == 2 * rod_mount[2]
    assert np.isclose(rig.rod_mount_length, 37.218946787892854)
    assert np.isclose(rig.linear_travel, travel)
    assert np.isclose(rig.screw_pitch, screw_pitch)
    assert np.isclose(rig.travel_per_rad, screw_pitch / (2 * np.pi))
    assert rig.motor_torque == motor_torque
    assert rig.motor_rpm == motor_rpm


def test_calc_length_w_one_point(rig_ctc_w_I, point_w_length):
    point, length = point_w_length

    assert np.isclose(rig_ctc_w_I._calc_length(point), length)


def test_calc_length_w_two_points(rig_ctc_w_I, points_w_length):
    point1, point2, length = points_w_length

    assert np.isclose(rig_ctc_w_I._calc_length(point1, point2), length)


def test_calc_ctc_location(rig_ctc_w_I, ctc_location_info):
    point, motor_angle, ctc_angle, ctc_location = ctc_location_info

    actual = rig_ctc_w_I._calc_ctc_location(point, motor_angle, ctc_angle)

    assert np.all(np.isclose(actual, ctc_location))


def test_calc_ctc_location_2(rig_ctc_w_I, ctc_location_info):
    point, motor_angle, ctc_angle, ctc_location = ctc_location_info
    point[2] *= - 1
    ctc_location[2] *= - 1

    actual = rig_ctc_w_I._calc_ctc_location(point, -motor_angle, ctc_angle)

    assert np.all(np.isclose(actual, ctc_location))


def test_calc_rod_mount_locations_ctc(rig_ctc_w_I, ctc_angles_w_rod_mount_locations):
    ctc_angle1, ctc_angle2, expected_point1, expected_point2 = ctc_angles_w_rod_mount_locations

    rm = rig_ctc_w_I.rod_mount
    # points = rm[0], rm[0], rm[1], rm[1], rm[2], -rm[2]
    points = (np.array([rm[0], rm[1], rm[2]]), np.array([rm[0], rm[1], -rm[2]]))
    actual_point1, actual_point2 = rig_ctc_w_I._calc_rod_mount_points(ctc_angle1, ctc_angle2, points)

    assert np.all(np.isclose(expected_point1, actual_point1, atol=1e-3))
    assert np.all(np.isclose(expected_point2, actual_point2, atol=1e-3))


def test_calc_rod_mount_locations_la(rig_la_w_I, pushrod_lengths_w_mount_locations):
    pushrod1, pushrod2, rod_mount1, rod_mount2 = pushrod_lengths_w_mount_locations

    rm = rig_la_w_I.rod_mount
    # points = rm[0], rm[0], rm[1], rm[1], rm[2], -rm[2]
    points = (np.array([rm[0], rm[1], rm[2]]), np.array([rm[0], rm[1], -rm[2]]))
    actual_point1, actual_point2 = rig_la_w_I._calc_rod_mount_points(pushrod1, pushrod2, points)

    assert np.all(np.isclose(rod_mount1, actual_point1, atol=1e-3))
    assert np.all(np.isclose(rod_mount2, actual_point2, atol=1e-3))


def test_calc_pitch_and_roll(rig_ctc_w_I, rod_mounts_and_pitch_and_roll):
    rod_mount1, rod_mount2, pitch_and_roll = rod_mounts_and_pitch_and_roll
    assert np.all(np.isclose(rig_ctc_w_I._calc_pitch_and_roll(rod_mount1, rod_mount2), pitch_and_roll))


def test__get_starting_points(rig_ctc_w_I):
    points = np.array([23.77483606, 27.34514893, 8.5]), np.array([23.77483606, 27.34514893, -8.5])
    actual = rig_ctc_w_I._get_starting_points()

    assert np.all(np.isclose(points, actual))


def test__get_starting_points_2(rig_ctc_w_I_2):
    points = np.array([0.29781586, -0.03613470, 0.2]), np.array([0.29781586, -0.03613470, -0.2])
    actual = rig_ctc_w_I_2._get_starting_points()

    assert np.all(np.isclose(points, actual))


def test_numerical_derivative_2(rig_ctc_w_I_2):
    rig_ctc_w_I_2.delta = .01745
    a = rig_ctc_w_I_2._numerical_derivative(-0.043633231299858216 - .01745,
                                            0.04363323129985827 - .01745,
                                            -0.043633231299858216 + .01745,
                                            0.04363323129985827 + .01745,
                                            (np.array([0.3, -.002, 0.2]), np.array([0.3, -6e-11, -0.2])))

    assert np.isclose(a[0], 0.166, rtol=3)


def test_calc_performance_ctc(rig_ctc_w_I, performance_info_ctc):
    pitch, roll, pitch_torque, roll_torque, pitch_omega, roll_omega = performance_info_ctc

    rig_ctc_w_I._calc_performance()
    assert np.all(np.isclose(rig_ctc_w_I.pitch, pitch))
    assert np.all(np.isclose(rig_ctc_w_I.roll, roll))
    assert np.all(np.isclose(rig_ctc_w_I.pitch_torque, pitch_torque))
    assert np.all(np.isclose(rig_ctc_w_I.roll_torque, roll_torque))
    assert np.all(np.isclose(rig_ctc_w_I.pitch_omega, pitch_omega))
    assert np.all(np.isclose(rig_ctc_w_I.roll_omega, roll_omega))


def test_calc_performance_linear(rig_la_w_I, performance_info_linear):
    pitch, roll, pitch_torque, roll_torque, pitch_omega, roll_omega = performance_info_linear

    rig_la_w_I._calc_performance()
    assert np.all(np.isclose(rig_la_w_I.pitch, pitch))
    assert np.all(np.isclose(rig_la_w_I.roll, roll))
    assert np.all(np.isclose(rig_la_w_I.pitch_torque, pitch_torque))
    assert np.all(np.isclose(rig_la_w_I.roll_torque, roll_torque))
    assert np.all(np.isclose(rig_la_w_I.pitch_omega, pitch_omega))
    assert np.all(np.isclose(rig_la_w_I.roll_omega, roll_omega))
