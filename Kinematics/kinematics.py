import numpy
import copy


class Coordinator:
    def __init__(self, position, x_direction, z_direction):
        """

        :type position: numpy.array
        """
        self._position = position
        self._x = x_direction
        self._z = z_direction

    def move_along(self, distance, direction):
        new_coordinator = self.clone()
        new_coordinator._position += direction * distance
        return new_coordinator

    def clone(self):
        return copy.deepcopy(self)

    @property
    def position(self):
        return self._position

    @property
    def x(self):
        return self._x

    @property
    def z(self):
        return self._z

class Link:
    def __init__(self, a, alpha, d, sigma):
        self._a = a
        self._alpha = alpha
        self._d = d
        self._sigma = sigma

    def transform(self, coordinator):
        self

class Robot:
    def __init__(self):
        pass

    def set_dh_matrix_parameters(self, dh):
        self._dh = dh
        pass
