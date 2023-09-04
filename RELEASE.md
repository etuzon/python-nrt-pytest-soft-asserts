# nrt-pytest-soft-asserts

## Version 1.0.5

### New Features

assert methods return True if assertion passes, False if assertion fails.

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
