"""
Spectral Generation
===================

Defines various objects performing spectral generation:

-   :func:`colour.sd_constant`
-   :func:`colour.sd_zeros`
-   :func:`colour.sd_ones`
-   :func:`colour.msds_constant`
-   :func:`colour.msds_zeros`
-   :func:`colour.msds_ones`
-   :func:`colour.colorimetry.sd_gaussian_normal`
-   :func:`colour.colorimetry.sd_gaussian_fwhm`
-   :attr:`colour.SD_GAUSSIAN_METHODS`
-   :func:`colour.sd_gaussian`
-   :func:`colour.colorimetry.sd_single_led_Ohno2005`
-   :attr:`colour.SD_SINGLE_LED_METHODS`
-   :func:`colour.sd_single_led`
-   :func:`colour.colorimetry.sd_multi_leds_Ohno2005`
-   :attr:`colour.SD_MULTI_LEDS_METHODS`
-   :func:`colour.sd_multi_leds`

References
----------
-   :cite:`Ohno2005` : Ohno, Yoshi. (2005). Spectral design considerations for
    white LED color rendering. Optical Engineering, 44(11), 111302.
    doi:10.1117/1.2130694
-   :cite:`Ohno2008a` : Ohno, Yoshiro, & Davis, W. (2008). NIST CQS simulation
    (Version 7.4) [Computer software].
    https://drive.google.com/file/d/1PsuU6QjUJjCX6tQyCud6ul2Tbs8rYWW9/view?\
usp=sharing
"""

from __future__ import annotations

import numpy as np

from colour.algebra.interpolation import LinearInterpolator
from colour.colorimetry import (
    SPECTRAL_SHAPE_DEFAULT,
    MultiSpectralDistributions,
    SpectralDistribution,
    SpectralShape,
)
from colour.hints import (
    Any,
    ArrayLike,
    Literal,
    NDArrayFloat,
    Sequence,
)
from colour.utilities import (
    CanonicalMapping,
    as_float_array,
    full,
    ones,
    validate_method,
)

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "sd_constant",
    "sd_zeros",
    "sd_ones",
    "msds_constant",
    "msds_zeros",
    "msds_ones",
    "sd_gaussian_normal",
    "sd_gaussian_fwhm",
    "SD_GAUSSIAN_METHODS",
    "sd_gaussian",
    "sd_single_led_Ohno2005",
    "SD_SINGLE_LED_METHODS",
    "sd_single_led",
    "sd_multi_leds_Ohno2005",
    "SD_MULTI_LEDS_METHODS",
    "sd_multi_leds",
]


def sd_constant(
    k: float, shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT, **kwargs: Any
) -> SpectralDistribution:
    """
    Return a spectral distribution of given spectral shape filled with
    constant :math:`k` values.

    Parameters
    ----------
    k
        Constant :math:`k` to fill the spectral distribution with.
    shape
        Spectral shape used to create the spectral distribution.

    Other Parameters
    ----------------
    kwargs
        {:class:`colour.SpectralDistribution`},
        See the documentation of the previously listed class.

    Returns
    -------
    :class:`colour.SpectralDistribution`
        Constant :math:`k` filled spectral distribution.

    Notes
    -----
    -   By default, the spectral distribution will use the shape given by
        :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.
    -   The interpolator is set to :class:`colour.LinearInterpolator` class.

    Examples
    --------
    >>> sd = sd_constant(100)
    >>> sd.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> sd[400]
    100.0
    """

    settings = {"name": f"{k} Constant", "interpolator": LinearInterpolator}
    settings.update(kwargs)

    values = full(len(shape.wavelengths), k)

    return SpectralDistribution(values, shape.wavelengths, **settings)


def sd_zeros(
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT, **kwargs: Any
) -> SpectralDistribution:
    """
    Return a spectral distribution of given spectral shape filled with zeros.

    Parameters
    ----------
    shape
        Spectral shape used to create the spectral distribution.

    Other Parameters
    ----------------
    kwargs
        {:func:`colour.sd_constant`},
        See the documentation of the previously listed definition.

    Returns
    -------
    :class:`colour.SpectralDistribution`
        Zeros filled spectral distribution.

    Notes
    -----
    -   By default, the spectral distribution will use the shape given by
        :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.
    -   The interpolator is set to :class:`colour.LinearInterpolator` class.

    Examples
    --------
    >>> sd = sd_zeros()
    >>> sd.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> sd[400]
    0.0
    """

    return sd_constant(0, shape, **kwargs)


