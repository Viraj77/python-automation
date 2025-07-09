from ..practiceDays.DaySixFunctionsAndScopes.prime_number import is_prime

def test_is_prime():
    assert is_prime(2) == True, "2 should be prime"
    assert is_prime(3) == True, "3 should be prime"
    assert is_prime(4) == False, "4 should not be prime"
    assert is_prime(5) == True, "5 should be prime"
    assert is_prime(16) == False, "16 should not be prime"
    assert is_prime(17) == True, "17 should be prime"
    assert is_prime(1) == False, "1 should not be prime"
    assert is_prime(-5) == False, "-5 should not be prime"