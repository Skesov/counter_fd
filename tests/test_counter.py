import unittest

from counter import counter

def test_counter():
    answer = counter.count_fd()
    assert answer.isdigit()