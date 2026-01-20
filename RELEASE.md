# nrt-pytest-soft-asserts

## Version History

### Version 2.0.0

- Support for asynchronous context managers. `async with SoftAsserts()` and `async with sa.assert_raised_with`.

### Version 1.4.1

- Add new assertion method: `assert_greater`, `assert_greater_equal`, `assert_less`, `assert_less_equal`.
- Changed `is_step_in_failure_steps` name to `is_in_failure_steps`.

### Version 1.4.0

#### New features:
- Support pytest fixture.
- Support on_failure callback.

### Version 1.3.0

Support `with` statement.

### Version 1.2.4

Fix pyproject.toml.

### Version 1.2.3

Support Python 3.14.

### Version 1.2.2

Fix License.

### Version 1.2.1

Fix assert counts message.

### Version 1.2.0

#### New features:

Support with duplicated errors validation options.

### Version 1.1.3

Support Python 3.13.

### Version 1.1.2

Fix dependency issue.

### Version 1.1.1

Fix bug in README.md.

### Version 1.1.0

#### New features:

Error message is in `message [file_path: line_number] code_line` format.

### Version 1.0.9

Support in latest version of pytest.

### Version 1.0.8

GitHub workflow updates.

### Version 1.0.7

Fix bug in Python 3.8 support.

### Version 1.0.6

Support Python 3.8.

### Version 1.0.5

#### New Features

Assert methods return True if assertion passes, False if assertion fails.

Example:
```python
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts

soft_asserts = SoftAsserts()


def test_assert_equal():
    # result is True
    result = soft_asserts.assert_equal(1, 1)
    # result is False
    result = soft_asserts.assert_equal(1, 2)
    soft_asserts.assert_all()
    

def test_is_not_none():
    # result is True
    result = soft_asserts.assert_is_not_none(1)
    # result is False
    result = soft_asserts.assert_is_not_none(None)
    soft_asserts.assert_all()
```
