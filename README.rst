pytest-poo is a plugin for `pytest <http://pytest.org/>`_ that points out your
crappy tests with piles of poo.

Really? Why?
============
I showed the --poo option at EuroPython 2013. A number of people thought I
should release it, so here it is.

Example output
==============

Requirements
============
A recent version of pytest is required (>= 2.3.4).

Quick start
===========
1. ``pip install pytest-poo``
2. Mark tests with the ``pytest.mark.poo`` marker.
3. Run tests with the --poo option to enable pile of poo output.

Documentation
==============

Marking tests
--------------------
Add the ``pytest.mark.poo`` marker to the tests that you consider crappy. The
markers are standard py.test markers and can be used like this on a test
function::

    import pytest

    @pytest.mark.poo
    def test_something():
        assert 0


or for classes::

    import pytest

    class MyTests(object):
        pytestmark = [pytest.mark.poo]


... or for entire modules::

    import pytest

    pytestmark = pytest.mark.poo


    def test_a():
        assert 0


    def test_b():
        assert 0


Showing crappy tests during test run
------------------------------------

Just run py.test with the ``--poo`` option to enable the output. To always
enable, add ``--poo`` to addopts in pytest.ini::

    [pytest]
    addopts = --poo


