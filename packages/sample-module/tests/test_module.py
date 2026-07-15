import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from __init__ import hello_world


def test_hello_world():
    result = hello_world()
    assert result == "Hello from sample-module!"
