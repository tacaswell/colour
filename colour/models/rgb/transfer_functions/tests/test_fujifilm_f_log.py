"""
Define the unit tests for the :mod:`colour.models.rgb.transfer_functions.\
fujifilm_f_log` module.
"""

import numpy as np
import unittest

from colour.models.rgb.transfer_functions import (
    log_encoding_FLog,
    log_decoding_FLog,
    log_encoding_FLog2,
    log_decoding_FLog2,
)
from colour.utilities import domain_range_scale, ignore_numpy_errors

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "TestLogEncoding_FLog",
    "TestLogDecoding_FLog",
    "TestLogEncoding_FLog2",
    "TestLogDecoding_FLog2",
]


class TestLogEncoding_FLog(unittest.TestCase):
    """
    Define :func:`colour.models.rgb.transfer_functions.fujifilm_f_log.\
log_encoding_FLog` definition unit tests methods.
    """

    def test_log_encoding_FLog(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_f_log.\
log_encoding_FLog` definition.
        """

        self.assertAlmostEqual(
            log_encoding_FLog(0.0), 0.092864000000000, places=7
        )

        self.assertAlmostEqual(
            log_encoding_FLog(0.18), 0.459318458661621, places=7
        )

        self.assertAlmostEqual(
            log_encoding_FLog(0.18, 12), 0.459318458661621, places=7
        )

        self.assertAlmostEqual(
            log_encoding_FLog(0.18, 10, False), 0.463336510514656, places=7
        )

        self.assertAlmostEqual(
            log_encoding_FLog(0.18, 10, False, False),
            0.446590337236003,
            places=7,
        )

        self.assertAlmostEqual(
            log_encoding_FLog(1.0), 0.704996409216428, places=7
        )

    def test_n_dimensional_log_encoding_FLog(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_f_log.\
log_encoding_FLog` definition n-dimensional arrays support.
        """

        L_in = 0.18
        V_out = log_encoding_FLog(L_in)

        L_in = np.tile(L_in, 6)
        V_out = np.tile(V_out, 6)
        np.testing.assert_array_almost_equal(
            log_encoding_FLog(L_in), V_out, decimal=7
        )

        L_in = np.reshape(L_in, (2, 3))
        V_out = np.reshape(V_out, (2, 3))
        np.testing.assert_array_almost_equal(
            log_encoding_FLog(L_in), V_out, decimal=7
        )

        L_in = np.reshape(L_in, (2, 3, 1))
        V_out = np.reshape(V_out, (2, 3, 1))
        np.testing.assert_array_almost_equal(
            log_encoding_FLog(L_in), V_out, decimal=7
        )

    def test_domain_range_scale_log_encoding_FLog(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_f_log.\
log_encoding_FLog` definition domain and range scale support.
        """

        L_in = 0.18
        V_out = log_encoding_FLog(L_in)

        d_r = (("reference", 1), ("1", 1), ("100", 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_array_almost_equal(
                    log_encoding_FLog(L_in * factor), V_out * factor, decimal=7
                )

    @ignore_numpy_errors
    def test_nan_log_encoding_FLog(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_f_log.\
log_encoding_FLog` definition nan support.
        """

        log_encoding_FLog(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestLogDecoding_FLog(unittest.TestCase):
    """
    Define :func:`colour.models.rgb.transfer_functions.fujifilm_f_log.\
log_decoding_FLog` definition unit tests methods.
    """

    def test_log_decoding_FLog(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_f_log.\
log_decoding_FLog` definition.
        """

        self.assertAlmostEqual(
            log_decoding_FLog(0.092864000000000), 0.0, places=7
        )

        self.assertAlmostEqual(
            log_decoding_FLog(0.459318458661621), 0.18, places=7
        )

        self.assertAlmostEqual(
            log_decoding_FLog(0.459318458661621, 12), 0.18, places=7
        )

        self.assertAlmostEqual(
            log_decoding_FLog(0.463336510514656, 10, False), 0.18, places=7
        )

        self.assertAlmostEqual(
            log_decoding_FLog(0.446590337236003, 10, False, False),
            0.18,
            places=7,
        )

        self.assertAlmostEqual(
            log_decoding_FLog(0.704996409216428), 1.0, places=7
        )

    def test_n_dimensional_log_decoding_FLog(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_f_log.\
log_decoding_FLog` definition n-dimensional arrays support.
        """

        V_out = 0.459318458661621
        L_in = log_decoding_FLog(V_out)

        V_out = np.tile(V_out, 6)
        L_in = np.tile(L_in, 6)
        np.testing.assert_array_almost_equal(
            log_decoding_FLog(V_out), L_in, decimal=7
        )

        V_out = np.reshape(V_out, (2, 3))
        L_in = np.reshape(L_in, (2, 3))
        np.testing.assert_array_almost_equal(
            log_decoding_FLog(V_out), L_in, decimal=7
        )

        V_out = np.reshape(V_out, (2, 3, 1))
        L_in = np.reshape(L_in, (2, 3, 1))
        np.testing.assert_array_almost_equal(
            log_decoding_FLog(V_out), L_in, decimal=7
        )

    def test_domain_range_scale_log_decoding_FLog(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_f_log.\
log_decoding_FLog` definition domain and range scale support.
        """

        V_out = 0.459318458661621
        L_in = log_decoding_FLog(V_out)

        d_r = (("reference", 1), ("1", 1), ("100", 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_array_almost_equal(
                    log_decoding_FLog(V_out * factor), L_in * factor, decimal=7
                )

    @ignore_numpy_errors
    def test_nan_log_decoding_FLog(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_f_log.\
log_decoding_FLog` definition nan support.
        """

        log_decoding_FLog(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestLogEncoding_FLog2(unittest.TestCase):
    """
    Define :func:`colour.models.rgb.transfer_functions.fujifilm_flog.\
log_encoding_FLog2` definition unit tests methods.
    """

    def test_log_encoding_FLog2(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_flog.\
log_encoding_FLog2` definition.
        """

        self.assertAlmostEqual(
            log_encoding_FLog2(0.0), 0.092864000000000, places=7
        )

        self.assertAlmostEqual(
            log_encoding_FLog2(0.18), 0.39100724189123, places=7
        )

        self.assertAlmostEqual(
            log_encoding_FLog2(0.18, 12), 0.39100724189123, places=7
        )

        self.assertAlmostEqual(
            log_encoding_FLog2(0.18, 10, False), 0.383562110108137, places=7
        )

        self.assertAlmostEqual(
            log_encoding_FLog2(0.18, 10, False, False),
            0.371293971820387,
            places=7,
        )

        self.assertAlmostEqual(
            log_encoding_FLog2(1.0), 0.568219370444443, places=7
        )

    def test_n_dimensional_log_encoding_FLog2(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_flog.\
log_encoding_FLog2` definition n-dimensional arrays support.
        """

        L_in = 0.18
        V_out = log_encoding_FLog2(L_in)

        L_in = np.tile(L_in, 6)
        V_out = np.tile(V_out, 6)
        np.testing.assert_almost_equal(
            log_encoding_FLog2(L_in), V_out, decimal=7
        )

        L_in = np.reshape(L_in, (2, 3))
        V_out = np.reshape(V_out, (2, 3))
        np.testing.assert_almost_equal(
            log_encoding_FLog2(L_in), V_out, decimal=7
        )

        L_in = np.reshape(L_in, (2, 3, 1))
        V_out = np.reshape(V_out, (2, 3, 1))
        np.testing.assert_almost_equal(
            log_encoding_FLog2(L_in), V_out, decimal=7
        )

    def test_domain_range_scale_log_encoding_FLog2(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_flog.\
log_encoding_FLog2` definition domain and range scale support.
        """

        L_in = 0.18
        V_out = log_encoding_FLog2(L_in)

        d_r = (("reference", 1), ("1", 1), ("100", 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    log_encoding_FLog2(L_in * factor),
                    V_out * factor,
                    decimal=7,
                )

    @ignore_numpy_errors
    def test_nan_log_encoding_FLog2(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_flog.\
log_encoding_FLog2` definition nan support.
        """

        log_encoding_FLog2(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestLogDecoding_FLog2(unittest.TestCase):
    """
    Define :func:`colour.models.rgb.transfer_functions.fujifilm_flog.\
log_decoding_FLog2` definition unit tests methods.
    """

    def test_log_decoding_FLog2(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_flog.\
log_decoding_FLog2` definition.
        """

        self.assertAlmostEqual(
            log_decoding_FLog2(0.092864000000000), 0.0, places=7
        )

        self.assertAlmostEqual(
            log_decoding_FLog2(0.391007241891230), 0.18, places=7
        )

        self.assertAlmostEqual(
            log_decoding_FLog2(0.391007241891230, 12), 0.18, places=7
        )

        self.assertAlmostEqual(
            log_decoding_FLog2(0.383562110108137, 10, False), 0.18, places=7
        )

        self.assertAlmostEqual(
            log_decoding_FLog2(0.371293971820387, 10, False, False),
            0.18,
            places=7,
        )

        self.assertAlmostEqual(
            log_decoding_FLog2(0.568219370444443), 1.0, places=7
        )

    def test_n_dimensional_log_decoding_FLog2(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_flog.\
log_decoding_FLog2` definition n-dimensional arrays support.
        """

        V_out = 0.39100724189123
        L_in = log_decoding_FLog2(V_out)

        V_out = np.tile(V_out, 6)
        L_in = np.tile(L_in, 6)
        np.testing.assert_almost_equal(
            log_decoding_FLog2(V_out), L_in, decimal=7
        )

        V_out = np.reshape(V_out, (2, 3))
        L_in = np.reshape(L_in, (2, 3))
        np.testing.assert_almost_equal(
            log_decoding_FLog2(V_out), L_in, decimal=7
        )

        V_out = np.reshape(V_out, (2, 3, 1))
        L_in = np.reshape(L_in, (2, 3, 1))
        np.testing.assert_almost_equal(
            log_decoding_FLog2(V_out), L_in, decimal=7
        )

    def test_domain_range_scale_log_decoding_FLog2(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_flog.\
log_decoding_FLog2` definition domain and range scale support.
        """

        V_out = 0.39100724189123
        L_in = log_decoding_FLog2(V_out)

        d_r = (("reference", 1), ("1", 1), ("100", 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    log_decoding_FLog2(V_out * factor),
                    L_in * factor,
                    decimal=7,
                )

    @ignore_numpy_errors
    def test_nan_log_decoding_FLog2(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.fujifilm_flog.\
log_decoding_FLog2` definition nan support.
        """

        log_decoding_FLog2(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


if __name__ == "__main__":
    unittest.main()