def sd_ones(
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT, **kwargs: Any
) -> SpectralDistribution:
    """
    Return a spectral distribution of given spectral shape filled with ones.

    Parameters
    ----------
    shape
        Spectral shape used to create the spectral distribution.

    Other Parameters
    ----------------
    kwargs
        {:func:`colour.sd_constant`},
        See the documentation of the previously listed definition.

    Returns
    -------
    :class:`colour.SpectralDistribution`
        Ones filled spectral distribution.

    Notes
    -----
    -   By default, the spectral distribution will use the shape given by
        :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.
    -   The interpolator is set to :class:`colour.LinearInterpolator` class.

    Examples
    --------
    >>> sd = sd_ones()
    >>> sd.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> sd[400]
    1.0
    """

    return sd_constant(1, shape, **kwargs)


def msds_constant(
    k: float,
    labels: Sequence,
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT,
    **kwargs: Any,
) -> MultiSpectralDistributions:
    """
    Return the multi-spectral distributions with given labels and given
    spectral shape filled with constant :math:`k` values.

    Parameters
    ----------
    k
        Constant :math:`k` to fill the multi-spectral distributions with.
    labels
        Names to use for the :class:`colour.SpectralDistribution` class
        instances.
    shape
        Spectral shape used to create the multi-spectral distributions.

    Other Parameters
    ----------------
    kwargs
        {:class:`colour.MultiSpectralDistributions`},
        See the documentation of the previously listed class.

    Returns
    -------
    :class:`colour.MultiSpectralDistributions`
        Constant :math:`k` filled multi-spectral distributions.

    Notes
    -----
    -   By default, the multi-spectral distributions will use the shape given
        by :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.
    -   The interpolator is set to :class:`colour.LinearInterpolator` class.

    Examples
    --------
    >>> msds = msds_constant(100, labels=["a", "b", "c"])
    >>> msds.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> msds[400]
    array([ 100.,  100.,  100.])
    >>> msds.labels  # doctest: +SKIP
    ['a', 'b', 'c']
    """

    settings = {"name": f"{k} Constant", "interpolator": LinearInterpolator}
    settings.update(kwargs)

    wavelengths = shape.wavelengths
    values = full((len(wavelengths), len(labels)), k)

    return MultiSpectralDistributions(
        values, wavelengths, labels=labels, **settings
    )


def msds_zeros(
    labels: Sequence,
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT,
    **kwargs: Any,
) -> MultiSpectralDistributions:
    """
    Return the multi-spectral distributionss with given labels and given
    spectral shape filled with zeros.

    Parameters
    ----------
    labels
        Names to use for the :class:`colour.SpectralDistribution` class
        instances.
    shape
        Spectral shape used to create the multi-spectral distributions.

    Other Parameters
    ----------------
    kwargs
        {:func:`colour.msds_constant`},
        See the documentation of the previously listed definition.

    Returns
    -------
    :class:`colour.MultiSpectralDistributions`
        Zeros filled multi-spectral distributions.

    Notes
    -----
    -   By default, the multi-spectral distributions will use the shape given
        by :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.
    -   The interpolator is set to :class:`colour.LinearInterpolator` class.

    Examples
    --------
    >>> msds = msds_zeros(labels=["a", "b", "c"])
    >>> msds.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> msds[400]
    array([ 0.,  0.,  0.])
    >>> msds.labels  # doctest: +SKIP
    ['a', 'b', 'c']
    """

    return msds_constant(0, labels, shape, **kwargs)


def msds_ones(
    labels: Sequence,
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT,
    **kwargs: Any,
) -> MultiSpectralDistributions:
    """
    Return the multi-spectral distributionss with given labels and given
    spectral shape filled with ones.

    Parameters
    ----------
    labels
        Names to use for the :class:`colour.SpectralDistribution` class
        instances.
    shape
        Spectral shape used to create the multi-spectral distributions.

    Other Parameters
    ----------------
    kwargs
        {:func:`colour.msds_constant`},
        See the documentation of the previously listed definition.

    Returns
    -------
    :class:`colour.MultiSpectralDistributions`
        Ones filled multi-spectral distributions.

    Notes
    -----
    -   By default, the multi-spectral distributions will use the shape given
        by :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.
    -   The interpolator is set to :class:`colour.LinearInterpolator` class.

    Examples
    --------
    >>> msds = msds_ones(labels=["a", "b", "c"])
    >>> msds.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> msds[400]
    array([ 1.,  1.,  1.])
    >>> msds.labels  # doctest: +SKIP
    ['a', 'b', 'c']
    """

    return msds_constant(1, labels, shape, **kwargs)


