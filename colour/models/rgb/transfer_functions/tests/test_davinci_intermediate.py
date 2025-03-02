"""
Define the unit tests for the :mod:`colour.models.rgb.transfer_functions.\
davinci_intermediate` module.
"""

import numpy as np
import unittest

from colour.models.rgb.transfer_functions import (
    oetf_DaVinciIntermediate,
    oetf_inverse_DaVinciIntermediate,
)
from colour.utilities import domain_range_scale, ignore_numpy_errors

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "TestOetf_DaVinciIntermediate",
    "TestOetf_inverse_DaVinciIntermediate",
]


class TestOetf_DaVinciIntermediate(unittest.TestCase):
    """
    Define :func:`colour.models.rgb.transfer_functions.davinci_intermediate.\
oetf_DaVinciIntermediate` definition unit tests methods.
    """

    def test_oetf_DaVinciIntermediate(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.\
davinci_intermediate.oetf_DaVinciIntermediate` definition.
        """

        self.assertAlmostEqual(
            oetf_DaVinciIntermediate(-0.01), -0.104442685500000, places=7
        )

        self.assertAlmostEqual(oetf_DaVinciIntermediate(0.0), 0.0, places=7)

        self.assertAlmostEqual(
            oetf_DaVinciIntermediate(0.18), 0.336043272384855, places=7
        )

        self.assertAlmostEqual(
            oetf_DaVinciIntermediate(1.0), 0.513837441116225, places=7
        )

        self.assertAlmostEqual(
            oetf_DaVinciIntermediate(100.0), 0.999999987016872, places=7
        )

    def test_n_dimensional_oetf_DaVinciIntermediate(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.\
davinci_intermediate.oetf_DaVinciIntermediate` definition n-dimensional arrays
        support.
        """

        L = 0.18
        V = oetf_DaVinciIntermediate(L)

        L = np.tile(L, 6)
        V = np.tile(V, 6)
        np.testing.assert_array_almost_equal(
            oetf_DaVinciIntermediate(L), V, decimal=7
        )

        L = np.reshape(L, (2, 3))
        V = np.reshape(V, (2, 3))
        np.testing.assert_array_almost_equal(
            oetf_DaVinciIntermediate(L), V, decimal=7
        )

        L = np.reshape(L, (2, 3, 1))
        V = np.reshape(V, (2, 3, 1))
        np.testing.assert_array_almost_equal(
            oetf_DaVinciIntermediate(L), V, decimal=7
        )

    def test_domain_range_scale_oetf_DaVinciIntermediate(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.\
davinci_intermediate.oetf_DaVinciIntermediate` definition domain and range
        scale support.
        """

        L = 0.18
        V = oetf_DaVinciIntermediate(L)

        d_r = (("reference", 1), ("1", 1), ("100", 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_array_almost_equal(
                    oetf_DaVinciIntermediate(L * factor), V * factor, decimal=7
                )

    @ignore_numpy_errors
    def test_nan_oetf_DaVinciIntermediate(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.\
davinci_intermediate.oetf_DaVinciIntermediate` definition nan support.
        """

        oetf_DaVinciIntermediate(
            np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan])
        )


class TestOetf_inverse_DaVinciIntermediate(unittest.TestCase):
    """
    Define :func:`colour.models.rgb.transfer_functions.\
davinci_intermediate.oetf_inverse_DaVinciIntermediate` definition unit tests
    methods.
    """

    def test_oetf_inverse_DaVinciIntermediate(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.\
davinci_intermediate.oetf_inverse_DaVinciIntermediate` definition.
        """

        self.assertAlmostEqual(
            oetf_inverse_DaVinciIntermediate(-0.104442685500000),
            -0.01,
            places=7,
        )

        self.assertAlmostEqual(
            oetf_inverse_DaVinciIntermediate(0.0), 0.0, places=7
        )

        self.assertAlmostEqual(
            oetf_inverse_DaVinciIntermediate(0.336043272384855), 0.18, places=7
        )

        self.assertAlmostEqual(
            oetf_inverse_DaVinciIntermediate(0.513837441116225), 1.0, places=7
        )

        self.assertAlmostEqual(
            oetf_inverse_DaVinciIntermediate(0.999999987016872),
            100.0,
            places=7,
        )

    def test_n_dimensional_oetf_inverse_DaVinciIntermediate(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.\
davinci_intermediate.oetf_inverse_DaVinciIntermediate` definition n-dimensional
        arrays support.
        """

        V = 0.336043272384855
        L = oetf_inverse_DaVinciIntermediate(V)

        V = np.tile(V, 6)
        L = np.tile(L, 6)
        np.testing.assert_array_almost_equal(
            oetf_inverse_DaVinciIntermediate(V), L, decimal=7
        )

        V = np.reshape(V, (2, 3))
        L = np.reshape(L, (2, 3))
        np.testing.assert_array_almost_equal(
            oetf_inverse_DaVinciIntermediate(V), L, decimal=7
        )

        V = np.reshape(V, (2, 3, 1))
        L = np.reshape(L, (2, 3, 1))
        np.testing.assert_array_almost_equal(
            oetf_inverse_DaVinciIntermediate(V), L, decimal=7
        )

    def test_domain_range_scale_oetf_inverse_DaVinciIntermediate(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.\
davinci_intermediate.oetf_inverse_DaVinciIntermediate` definition domain and
        range scale support.
        """

        V = 0.336043272384855
        L = oetf_inverse_DaVinciIntermediate(V)

        d_r = (("reference", 1), ("1", 1), ("100", 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_array_almost_equal(
                    oetf_inverse_DaVinciIntermediate(V * factor),
                    L * factor,
                    decimal=7,
                )

    @ignore_numpy_errors
    def test_nan_oetf_inverse_DaVinciIntermediate(self):
        """
        Test :func:`colour.models.rgb.transfer_functions.\
davinci_intermediate.oetf_inverse_DaVinciIntermediate` definition nan support.
        """

        oetf_inverse_DaVinciIntermediate(
            np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan])
        )


if __name__ == "__main__":
    unittest.main()
