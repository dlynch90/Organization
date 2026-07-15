import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from __init__ import ci_verification, hello_world


def test_hello_world():
    result = hello_world()
    assert result == "Hello from sample-module!"


def test_ci_verification():
    """Test that CI/CD workflow triggers correctly."""
    result = ci_verification()
    assert result == "CI/CD workflow verification successful!"