def sd_gaussian_normal(
    mu: float,
    sigma: float,
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT,
    **kwargs: Any,
) -> SpectralDistribution:
    """
    Return a gaussian spectral distribution of given spectral shape at
    given mean wavelength :math:`\\mu` and standard deviation :math:`sigma`.

    Parameters
    ----------
    mu
        Mean wavelength :math:`\\mu` the gaussian spectral distribution will
        peak at.
    sigma
        Standard deviation :math:`sigma` of the gaussian spectral distribution.
    shape
        Spectral shape used to create the spectral distribution.

    Other Parameters
    ----------------
    kwargs
        {:class:`colour.SpectralDistribution`},
        See the documentation of the previously listed class.

    Returns
    -------
    :class:`colour.SpectralDistribution`
        Gaussian spectral distribution.

    Notes
    -----
    -   By default, the spectral distribution will use the shape given by
        :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.

    Examples
    --------
    >>> sd = sd_gaussian_normal(555, 25)
    >>> sd.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> sd[555]  # doctest: +SKIP
    1.0
    >>> sd[530]  # doctest: +ELLIPSIS
    0.6065306...
    """

    settings = {"name": f"{mu}nm - {sigma} Sigma - Gaussian"}
    settings.update(kwargs)

    values = np.exp(-((shape.wavelengths - mu) ** 2) / (2 * sigma**2))

    return SpectralDistribution(values, shape.wavelengths, **settings)


def sd_gaussian_fwhm(
    peak_wavelength: float,
    fwhm: float,
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT,
    **kwargs: Any,
) -> SpectralDistribution:
    """
    Return a gaussian spectral distribution of given spectral shape at given
    peak wavelength and full width at half maximum.

    Parameters
    ----------
    peak_wavelength
        Wavelength the gaussian spectral distribution will peak at.
    fwhm
        Full width at half maximum, i.e. width of the gaussian spectral
        distribution measured between those points on the *y* axis which are
        half the maximum amplitude.
    shape
        Spectral shape used to create the spectral distribution.

    Other Parameters
    ----------------
    kwargs
        {:class:`colour.SpectralDistribution`},
        See the documentation of the previously listed class.

    Returns
    -------
    :class:`colour.SpectralDistribution`
        Gaussian spectral distribution.

    Notes
    -----
    -   By default, the spectral distribution will use the shape given by
        :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.

    Examples
    --------
    >>> sd = sd_gaussian_fwhm(555, 25)
    >>> sd.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> sd[555]  # doctest: +SKIP
    1.0
    >>> sd[530]
    0.0625
    """

    settings = {"name": f"{peak_wavelength}nm - {fwhm} FWHM - Gaussian"}
    settings.update(kwargs)

    mu, sigma = peak_wavelength, fwhm / (2 * np.sqrt(2 * np.log(2)))
    values = np.exp(-((shape.wavelengths - mu) ** 2) / (2 * sigma**2))

    return SpectralDistribution(values, shape.wavelengths, **settings)


SD_GAUSSIAN_METHODS: CanonicalMapping = CanonicalMapping(
    {"Normal": sd_gaussian_normal, "FWHM": sd_gaussian_fwhm}
)
SD_GAUSSIAN_METHODS.__doc__ = """
Supported gaussian spectral distribution computation methods.
"""


def sd_gaussian(
    mu_peak_wavelength: float,
    sigma_fwhm: float,
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT,
    method: Literal["Normal", "FWHM"] | str = "Normal",
    **kwargs: Any,
) -> SpectralDistribution:
    """
    Return a gaussian spectral distribution of given spectral shape using
    given method.

    Parameters
    ----------
    mu_peak_wavelength
        Mean wavelength :math:`\\mu` the gaussian spectral distribution will
        peak at.
    sigma_fwhm
        Standard deviation :math:`sigma` of the gaussian spectral distribution
        or full width at half maximum, i.e. width of the gaussian spectral
        distribution measured between those points on the *y* axis which are
        half the maximum amplitude.
    shape
        Spectral shape used to create the spectral distribution.
    method
        Computation method.

    Other Parameters
    ----------------
    kwargs
        {:func:`colour.colorimetry.sd_gaussian_normal`,
        :func:`colour.colorimetry.sd_gaussian_fwhm`},
        See the documentation of the previously listed definitions.

    Returns
    -------
    :class:`colour.SpectralDistribution`
        Gaussian spectral distribution.

    Notes
    -----
    -   By default, the spectral distribution will use the shape given by
        :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.

    Examples
    --------
    >>> sd = sd_gaussian(555, 25)
    >>> sd.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> sd[555]  # doctest: +SKIP
    1.0
    >>> sd[530]  # doctest: +ELLIPSIS
    0.6065306...
    >>> sd = sd_gaussian(555, 25, method="FWHM")
    >>> sd.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> sd[555]  # doctest: +SKIP
    1.0
    >>> sd[530]
    0.0625
    """

    method = validate_method(method, tuple(SD_GAUSSIAN_METHODS))

    return SD_GAUSSIAN_METHODS[method](
        mu_peak_wavelength, sigma_fwhm, shape, **kwargs
    )


