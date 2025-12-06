import logging
import pytest
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts, soft_asserts

logger = logging.getLogger('test')

sa = SoftAsserts()
sa.set_logger(logger)

STEP_1 = 'step 1'
STEP_2 = 'step 2'


def __raise_value_error():
    raise ValueError('ValueError raised')


def __print_on_failure():
    print('Print message: Assertion failed!')


def test_assert_true():
    i = 1
    j = 2
    result = sa.assert_true(i + j == 3)
    logger.info(f'result: {result}')
    sa.assert_all()


def test_assert_true_fail():
    i = 1
    j = 2
    # logger.error() will print messages to console for each assert that fails
    result = sa.assert_true(i + j == 5)
    logger.info(f'result: {result}')
    result = sa.assert_equal(i, j, f'{i} is different from {j}')
    logger.info(f'result: {result}')
    sa.assert_all()


def test_assert_with_steps():
    sa.set_step(STEP_1)
    sa.assert_true(False)
    logger.info('print info')

    sa.set_step(STEP_2)
    sa.assert_true(False)

    # From this code section steps will not be attached to failure asserts
    sa.unset_step()
    sa.assert_true(False)

    sa.assert_all()


@pytest.mark.sa(soft_asserts=sa, skip_steps=[STEP_1])
def test_skip_if_step_1_fail():
    logger.info('print info')


@pytest.mark.sa(soft_asserts=sa, skip_steps=[STEP_2])
def test_skip_if_step_2_fail():
    logger.info('print info')


def test_assert_raises_with():
    with sa.assert_raised_with(TypeError):
        _ = sum([1, '2'])

    sa.assert_all()


def test_assert_raises_with_fail():
    with sa.assert_raised_with(ValueError):
        # sun will raise TypeError
        _ = sum([1, '2'])

    sa.assert_all()


def test_assert_raises():
    sa.assert_raises(ValueError, __raise_value_error)
    sa.assert_all()


def test_with_statement_1():
    with sa:
        sa.assert_true(False)
        sa.assert_equal(1, 2)


def test_with_statement_2():
    with SoftAsserts() as sa_1:
        sa_1.assert_true(False)
        sa_1.assert_equal(1, 2)


def test_assert_true_with_on_failure():
    sa.assert_true(False, on_failure=__print_on_failure)
    sa.assert_all()


@soft_asserts(sa=sa)
def test_with_decorator():
    sa.assert_true(False)
    sa.assert_equal(1, 2)
