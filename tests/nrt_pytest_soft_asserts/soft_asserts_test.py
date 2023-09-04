import logging

import pytest

from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts

ERROR_MESSAGE_1 = 'error message 1'

STEP_1 = 'step 1'
STEP_2 = 'step 2'
STEP_3 = 'step 3'

STEPS = [STEP_2, STEP_3]

soft_asserts = SoftAsserts()

print_message = ''


@pytest.fixture
def before_test():
    SoftAsserts.unset_logger()
    SoftAsserts.unset_print_method()
    # If it fails, then Missing assert_all in tests
    soft_asserts.assert_all()
    soft_asserts.init_failure_steps()


def test_assert_true(before_test):
    # Soft Asserts return True if assertion passes, False if assertion fails.
    assert soft_asserts.assert_true(True)
    assert soft_asserts.assert_true(True, ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_false(before_test):
    assert soft_asserts.assert_false(False)
    assert soft_asserts.assert_false(False, ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_equal(before_test):
    assert soft_asserts.assert_equal(1, 1)
    assert soft_asserts.assert_equal('1', '1', ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_not_equal(before_test):
    assert soft_asserts.assert_not_equal(1, 2)
    assert soft_asserts.assert_not_equal('1', '2', ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_is(before_test):
    assert soft_asserts.assert_is(1, 1)
    assert soft_asserts.assert_is('1', '1', ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_is_not(before_test):
    assert soft_asserts.assert_is_not(1, 2)
    assert soft_asserts.assert_is_not('1', '2', ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_is_none(before_test):
    assert soft_asserts.assert_is_none(None)
    assert soft_asserts.assert_is_none(None, ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_is_not_none(before_test):
    assert soft_asserts.assert_is_not_none(1)
    assert soft_asserts.assert_is_not_none(1, ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_in(before_test):
    assert soft_asserts.assert_in(1, [1, 2, 3])
    assert soft_asserts.assert_in('1', ['1', '2', '3'], ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_not_in(before_test):
    assert soft_asserts.assert_not_in(1, [2, 3, 4])
    assert soft_asserts.assert_not_in('1', ['2', '3', '4'], ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_is_instance(before_test):
    assert soft_asserts.assert_is_instance(1, int)
    assert soft_asserts.assert_is_instance('1', str, ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_not_is_instance(before_test):
    assert soft_asserts.assert_not_is_instance(1, str)
    assert soft_asserts.assert_not_is_instance('1', int, ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_almost_equal(before_test):
    assert soft_asserts.assert_almost_equal(1.0001, 1.0002, 0.002)
    soft_asserts.assert_all()


def test_assert_not_almost_equal(before_test):
    assert soft_asserts.assert_not_almost_equal(1.0001, 1.0002, 0.000001)
    soft_asserts.assert_all()


def test_assert_raises(before_test):
    assert soft_asserts.assert_raises(ValueError, __raise_value_error)
    assert soft_asserts.assert_raises(ValueError, __raise_value_error, ERROR_MESSAGE_1)
    soft_asserts.assert_all()


def test_assert_raised_with(before_test):
    with soft_asserts.assert_raised_with(ValueError):
        raise ValueError(ERROR_MESSAGE_1)

    soft_asserts.assert_all()


def test_assert_true_fail(before_test):
    assert not soft_asserts.assert_true(False)
    assert soft_asserts.assert_true(True)
    assert not soft_asserts.assert_true(False, ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 2
    __verify_assert_all_raised_exception()


def test_assert_false_fail(before_test):
    assert not soft_asserts.assert_false(True)
    assert soft_asserts.assert_false(False)
    assert not soft_asserts.assert_false(True, ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 2
    __verify_assert_all_raised_exception()


def test_assert_equal_fail(before_test):
    assert not soft_asserts.assert_equal(1, 2)
    assert soft_asserts.assert_equal(1, 1)
    assert not soft_asserts.assert_equal('1', '2')
    assert not soft_asserts.assert_equal('1', '2', ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 3
    __verify_assert_all_raised_exception()


def test_assert_not_equal_fail(before_test):
    assert not soft_asserts.assert_not_equal(1, 1)
    assert soft_asserts.assert_not_equal(1, 2)
    assert soft_asserts.assert_not_equal('1', '2')
    assert not soft_asserts.assert_not_equal('1', '1', ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 2
    __verify_assert_all_raised_exception()


def test_assert_is_fail(before_test):
    assert not soft_asserts.assert_is(1, 2)
    assert soft_asserts.assert_is(1, 1)
    assert not soft_asserts.assert_is('1', '2')
    assert not soft_asserts.assert_is('2', '1', ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 3
    __verify_assert_all_raised_exception()


def test_assert_is_not_fail(before_test):
    assert not soft_asserts.assert_is_not(1, 1)
    assert soft_asserts.assert_is_not(1, 2)
    assert soft_asserts.assert_is_not('2', '1')
    assert not soft_asserts.assert_is_not('1', '1', ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 2
    __verify_assert_all_raised_exception()


def test_assert_is_none_fail(before_test):
    assert not soft_asserts.assert_is_none(1)
    assert soft_asserts.assert_is_none(None)
    assert not soft_asserts.assert_is_none(1, ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 2
    __verify_assert_all_raised_exception()


def test_assert_is_not_none_fail(before_test):
    assert not soft_asserts.assert_is_not_none(None)
    assert soft_asserts.assert_is_not_none(1)
    assert not soft_asserts.assert_is_not_none(None, ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 2
    __verify_assert_all_raised_exception()


def test_assert_in_fail(before_test):
    assert not soft_asserts.assert_in(1, [2, 3, 4])
    assert soft_asserts.assert_in(1, [1, 2, 3])
    assert not soft_asserts.assert_in('1', ['2', '3', '4'])
    assert soft_asserts.assert_in('1', ['1', '2', '3'], ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 2
    __verify_assert_all_raised_exception()


def test_assert_not_in_fail(before_test):
    assert not soft_asserts.assert_not_in(1, [1, 2, 3])
    assert soft_asserts.assert_not_in(1, [2, 3, 4])
    assert not soft_asserts.assert_not_in('1', ['1', '2', '3'])
    assert soft_asserts.assert_not_in('1', ['2', '3', '4'], ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 2
    __verify_assert_all_raised_exception()


def test_assert_is_instance_fail(before_test):
    assert not soft_asserts.assert_is_instance(1, str)
    assert soft_asserts.assert_is_instance(1, int)
    assert soft_asserts.assert_is_instance('1', str)
    assert not soft_asserts.assert_is_instance('1', int, ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 2
    __verify_assert_all_raised_exception()


def test_assert_not_is_instance_fail(before_test):
    assert not soft_asserts.assert_not_is_instance(1, int)
    assert soft_asserts.assert_not_is_instance(1, str)
    assert not soft_asserts.assert_not_is_instance('1', str)
    assert not soft_asserts.assert_not_is_instance('1', str, ERROR_MESSAGE_1)
    assert len(soft_asserts.failures) == 3
    __verify_assert_all_raised_exception()


def test_assert_almost_equal_fail(before_test):
    assert not soft_asserts.assert_almost_equal(1.001, 1.0002, 0.00001)
    assert soft_asserts.assert_almost_equal(1.001, 1.0002, 0.002)
    assert len(soft_asserts.failures) == 1
    __verify_assert_all_raised_exception()


def test_assert_not_almost_equal_fail(before_test):
    assert not soft_asserts.assert_not_almost_equal(1.0001, 1.0002, 0.001)
    assert not soft_asserts.assert_not_almost_equal(1.0001, 1.0002, 0.002)
    assert len(soft_asserts.failures) == 2
    __verify_assert_all_raised_exception()


def test_assert_raises_fail(before_test):
    assert not soft_asserts.assert_raises(NotImplementedError, __raise_value_error)
    assert not soft_asserts.assert_raises(
        NotImplementedError, __raise_value_error, ERROR_MESSAGE_1)
    assert not soft_asserts.assert_raises(NotImplementedError, __not_raise_exception)
    assert len(soft_asserts.failures) == 3
    __verify_assert_all_raised_exception()


def test_assert_raised_with_fail(before_test):
    with soft_asserts.assert_raised_with(ValueError):
        _ = 1

    with soft_asserts.assert_raised_with(ValueError, ERROR_MESSAGE_1):
        raise NotImplementedError()

    assert len(soft_asserts.failures) == 2
    __verify_assert_all_raised_exception()


def test_fail_with_print_message(before_test):
    SoftAsserts.set_print_method(__print)
    soft_asserts.assert_true(False, ERROR_MESSAGE_1)
    assert print_message == ERROR_MESSAGE_1
    __verify_assert_all_raised_exception()


def test_fail_with_logger(before_test):
    logger = logging.getLogger('test')
    SoftAsserts.set_logger(logger)
    soft_asserts.assert_true(False, ERROR_MESSAGE_1)
    __verify_assert_all_raised_exception()


def test_fail_with_logger_and_print_message_negative(before_test):
    logger = logging.getLogger('test')
    SoftAsserts.set_logger(logger)
    SoftAsserts.set_print_method(__print)

    try:
        with pytest.raises(ValueError) as e:
            soft_asserts.assert_true(False, ERROR_MESSAGE_1)

        assert e.value.args[0] == 'Cannot set both logger and print_method'
    finally:
        with pytest.raises(AssertionError):
            soft_asserts.assert_all()


def test_steps(before_test):
    soft_asserts.set_step(STEP_1)
    soft_asserts.assert_true(True, ERROR_MESSAGE_1)
    soft_asserts.set_step(STEP_2)
    soft_asserts.assert_true(False, ERROR_MESSAGE_1)
    soft_asserts.set_step(STEP_3)
    soft_asserts.assert_true(False, ERROR_MESSAGE_1)

    assert len(soft_asserts.failures) == 2

    with pytest.raises(AssertionError):
        soft_asserts.assert_all()

    assert not soft_asserts.is_step_in_failure_steps(STEP_1)
    assert soft_asserts.is_step_in_failure_steps(STEP_2)
    assert soft_asserts.is_step_in_failure_steps(STEP_3)

    soft_asserts.init_failure_steps()

    assert not soft_asserts.is_step_in_failure_steps(STEP_2)
    assert not soft_asserts.is_step_in_failure_steps(STEP_3)


def test_unset_step(before_test):
    soft_asserts.set_step(STEP_1)
    soft_asserts.unset_step()

    soft_asserts.assert_true(False, ERROR_MESSAGE_1)

    soft_asserts.set_step(STEP_2)

    soft_asserts.assert_true(False)

    with pytest.raises(AssertionError):
        soft_asserts.assert_all()

    assert not soft_asserts.is_step_in_failure_steps(STEP_1)
    assert soft_asserts.is_step_in_failure_steps(STEP_2)


def test_step_not_exist_after_assert_all(before_test):
    soft_asserts.set_step(STEP_1)
    soft_asserts.assert_true(False, ERROR_MESSAGE_1)

    with pytest.raises(AssertionError):
        soft_asserts.assert_all()

    assert soft_asserts.is_step_in_failure_steps(STEP_1)

    soft_asserts.failure_steps = []
    soft_asserts.assert_true(False, ERROR_MESSAGE_1)

    with pytest.raises(AssertionError):
        soft_asserts.assert_all()

    assert not soft_asserts.is_step_in_failure_steps(STEP_1)


def test_step_not_in_failure_steps_before_assert_all(before_test):
    soft_asserts.set_step(STEP_1)
    soft_asserts.assert_true(False, ERROR_MESSAGE_1)

    assert not soft_asserts.is_step_in_failure_steps(STEP_1)

    with pytest.raises(AssertionError):
        soft_asserts.assert_all()

    assert soft_asserts.is_step_in_failure_steps(STEP_1)


def __verify_assert_all_raised_exception():
    with pytest.raises(AssertionError) as e:
        soft_asserts.assert_all()

    assert e.value


def __raise_value_error(msg: str = ''):
    raise ValueError(msg)


def __not_raise_exception():
    return


def __print(message):
    global print_message
    print_message = message
