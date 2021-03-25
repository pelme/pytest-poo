import pytest


@pytest.fixture
def poo_testdir(testdir):
    testdir.tmpdir.join('test_poo.py').write('''
import pytest

@pytest.mark.poo
def test_success_with_poo():
    assert 1

@pytest.mark.poo
def test_fail_with_poo():
    assert 0


def test_success_without_poo():
    assert 1


def test_fail_without_poo():
    assert 0
''')

    return testdir


def test_verbose_mode_no_poo(poo_testdir):
    result = poo_testdir.runpytest('-v', '--strict-markers')

    result.stdout.fnmatch_lines(['*test_success_with_poo PASSED*'])
    result.stdout.fnmatch_lines(['*test_fail_with_poo FAILED*'])
    result.stdout.fnmatch_lines(['*test_success_without_poo PASSED*'])
    result.stdout.fnmatch_lines(['*test_fail_without_poo FAILED*'])


def test_verbose_mode_with_poo(poo_testdir):
    result = poo_testdir.runpytest('-v', '--poo', '--strict-markers')

    result.stdout.fnmatch_lines(['*test_success_with_poo PASSED (\U0001f4a9)*'])
    result.stdout.fnmatch_lines(['*test_fail_with_poo FAILED (\U0001f4a9)*'])
    result.stdout.fnmatch_lines(['*test_success_without_poo PASSED*'])
    result.stdout.fnmatch_lines(['*test_fail_without_poo FAILED*'])


def test_quiet_mode_no_poo(poo_testdir):
    result = poo_testdir.runpytest('-q', '--strict-markers')
    outcome_line = result.stdout.lines[0]

    assert outcome_line.count('.') == 2
    assert outcome_line.count('F') == 2


def test_quiet_mode_with_poo(poo_testdir, request):
    result = poo_testdir.runpytest('-q', '--poo', '--strict-markers')
    print(result.stdout)
    outcome_line = result.stdout.lines[0]

    assert outcome_line.count(u'.') == 1
    assert outcome_line.count(u'\U0001f4a9') == 1
    assert outcome_line.count(u'F') == 2
