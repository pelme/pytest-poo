pytest-poo is a plugin for `pytest <http://pytest.org/>`_ that points out your
crappy tests with piles of poo.

Really? Why?
============
I showed the --poo option at EuroPython 2013. A number of people thought I
should release it, so here it is.

Screenshots
==============

This is what the output usually looks like:

.. image:: https://github.com/pelme/pytest-poo/raw/master/screenshots/normal.png
    :width: 722px
    :alt: Normal mode, without poo
    :align: center
    :target: https://github.com/pelme/pytest-poo/raw/master/screenshots/normal.png

... when passing --poo, this is what is outputted instead:

.. image:: https://github.com/pelme/pytest-poo/raw/master/screenshots/poo.png
    :width: 722px
    :alt: Poo mode!
    :align: center
    :target: https://github.com/pelme/pytest-poo/raw/master/screenshots/poo.png


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
function:

.. code-block:: python

    import pytest

    @pytest.mark.poo
    def test_something():
        assert 0


or for classes:

.. code-block:: python

    import pytest

    class MyTests(object):
        pytestmark = [pytest.mark.poo]


... or for entire modules:

.. code-block:: python

    import pytest

    pytestmark = pytest.mark.poo


    def test_a():
        assert 0


    def test_b():
        assert 0


Showing crappy tests during test run
------------------------------------

Just run py.test with the ``--poo`` option to enable the output. To always
enable, add ``--poo`` to addopts in pytest.ini:

.. code-block:: ini

    [pytest]
    addopts = --poo


