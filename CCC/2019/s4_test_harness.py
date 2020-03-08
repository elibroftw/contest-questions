from s4_tourism import *


def test_harness(n, k, attractions):
    assert tourism(n, k, attractions)
    findings.clear()

assert tourism(12, 6, (2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2)) == 5
assert tourism(12, 7, (2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2)) == 6
assert tourism(12, 7, (2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2)) == 6
assert tourism(12, 10, (2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2)) == 6
assert tourism(12, 10, (2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2)) == 6
assert tourism(12, 10, (2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)) == 5
assert tourism(12, 11, (3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3)) == 6
assert tourism(12, 11, (3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)) == 5
assert tourism(12, 11, (3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)) == 6
assert tourism(12, 11, (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3)) == 6
assert tourism(12, 12, (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3)) == 3
assert tourism(12, 3, (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3)) == 9
assert tourism(12, 4, (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3)) == 7
assert tourism(12, 5, (2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3)) == 8
assert tourism(12, 5, (3, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2)) == 8
assert tourism(6, 4, (1, 2, 3, 4, 5, 6)) == 10
assert tourism(6, 4, (4, 5, 3, 6, 1, 2)) == 11
assert tourism(6, 2, (2, 5, 7, 1, 4, 3)) == 16
assert tourism(5, 2, (2, 5, 7, 1, 4)) == 16
assert tourism(5, 3, (2, 5, 7, 1, 4)) == 12 
assert tourism(1, 5, (1,)) == 1
assert tourism(2, 5, (1, 3)) == 3
assert tourism(6, 4, (1, 2, 3, 4, 5, 6)) == 10
assert tourism(6, 4, (4, 5, 6, 1, 2, 3)) == 11
findings.clear()