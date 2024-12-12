"""Top level API.

.. data:: __version__
    :type: str

    Version number as calculated by https://github.com/pypa/setuptools_scm
"""

from ._version import __version__
from .ppmac_macro_substitiution import generate

__all__ = ["__version__", "generate"]
