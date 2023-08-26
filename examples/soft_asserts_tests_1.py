import logging
import pytest
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts


logger = logging.getLogger('test')

soft_asserts = SoftAsserts()
soft_asserts.set_logger(logger)

STEP_1 = 'step 1'
STEP_2 = 'step 2'


def __raise_value_error():
    raise ValueError('ValueError raised')


def test_01_assert_true():
    i = 1
    j = 2
    soft_asserts.assert_true(i + j == 3)
    logger.info('print info')
    soft_asserts.assert_all()


def test_02_assert_true_fail():
    i = 1
    j = 2
    # logger.error() will print messages to console for each assert that fails
    soft_asserts.assert_true(i + j == 5)
    soft_asserts.assert_equal(i, j, f'{i} is different from {j}')
    logger.info('print info')
    soft_asserts.assert_all()


def test_03_assert_with_steps():
    soft_asserts.set_step(STEP_1)
    soft_asserts.assert_true(False)
    logger.info('print info')

    soft_asserts.set_step(STEP_2)
    soft_asserts.assert_true(False)

    # From this code section steps will not be attached to failure asserts
    soft_asserts.unset_step()
    soft_asserts.assert_true(False)

    soft_asserts.assert_all()


@pytest.mark.soft_asserts(soft_asserts=soft_asserts, skip_steps=[STEP_1])
def test_04_skip_if_step_1_fail():
    logger.info('print info')


@pytest.mark.soft_asserts(soft_asserts=soft_asserts, skip_steps=[STEP_2])
def test_05_skip_if_step_2_fail():
    logger.info('print info')


def test_06_assert_raises_with():
    with soft_asserts.assert_raised_with(TypeError):
        _ = sum([1, '2'])

    soft_asserts.assert_all()


def test_06_assert_raises_with_fail():
    with soft_asserts.assert_raised_with(ValueError):
        # sun will raise TypeError
        _ = sum([1, '2'])

    soft_asserts.assert_all()


def test_07_assert_raises():
    soft_asserts.assert_raises(ValueError, __raise_value_error)
    soft_asserts.assert_all()
