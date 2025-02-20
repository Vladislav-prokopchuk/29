from gcd import gcd


def test_gcd():
    assert gcd(60, 48) == 12
    assert gcd(101, 10) == 1
    assert gcd(25, 5) == 5
