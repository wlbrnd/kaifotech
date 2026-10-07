from dataclasses import dataclass, field
import numpy as np


@dataclass
class DroneState:
    position: np.ndarray = field(
        default_factory=lambda: np.array([0.0, 1.0, 0.0], dtype=float)
    )

    velocity: np.ndarray = field(
        default_factory=lambda: np.zeros(3, dtype=float)
    )

    acceleration: np.ndarray = field(
        default_factory=lambda: np.zeros(3, dtype=float)
    )

    orientation: np.ndarray = field(
        default_factory=lambda: np.zeros(3, dtype=float)
    )
    # roll, pitch, yaw

    angular_velocity: np.ndarray = field(
        default_factory=lambda: np.zeros(3, dtype=float)
    )

    motor_throttles: np.ndarray = field(
        default_factory=lambda: np.zeros(4, dtype=float)
    )

    airborne: bool = False

    crashed: bool = False

    simulation_time: float = 0.0


@dataclass
class ForceSnapshot:
    gravity: np.ndarray = field(
        default_factory=lambda: np.zeros(3, dtype=float)
    )

    thrust: np.ndarray = field(
        default_factory=lambda: np.zeros(3, dtype=float)
    )

    drag: np.ndarray = field(
        default_factory=lambda: np.zeros(3, dtype=float)
    )

    wind_effect: np.ndarray = field(
        default_factory=lambda: np.zeros(3, dtype=float)
    )

    total: np.ndarray = field(
        default_factory=lambda: np.zeros(3, dtype=float)
    )

    torque: np.ndarray = field(
        default_factory=lambda: np.zeros(3, dtype=float)
    )
    