def sd_single_led_Ohno2005(
    peak_wavelength: float,
    half_spectral_width: float,
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT,
    **kwargs: Any,
) -> SpectralDistribution:
    """
    Return a single *LED* spectral distribution of given spectral shape at
    given peak wavelength and half spectral width :math:`\\Delta\\lambda_{0.5}`
    according to *Ohno (2005)* method.

    Parameters
    ----------
    peak_wavelength
        Wavelength the single *LED* spectral distribution will peak at.
    half_spectral_width
        Half spectral width :math:`\\Delta\\lambda_{0.5}`.
    shape
        Spectral shape used to create the spectral distribution.

    Other Parameters
    ----------------
    kwargs
        {:class:`colour.SpectralDistribution`},
        See the documentation of the previously listed class.

    Returns
    -------
    :class:`colour.SpectralDistribution`
        Single *LED* spectral distribution.

    Notes
    -----
    -   By default, the spectral distribution will use the shape given by
        :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.

    References
    ----------
    :cite:`Ohno2005`, :cite:`Ohno2008a`

    Examples
    --------
    >>> sd = sd_single_led_Ohno2005(555, 25)
    >>> sd.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> sd[555]  # doctest: +ELLIPSIS
    1...
    """

    settings = {
        "name": f"{peak_wavelength}nm - {half_spectral_width} "
        f"Half Spectral Width LED - Ohno (2005)"
    }
    settings.update(kwargs)

    values = np.exp(
        -(((shape.wavelengths - peak_wavelength) / half_spectral_width) ** 2)
    )
    values = (values + 2 * values**5) / 3

    return SpectralDistribution(values, shape.wavelengths, **settings)


SD_SINGLE_LED_METHODS: CanonicalMapping = CanonicalMapping(
    {
        "Ohno 2005": sd_single_led_Ohno2005,
    }
)
SD_SINGLE_LED_METHODS.__doc__ = """
Supported single *LED* spectral distribution computation methods.
"""


def sd_single_led(
    peak_wavelength: float,
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT,
    method: Literal["Ohno 2005"] | str = "Ohno 2005",
    **kwargs: Any,
) -> SpectralDistribution:
    """
    Return a single *LED* spectral distribution of given spectral shape at
    given peak wavelength according to given method.

    Parameters
    ----------
    peak_wavelength
        Wavelength the single *LED* spectral distribution will peak at.
    shape
        Spectral shape used to create the spectral distribution.
    method
        Computation method.

    Other Parameters
    ----------------
    kwargs
        {:func:`colour.colorimetry.sd_single_led_Ohno2005`},
        See the documentation of the previously listed definition.

    Returns
    -------
    :class:`colour.SpectralDistribution`
        Single *LED* spectral distribution.

    Notes
    -----
    -   By default, the spectral distribution will use the shape given by
        :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.

    References
    ----------
    :cite:`Ohno2005`, :cite:`Ohno2008a`

    Examples
    --------
    >>> sd = sd_single_led(555, half_spectral_width=25)
    >>> sd.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> sd[555]  # doctest: +ELLIPSIS
    1...
    """

    method = validate_method(method, tuple(SD_SINGLE_LED_METHODS))
    kwargs["shape"] = shape

    return SD_SINGLE_LED_METHODS[method](peak_wavelength, **kwargs)


