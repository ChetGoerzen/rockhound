# pylint: disable=missing-docstring
# Import functions/classes to make the public API
from . import version
from .registry import data_location
from .etopo1 import fetch_etopo1
from .earth_models import fetch_prem
from .earth_models import fetch_ak135f
from .earth_models import fetch_iasp91
from .earth_models import fetch_mean
from .earth_models import fetch_pema
from .earth_models import fetch_pemc
from .earth_models import fetch_pemo
from .earth_models import fetch_mc35
from .earth_models import fetch_stw105
from .earth_models import fetch_tna_sna
from .bedmap2 import fetch_bedmap2
from .seafloor import fetch_seafloor_age

# from .iasp91 import fetch_iasp91
# from .ak135f import fetch_ak135f


# Get the version number through versioneer
__version__ = version.full_version


def test(doctest=True, verbose=True, coverage=False, figures=False):
    """
    Run the test suite.

    Uses `py.test <http://pytest.org/>`__ to discover and run the tests.

    Parameters
    ----------

    doctest : bool
        If ``True``, will run the doctests as well (code examples that start
        with a ``>>>`` in the docs).
    verbose : bool
        If ``True``, will print extra information during the test run.
    coverage : bool
        If ``True``, will run test coverage analysis on the code as well.
        Requires ``pytest-cov``.
    figures : bool
        If ``True``, will test generated figures against saved baseline
        figures.  Requires ``pytest-mpl`` and ``matplotlib``.

    Raises
    ------

    AssertionError
        If pytest returns a non-zero error code indicating that some tests have
        failed.

    """
    import pytest

    package = __name__
    args = []
    if verbose:
        args.append("-vv")
    if coverage:
        args.append("--cov={}".format(package))
        args.append("--cov-report=term-missing")
    if doctest:
        args.append("--doctest-modules")
    if figures:
        args.append("--mpl")
    args.append("--pyargs")
    args.append(package)
    status = pytest.main(args)
    assert status == 0, "Some tests have failed."
