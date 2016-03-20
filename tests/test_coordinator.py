import unittest
from unittest import TestCase
from Kinematics.kinematics import *
import numpy


class TestCoordinator(TestCase):
    def setUp(self):
        position = numpy.asarray([0,0,0])
        x = numpy.asarray([1,0,0])
        z = numpy.asarray([0,0,1])
        self._base = Coordinator(position, x, z)

    def test_move_along(self):
        x10 = self._base.move_along(10, self._base.x)
        z10 = self._base.move_along(10, self._base.z)
        self.assertListEqual(x10.position.tolist(), [10,0,0])
        self.assertEqual(z10.position.tolist(), [0,0,10])
        self.assertEqual(self._base.position.tolist(), [0,0,0])

if __name__ == '__main__':
    unittest.main()