import pytest

PILE_OF_POO = u"\U0001F4A9 "


def pytest_addoption(parser):
    group = parser.getgroup('Poo', 'Poo')
    group._addoption('--poo',
                     action="store_true", dest="poo", default=False,
                     help="Show crappy tests.")


def pytest_report_teststatus(report):
    if (not pytest.config.option.poo) or ('poo' not in report.keywords) or (report.when != 'call'):
        return

    if (pytest.config.option.verbose == -1 and report.passed) or pytest.config.option.verbose >= 0:
        return (report.outcome, PILE_OF_POO, '%s (%s)' % (report.outcome.upper(), PILE_OF_POO))


def pytest_configure(config):
    config.addinivalue_line(
        'markers',
        'poo: Mark the test as crappy. When using --poo, pile of poo '
        'will be shown with the test outcome.')
