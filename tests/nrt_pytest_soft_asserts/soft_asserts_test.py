import logging
import pytest
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts, DuplicatedErrorsEnum, soft_asserts

ERROR_MESSAGE_1 = 'error message 1'
ERROR_MESSAGE_2 = 'error message 2'

STEP_1 = 'step 1'
STEP_2 = 'step 2'
STEP_3 = 'step 3'

STEPS = [STEP_2, STEP_3]


sa = SoftAsserts()

print_message = ''

is_on_failure = False


@pytest.fixture(autouse=True)
def before_test():

    SoftAsserts.unset_logger()
    SoftAsserts.unset_print_method()
    # If it fails, then Missing assert_all in tests
    sa.assert_all()
    sa.init_failure_steps()
    global is_on_failure
    is_on_failure = False


def test_assert_true():
    # Soft Asserts return True if assertion passes, False if assertion fails.
    assert sa.assert_true(True)
    assert sa.assert_true(True, ERROR_MESSAGE_1)
    assert sa.assert_true(True, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_false():
    assert sa.assert_false(False)
    assert sa.assert_false(False, ERROR_MESSAGE_1)
    assert sa.assert_false(False, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_equal():
    assert sa.assert_equal(1, 1)
    assert sa.assert_equal('1', '1', ERROR_MESSAGE_1)
    assert sa.assert_equal(2, 2, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_not_equal():
    assert sa.assert_not_equal(1, 2)
    assert sa.assert_not_equal('1', '2', ERROR_MESSAGE_1)
    assert sa.assert_not_equal(1, 5, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_is():
    a = b = SoftAsserts()

    assert sa.assert_is(1, 1)
    assert sa.assert_is('1', '1', ERROR_MESSAGE_1)
    assert sa.assert_is(a, b, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_is_not():
    a = SoftAsserts()
    b = SoftAsserts()

    assert sa.assert_is_not(1, 2)
    assert sa.assert_is_not('1', '2', ERROR_MESSAGE_1)
    assert sa.assert_is_not(a, b, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_is_none():
    assert sa.assert_is_none(None)
    assert sa.assert_is_none(None, ERROR_MESSAGE_1)
    assert sa.assert_is_none(None, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_is_not_none():
    assert sa.assert_is_not_none(1)
    assert sa.assert_is_not_none(1, ERROR_MESSAGE_1)
    assert sa.assert_is_not_none(1, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_in():
    assert sa.assert_in(1, [1, 2, 3])
    assert sa.assert_in('1', ['1', '2', '3'], ERROR_MESSAGE_1)
    assert sa.assert_in(2, [1, 2, 3], on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_not_in():
    assert sa.assert_not_in(1, [2, 3, 4])
    assert sa.assert_not_in('1', ['2', '3', '4'], ERROR_MESSAGE_1)
    assert sa.assert_not_in(5, [1, 2, 3], on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_is_instance():
    a = SoftAsserts()

    assert sa.assert_is_instance(1, int)
    assert sa.assert_is_instance('1', str, ERROR_MESSAGE_1)
    assert sa.assert_is_instance(a, SoftAsserts, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_not_is_instance():
    assert sa.assert_not_is_instance(1, str)
    assert sa.assert_not_is_instance('1', int, ERROR_MESSAGE_1)
    assert sa.assert_not_is_instance(1, str, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_almost_equal():
    assert sa.assert_almost_equal(1.0001, 1.0002, 0.002)
    assert sa.assert_almost_equal(1.0001, 1.0002, 0.002, ERROR_MESSAGE_1)
    assert sa.assert_almost_equal(1.0001, 1.0002, 0.002, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_not_almost_equal():
    assert sa.assert_not_almost_equal(1.0001, 1.0002, 0.000001)
    assert sa.assert_not_almost_equal(1.0001, 1.0002, 0.000001, ERROR_MESSAGE_1)
    assert sa.assert_not_almost_equal(1.0001, 1.0002, 0.000001, on_failure=__set_is_on_failure_true)

    assert not is_on_failure

    sa.assert_all()


def test_assert_raises():
    assert sa.assert_raises(ValueError, __raise_value_error)

    assert not is_on_failure

    sa.assert_all()


def test_assert_raised_with():

    with sa.assert_raised_with(ValueError):
        raise ValueError(ERROR_MESSAGE_1)

    sa.assert_all()

    with sa.assert_raised_with(ValueError, on_failure=__set_is_on_failure_true):
        raise ValueError(ERROR_MESSAGE_1)

    assert not is_on_failure

    sa.assert_all()


def test_assert_true_fail():

    assert not sa.assert_true(False)
    assert sa.assert_true(True)
    assert not sa.assert_true(False, ERROR_MESSAGE_1)
    assert not sa.assert_true(False, on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_false_fail():

    assert not sa.assert_false(True)
    assert sa.assert_false(False)
    assert not sa.assert_false(True, ERROR_MESSAGE_1)
    assert not sa.assert_false(True, on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_equal_fail():

    assert not sa.assert_equal(1, 2)
    assert sa.assert_equal(1, 1)
    assert not sa.assert_equal('1', '2')
    assert not sa.assert_equal('1', '2', ERROR_MESSAGE_1)
    assert not sa.assert_equal('1', '2', on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 4

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_not_equal_fail():

    assert not sa.assert_not_equal(1, 1)
    assert sa.assert_not_equal(1, 2)
    assert sa.assert_not_equal('1', '2')
    assert not sa.assert_not_equal('1', '1', ERROR_MESSAGE_1)
    assert not sa.assert_not_equal('1', '1', on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_is_fail():

    assert not sa.assert_is(1, 2)
    assert sa.assert_is(1, 1)
    assert not sa.assert_is('1', '2')
    assert not sa.assert_is('2', '1', ERROR_MESSAGE_1)
    assert not sa.assert_is('2', '1', on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 4

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_is_not_fail():

    assert not sa.assert_is_not(1, 1)
    assert sa.assert_is_not(1, 2)
    assert sa.assert_is_not('2', '1')
    assert not sa.assert_is_not('1', '1', ERROR_MESSAGE_1)
    assert not sa.assert_is_not('1', '1', on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_is_none_fail():

    assert not sa.assert_is_none(1)
    assert sa.assert_is_none(None)
    assert not sa.assert_is_none(1, ERROR_MESSAGE_1)
    assert not sa.assert_is_none(1, on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_is_not_none_fail():

    assert not sa.assert_is_not_none(None)
    assert sa.assert_is_not_none(1)
    assert not sa.assert_is_not_none(None, ERROR_MESSAGE_1)
    assert not sa.assert_is_not_none(None, on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_in_fail():

    assert not sa.assert_in(1, [2, 3, 4])
    assert sa.assert_in(1, [1, 2, 3])
    assert not sa.assert_in('1', ['2', '3', '4'])
    assert sa.assert_in('1', ['1', '2', '3'], ERROR_MESSAGE_1)
    assert not sa.assert_in('8', ['1', '2', '3'], on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_not_in_fail():

    assert not sa.assert_not_in(1, [1, 2, 3])
    assert sa.assert_not_in(1, [2, 3, 4])
    assert not sa.assert_not_in('1', ['1', '2', '3'])
    assert sa.assert_not_in('1', ['2', '3', '4'], ERROR_MESSAGE_1)
    assert not sa.assert_not_in('2', ['1', '2', '3'], on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_is_instance_fail():

    assert not sa.assert_is_instance(1, str)
    assert sa.assert_is_instance(1, int)
    assert sa.assert_is_instance('1', str)
    assert not sa.assert_is_instance('1', int, ERROR_MESSAGE_1)
    assert not sa.assert_is_instance(1, str, on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_not_is_instance_fail():

    assert not sa.assert_not_is_instance(1, int)
    assert sa.assert_not_is_instance(1, str)
    assert not sa.assert_not_is_instance('1', str)
    assert not sa.assert_not_is_instance('1', str, ERROR_MESSAGE_1)
    assert not sa.assert_not_is_instance(1, int, on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 4

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_almost_equal_fail():

    assert not sa.assert_almost_equal(1.001, 1.0002, 0.00001)
    assert sa.assert_almost_equal(1.001, 1.0002, 0.002)
    assert not sa.assert_almost_equal(1.001, 1.0002, 0.00001, ERROR_MESSAGE_1)
    assert not sa.assert_almost_equal(1.001, 1.0002, 0.00001, on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_not_almost_equal_fail():

    assert not sa.assert_not_almost_equal(1.0001, 1.0002, 0.001)
    assert not sa.assert_not_almost_equal(1.0001, 1.0002, 0.002)
    assert sa.assert_not_almost_equal(1.0001, 1.0002, 0.000001, ERROR_MESSAGE_1)
    assert not sa.assert_not_almost_equal(1.0001, 1.0002, 0.001, on_failure=__set_is_on_failure_true)

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_raises_fail():

    assert not sa.assert_raises(NotImplementedError, __raise_value_error)
    assert not sa.assert_raises(NotImplementedError, __raise_value_error, ERROR_MESSAGE_1)
    assert not sa.assert_raises(NotImplementedError, __not_raise_exception)

    assert len(sa.failures) == 3

    assert not is_on_failure

    __verify_assert_all_raised_exception()


def test_assert_raised_with_fail():

    with sa.assert_raised_with(ValueError):
        _ = 1

    with sa.assert_raised_with(ValueError, ERROR_MESSAGE_1):
        raise NotImplementedError()

    with sa.assert_raised_with(ValueError, on_failure=__set_is_on_failure_true):
        raise NotImplementedError()

    assert len(sa.failures) == 3

    assert is_on_failure

    __verify_assert_all_raised_exception()


def test_fail_with_print_message():

    SoftAsserts.set_print_method(__print)
    sa.assert_true(False, ERROR_MESSAGE_1)
    assert print_message.startswith(f'[1] {ERROR_MESSAGE_1}')
    __verify_assert_all_raised_exception()


def test_fail_with_logger():

    logger = logging.getLogger('test')
    SoftAsserts.set_logger(logger)
    sa.assert_true(False, ERROR_MESSAGE_1)
    __verify_assert_all_raised_exception()


def test_fail_with_logger_and_print_message_negative():

    logger = logging.getLogger('test')
    SoftAsserts.set_logger(logger)
    SoftAsserts.set_print_method(__print)

    try:
        with pytest.raises(ValueError) as e:
            sa.assert_true(False, ERROR_MESSAGE_1)

        assert e.value.args[0] == 'Cannot set both logger and print_method'
    finally:
        with pytest.raises(AssertionError):
            sa.assert_all()


def test_steps():

    sa.set_step(STEP_1)
    sa.assert_true(True, ERROR_MESSAGE_1)
    sa.set_step(STEP_2)
    sa.assert_true(False, ERROR_MESSAGE_1)
    sa.set_step(STEP_3)
    sa.assert_true(False, ERROR_MESSAGE_1)

    assert len(sa.failures) == 2

    with pytest.raises(AssertionError):
        sa.assert_all()

    assert not sa.is_step_in_failure_steps(STEP_1)
    assert sa.is_step_in_failure_steps(STEP_2)
    assert sa.is_step_in_failure_steps(STEP_3)

    sa.init_failure_steps()

    assert not sa.is_step_in_failure_steps(STEP_2)
    assert not sa.is_step_in_failure_steps(STEP_3)


def test_unset_step():

    sa.set_step(STEP_1)
    sa.unset_step()

    sa.assert_true(False, ERROR_MESSAGE_1)

    sa.set_step(STEP_2)

    sa.assert_true(False)

    with pytest.raises(AssertionError):
        sa.assert_all()

    assert not sa.is_step_in_failure_steps(STEP_1)
    assert sa.is_step_in_failure_steps(STEP_2)


def test_step_not_exist_after_assert_all():

    sa.set_step(STEP_1)
    sa.assert_true(False, ERROR_MESSAGE_1)

    with pytest.raises(AssertionError):
        sa.assert_all()

    assert sa.is_step_in_failure_steps(STEP_1)

    sa.failure_steps = []
    sa.assert_true(False, ERROR_MESSAGE_1)

    with pytest.raises(AssertionError):
        sa.assert_all()

    assert not sa.is_step_in_failure_steps(STEP_1)


def test_step_not_in_failure_steps_before_assert_all():

    sa.set_step(STEP_1)
    sa.assert_true(False, ERROR_MESSAGE_1)

    assert not sa.is_step_in_failure_steps(STEP_1)

    with pytest.raises(AssertionError):
        sa.assert_all()

    assert sa.is_step_in_failure_steps(STEP_1)


def test_print_duplicate_errors_value_no_duplicated_errors_code_source():

    sa.print_duplicate_errors = \
        DuplicatedErrorsEnum.NO_DUPLICATED_ERRORS_CODE_SOURCE

    __soft_assert_true(False, ERROR_MESSAGE_1)
    __soft_assert_true(False, ERROR_MESSAGE_1)
    __soft_assert_true(False, ERROR_MESSAGE_2)

    assert len(sa.failures) == 1

    with pytest.raises(AssertionError) as e:
        sa.assert_all()

    assert e.value.args[0].count(ERROR_MESSAGE_1) == 1
    assert e.value.args[0].count(f'[3] {ERROR_MESSAGE_1}') == 1


def test_print_duplicate_errors_value_no_duplicated_errors_code_source_and_error():

    sa.print_duplicate_errors = \
        DuplicatedErrorsEnum.NO_DUPLICATED_ERRORS_CODE_SOURCE_AND_ERROR

    __soft_assert_true(False, ERROR_MESSAGE_1)
    __soft_assert_true(False, ERROR_MESSAGE_1)
    __soft_assert_true(False, ERROR_MESSAGE_2)

    assert len(sa.failures) == 2

    with pytest.raises(AssertionError) as e:
        sa.assert_all()

    assert e.value.args[0].count(ERROR_MESSAGE_1) == 1
    assert e.value.args[0].count(ERROR_MESSAGE_2) == 1
    assert e.value.args[0].count(f'[2] {ERROR_MESSAGE_1}') == 1
    assert e.value.args[0].count(f'[1] {ERROR_MESSAGE_2}') == 1


def test_with_statement():

    with pytest.raises(AssertionError) as e:
        with sa:
            __soft_assert_true(False, ERROR_MESSAGE_1)
            __soft_assert_true(True)
            assert len(sa.failures) == 1

    assert not len(sa.failures)

    assert e.value.args[0].count(ERROR_MESSAGE_1) == 1

    sa.assert_all()


def test_decorator_soft_asserts():

    with pytest.raises(AssertionError) as e:

        @soft_asserts(sa=sa)
        def test_function():
            __soft_assert_true(False, ERROR_MESSAGE_1)

        test_function()

    assert e.value.args[0].count(ERROR_MESSAGE_1) == 1


def __soft_assert_true(condition: bool, message: str = ''):
    sa.assert_true(condition, message)


def __verify_assert_all_raised_exception():
    with pytest.raises(AssertionError) as e:
        sa.assert_all()

    assert e.value


def __raise_value_error(msg: str = ''):
    raise ValueError(msg)


def __not_raise_exception():
    return


def __print(message):
    global print_message
    print_message = message


def __set_is_on_failure_true():
    global is_on_failure
    is_on_failure = True
