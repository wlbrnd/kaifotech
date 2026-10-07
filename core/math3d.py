import math
import numpy as np


def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))


def clamp01(value):
    return clamp(value, 0.0, 1.0)


def normalize(v):
    v = np.asarray(v, dtype=float)

    norm = np.linalg.norm(v)

    if norm < 1e-8:
        return np.zeros_like(v)

    return v / norm


def rotation_matrix(roll, pitch, yaw):
    """
    Body -> World rotation matrix.

    Coordinate system:
        X = right
        Y = up
        Z = forward
    """

    cr = math.cos(roll)
    sr = math.sin(roll)

    cp = math.cos(pitch)
    sp = math.sin(pitch)

    cy = math.cos(yaw)
    sy = math.sin(yaw)

    rx = np.array([
        [1, 0, 0],
        [0, cr, -sr],
        [0, sr, cr],
    ], dtype=float)

    ry = np.array([
        [cp, 0, sp],
        [0, 1, 0],
        [-sp, 0, cp],
    ], dtype=float)

    rz = np.array([
        [cy, -sy, 0],
        [sy, cy, 0],
        [0, 0, 1],
    ], dtype=float)

    return rz @ ry @ rx


def world_to_body(vector, roll, pitch, yaw):
    r = rotation_matrix(roll, pitch, yaw)
    return r.T @ vector


def body_to_world(vector, roll, pitch, yaw):
    r = rotation_matrix(roll, pitch, yaw)
    return r @ vector


def radians_to_degrees(value):
    return math.degrees(value)


def degrees_to_radians(value):
    return math.radians(value)


def wrap_angle(angle):
    while angle > math.pi:
        angle -= 2 * math.pi

    while angle < -math.pi:
        angle += 2 * math.pi

    return angle


def vec_length(vector):
    return float(np.linalg.norm(vector))
