"""
Extrapolation
=============

Defines the classes for extrapolating variables:

-   :class:`colour.Extrapolator`: 1-D function extrapolation.

References
----------
-   :cite:`Sastanina` : sastanin. (n.d.). How to make scipy.interpolate give an
    extrapolated result beyond the input range? Retrieved August 8, 2014, from
    http://stackoverflow.com/a/2745496/931625
-   :cite:`Westland2012i` : Westland, S., Ripamonti, C., & Cheung, V. (2012).
    Extrapolation Methods. In Computational Colour Science Using MATLAB (2nd
    ed., p. 38). ISBN:978-0-470-66569-5
"""

from __future__ import annotations

import numpy as np

from colour.algebra import NullInterpolator, sdiv, sdiv_mode
from colour.constants import DEFAULT_FLOAT_DTYPE
from colour.hints import (
    Any,
    ArrayLike,
    DTypeReal,
    Literal,
    NDArrayFloat,
    ProtocolInterpolator,
    Real,
    Type,
)
from colour.utilities import (
    as_float_array,
    as_float,
    attest,
    is_numeric,
    is_string,
    optional,
    validate_method,
)

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "Extrapolator",
]


class Extrapolator:
    """
    Extrapolate the 1-D function of given interpolator.

    The :class:`colour.Extrapolator` class acts as a wrapper around a given
    *Colour* or *scipy* interpolator class instance with compatible signature.
    Two extrapolation methods are available:

    -   *Linear*: Linearly extrapolates given points using the slope defined by
        the interpolator boundaries (xi[0], xi[1]) if x < xi[0] and
        (xi[-1], xi[-2]) if x > xi[-1].
    -   *Constant*: Extrapolates given points by assigning the interpolator
        boundaries values xi[0] if x < xi[0] and xi[-1] if x > xi[-1].

    Specifying the *left* and *right* arguments takes precedence on the chosen
    extrapolation method and will assign the respective *left* and *right*
    values to the given points.

    Parameters
    ----------
    interpolator
        Interpolator object.
    method
        Extrapolation method.
    left
        Value to return for x < xi[0].
    right
        Value to return for x > xi[-1].
    dtype
        Data type used for internal conversions.

    Methods
    -------
    -   :meth:`~colour.Extrapolator.__init__`
    -   :meth:`~colour.Extrapolator.__class__`

    Notes
    -----
    -   The interpolator must define ``x`` and ``y`` properties.

    References
    ----------
    :cite:`Sastanina`, :cite:`Westland2012i`

    Examples
    --------
    Extrapolating a single numeric variable:

    >>> from colour.algebra import LinearInterpolator
    >>> x = np.array([3, 4, 5])
    >>> y = np.array([1, 2, 3])
    >>> interpolator = LinearInterpolator(x, y)
    >>> extrapolator = Extrapolator(interpolator)
    >>> extrapolator(1)
    -1.0

    Extrapolating an `ArrayLike` variable:

    >>> extrapolator(np.array([6, 7, 8]))
    array([ 4.,  5.,  6.])

    Using the *Constant* extrapolation method:

    >>> x = np.array([3, 4, 5])
    >>> y = np.array([1, 2, 3])
    >>> interpolator = LinearInterpolator(x, y)
    >>> extrapolator = Extrapolator(interpolator, method="Constant")
    >>> extrapolator(np.array([0.1, 0.2, 8, 9]))
    array([ 1.,  1.,  3.,  3.])

    Using defined *left* boundary and *Constant* extrapolation method:

    >>> x = np.array([3, 4, 5])
    >>> y = np.array([1, 2, 3])
    >>> interpolator = LinearInterpolator(x, y)
    >>> extrapolator = Extrapolator(interpolator, method="Constant", left=0)
    >>> extrapolator(np.array([0.1, 0.2, 8, 9]))
    array([ 0.,  0.,  3.,  3.])
    """

    def __init__(
        self,
        interpolator: ProtocolInterpolator | None = None,
        method: Literal["Linear", "Constant"] | str = "Linear",
        left: Real | None = None,
        right: Real | None = None,
        dtype: Type[DTypeReal] | None = None,
        *args: Any,  # noqa: ARG002
        **kwargs: Any,  # noqa: ARG002
    ) -> None:
        dtype = optional(dtype, DEFAULT_FLOAT_DTYPE)

        self._interpolator: ProtocolInterpolator = NullInterpolator(
            np.array([-np.inf, np.inf]), np.array([-np.inf, np.inf])
        )
        self.interpolator = optional(interpolator, self._interpolator)
        self._method: Literal["Linear", "Constant"] | str = "Linear"
        self.method = optional(method, self._method)
        self._right: Real | None = None
        self.right = right
        self._left: Real | None = None
        self.left = left

        self._dtype: Type[DTypeReal] = dtype

    @property
    def interpolator(self) -> ProtocolInterpolator:
        """
        Getter and setter property for the *Colour* or *scipy* interpolator
        class instance.

        Parameters
        ----------
        value
            Value to set the *Colour* or *scipy* interpolator class instance
            with.

        Returns
        -------
        ProtocolInterpolator
            *Colour* or *scipy* interpolator class instance.
        """

        return self._interpolator

    @interpolator.setter
    def interpolator(self, value: ProtocolInterpolator):
        """Setter for the **self.interpolator** property."""

        attest(
            hasattr(value, "x"),
            f'"{value}" interpolator has no "x" attribute!',
        )

        attest(
            hasattr(value, "y"),
            f'"{value}" interpolator has no "y" attribute!',
        )

        self._interpolator = value

    @property
    def method(self) -> Literal["Linear", "Constant"] | str:
        """
        Getter and setter property for the extrapolation method.

        Parameters
        ----------
        value
            Value to set the extrapolation method. with.

        Returns
        -------
        :class:`str`
            Extrapolation method.
        """

        return self._method

    @method.setter
    def method(self, value: Literal["Linear", "Constant"] | str):
        """Setter for the **self.method** property."""

        attest(
            is_string(value),
            f'"method" property: "{value}" type is not "str"!',
        )

        value = validate_method(value, ("Linear", "Constant"))

        self._method = value

    @property
    def left(self) -> Real | None:
        """
        Getter and setter property for left value to return for x < xi[0].

        Parameters
        ----------
        value
            Left value to return for x < xi[0].

        Returns
        -------
        :py:data:`None` or Real
            Left value to return for x < xi[0].
        """

        return self._left

    @left.setter
    def left(self, value: Real | None):
        """Setter for the **self.left** property."""

        if value is not None:
            attest(
                is_numeric(value),
                f'"left" property: "{value}" is not a "number"!',
            )

            self._left = value

    @property
    def right(self) -> Real | None:
        """
        Getter and setter property for right value to return for x > xi[-1].

        Parameters
        ----------
        value
            Right value to return for x > xi[-1].

        Returns
        -------
        :py:data:`None` or Real
            Right value to return for x > xi[-1].
        """

        return self._right

    @right.setter
    def right(self, value: Real | None):
        """Setter for the **self.right** property."""

        if value is not None:
            attest(
                is_numeric(value),
                f'"right" property: "{value}" is not a "number"!',
            )

            self._right = value

    def __call__(self, x: ArrayLike) -> NDArrayFloat:
        """
        Evaluate the Extrapolator at given point(s).

        Parameters
        ----------
        x
            Point(s) to evaluate the Extrapolator at.

        Returns
        -------
        :class:`numpy.ndarray`
            Extrapolated points value(s).
        """

        x = as_float_array(x)

        xe = self._evaluate(x)

        return as_float(xe)

    def _evaluate(self, x: NDArrayFloat) -> NDArrayFloat:
        """
        Perform the extrapolating evaluation at given points.

        Parameters
        ----------
        x
            Points to evaluate the Extrapolator at.

        Returns
        -------
        :class:`numpy.ndarray`
            Extrapolated points values.
        """

        xi = self._interpolator.x
        yi = self._interpolator.y

        y = np.empty_like(x)

        if self._method == "linear":
            with sdiv_mode():
                y[x < xi[0]] = yi[0] + (x[x < xi[0]] - xi[0]) * sdiv(
                    yi[1] - yi[0], xi[1] - xi[0]
                )
                y[x > xi[-1]] = yi[-1] + (x[x > xi[-1]] - xi[-1]) * sdiv(
                    yi[-1] - yi[-2], xi[-1] - xi[-2]
                )
        elif self._method == "constant":
            y[x < xi[0]] = yi[0]
            y[x > xi[-1]] = yi[-1]

        if self._left is not None:
            y[x < xi[0]] = self._left
        if self._right is not None:
            y[x > xi[-1]] = self._right

        in_range = np.logical_and(x >= xi[0], x <= xi[-1])
        y[in_range] = self._interpolator(x[in_range])

        return y
