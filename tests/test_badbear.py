import unittest
from badbear import BadBearVisitor, BB001
from flake8_plugin_utils import assert_error, assert_not_error


def test_BB001_error():
    assert_error(
        BadBearVisitor,
        'a(b=10)[2]',
        BB001,
    )

def test_BB001_not_error():
    assert_not_error(
        BadBearVisitor,
        'a(b=10)',
        BB001,
    )
    
if __name__ == "__main__":
    unittest.main()