def sd_multi_leds_Ohno2005(
    peak_wavelengths: ArrayLike,
    half_spectral_widths: ArrayLike,
    peak_power_ratios: ArrayLike | None = None,
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT,
    **kwargs: Any,
) -> SpectralDistribution:
    """
    Return a multi *LED* spectral distribution of given spectral shape at
    given peak wavelengths, half spectral widths :math:`\\Delta\\lambda_{0.5}`
    and peak power ratios according to *Ohno (2005)* method.

    The multi *LED* spectral distribution is generated using many single *LED*
    spectral distributions generated with :func:`colour.sd_single_led_Ohno2005`
    definition.

    Parameters
    ----------
    peak_wavelengths
        Wavelengths the multi *LED* spectral distribution will peak at, i.e.
        the peaks for each generated single *LED* spectral distributions.
    half_spectral_widths
        Half spectral widths :math:`\\Delta\\lambda_{0.5}`.
    peak_power_ratios
        Peak power ratios for each generated single *LED* spectral
        distributions.
    shape
        Spectral shape used to create the spectral distribution.

    Other Parameters
    ----------------
    kwargs
        {:func:`colour.colorimetry.sd_single_led_Ohno2005`},
        See the documentation of the previously listed definition.

    Returns
    -------
    :class:`colour.SpectralDistribution`
        Multi *LED* spectral distribution.

    Notes
    -----
    -   By default, the spectral distribution will use the shape given by
        :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.

    References
    ----------
    :cite:`Ohno2005`, :cite:`Ohno2008a`

    Examples
    --------
    >>> sd = sd_multi_leds_Ohno2005(
    ...     np.array([457, 530, 615]),
    ...     np.array([20, 30, 20]),
    ...     np.array([0.731, 1.000, 1.660]),
    ... )
    >>> sd.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> sd[500]  # doctest: +ELLIPSIS
    0.1295132...
    """

    peak_wavelengths = as_float_array(peak_wavelengths)
    half_spectral_widths = np.resize(
        half_spectral_widths, peak_wavelengths.shape
    )
    if peak_power_ratios is None:
        peak_power_ratios = ones(peak_wavelengths.shape)
    else:
        peak_power_ratios = np.resize(
            peak_power_ratios, peak_wavelengths.shape
        )

    sd = sd_zeros(shape)

    for peak_wavelength, half_spectral_width, peak_power_ratio in zip(
        peak_wavelengths, half_spectral_widths, peak_power_ratios
    ):
        sd += (
            sd_single_led_Ohno2005(
                peak_wavelength, half_spectral_width, **kwargs
            )
            * peak_power_ratio
        )

    def _format_array(a: NDArrayFloat) -> str:
        """Format given array :math:`a`."""

        return ", ".join([str(e) for e in a])

    sd.name = (
        f"{_format_array(peak_wavelengths)}nm - "
        f"{_format_array(half_spectral_widths)} FWHM - "
        f"{_format_array(peak_power_ratios)} Peak Power Ratios - "
        f"LED - Ohno (2005)"
    )

    return sd


SD_MULTI_LEDS_METHODS: CanonicalMapping = CanonicalMapping(
    {
        "Ohno 2005": sd_multi_leds_Ohno2005,
    }
)
SD_MULTI_LEDS_METHODS.__doc__ = """
Supported multi *LED* spectral distribution computation methods.
"""


def sd_multi_leds(
    peak_wavelengths: ArrayLike,
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT,
    method: Literal["Ohno 2005"] | str = "Ohno 2005",
    **kwargs: Any,
) -> SpectralDistribution:
    """
    Return a multi *LED* spectral distribution of given spectral shape at
    given peak wavelengths.

    Parameters
    ----------
    peak_wavelengths
        Wavelengths the multi *LED* spectral distribution will peak at, i.e.
        the peaks for each generated single *LED* spectral distributions.
    shape
        Spectral shape used to create the spectral distribution.
    method
        Computation method.

    Other Parameters
    ----------------
    kwargs
        {:func:`colour.colorimetry.sd_multi_leds_Ohno2005`},
        See the documentation of the previously listed definition.

    Returns
    -------
    :class:`colour.SpectralDistribution`
        Multi *LED* spectral distribution.

    Notes
    -----
    -   By default, the spectral distribution will use the shape given by
        :attr:`colour.SPECTRAL_SHAPE_DEFAULT` attribute.

    References
    ----------
    :cite:`Ohno2005`, :cite:`Ohno2008a`

    Examples
    --------
    >>> sd = sd_multi_leds(
    ...     np.array([457, 530, 615]),
    ...     half_spectral_widths=np.array([20, 30, 20]),
    ...     peak_power_ratios=np.array([0.731, 1.000, 1.660]),
    ... )
    >>> sd.shape
    SpectralShape(360.0, 780.0, 1.0)
    >>> sd[500]  # doctest: +ELLIPSIS
    0.1295132...
    """

    method = validate_method(method, tuple(SD_MULTI_LEDS_METHODS))
    kwargs["shape"] = shape

    return SD_MULTI_LEDS_METHODS[method](peak_wavelengths, **kwargs)
