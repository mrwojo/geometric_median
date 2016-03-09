import unittest
import numpy as np

from geometric_median import *


class TestBasic(unittest.TestCase):

    def test_list(self):
        """
        Accept Python list as input.
        """

        a = [(0, 0), (0, 0)]
        np.testing.assert_almost_equal([0, 0], geometric_median(a, method='minimize'))
        np.testing.assert_almost_equal([0, 0], geometric_median(a, method='weiszfeld'))

    def test_1point(self):
        a = [(5, 5)]
        np.testing.assert_almost_equal(a[0], geometric_median(a, method='minimize'))
        np.testing.assert_almost_equal(a[0], geometric_median(a, method='weiszfeld'))

    def test_require2d(self):
        """
        Accepting 1D input has too much error potential.
        1 row of N dims or N rows of 1?
        """
        a = [1, 2]
        with self.assertRaises(ValueError):
            np.testing.assert_almost_equal(a, geometric_median(a, method='minimize'))
        with self.assertRaises(ValueError):
            np.testing.assert_almost_equal(a, geometric_median(a, method='weiszfeld'))

    def test_1d(self):
        """
        Geometric median should be median in 1D.
        """

        a = np.array([[8, 6, 7, 5, 3, 0, 9]]).T

        np.testing.assert_almost_equal(np.median(a), geometric_median(a, method='minimize'))
        np.testing.assert_almost_equal(np.median(a), geometric_median(a, method='weiszfeld'))

    def test_collinear(self):
        """
        Similar to the 1D case.
        """
        a = np.array([8, 6, 7, 5, 3, 0, 9])

        median = np.median(a)
        expected = [median, median]

        a = np.array(zip(a, a))

        np.testing.assert_almost_equal(expected, geometric_median(a, method='minimize'))
        np.testing.assert_almost_equal(expected, geometric_median(a, method='weiszfeld'))


    def test_square(self):
        """
        Simple square, median point obviously in the middle.
        """

        a = np.array([(0, 0),
                      (1, 0),
                      (1, 1),
                      (0, 1)])

        np.testing.assert_almost_equal([0.5, 0.5], geometric_median(a, method='minimize'))
        np.testing.assert_almost_equal([0.5, 0.5], geometric_median(a, method='weiszfeld'))

    def _test_4coplanar(self):
        """
        From Wikipedia:
        If 1 of the 4 points is inside the triangle formed by the other 3
        points, then the geometric median is that point.

        This is failing.
        """

        a = [(0, 0),
             (1, 0),
             (1, 1)]

        # TODO: assert that b is inside a
        b = [0.90, 0.90]

        a = np.r_[a, [b]]

        np.testing.assert_almost_equal(b, geometric_median(a, method='minimize'))
        np.testing.assert_almost_equal(b, geometric_median(a, method='weiszfeld'))

    # Non-deterministic
    # Note that the methods really do not converge to precisely the same values.
    # def test_random(self):
    #     from scipy.spatial.distance import cdist
    #     def total_distance(x, y):
    #         return cdist([x], y).sum()

    #     for i in range(1, 10):
    #         a = np.random.random(size=(i, 2)) - 0.5
    #         m = geometric_median(a, method='minimize')
    #         w = geometric_median(a, method='weiszfeld')

    #         np.testing.assert_almost_equal(m, w, decimal=2, err_msg=str(a))

    #         # print "total distance minimize =", total_distance(m, a), "weiszfeld =", total_distance(w, a)
    #         # print "is minimize better?", total_distance(m, a) < total_distance(w, a)
