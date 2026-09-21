"""Integer 类型测试"""
import pytest
from pypp import Integer, Float, String, Boolean, PyList


class TestIntegerCreation:
    def test_create_from_int(self):
        n = Integer(42)
        assert int(n) == 42

    def test_create_from_float(self):
        n = Integer(3.9)
        assert int(n) == 3

    def test_create_from_string(self):
        n = Integer("123")
        assert int(n) == 123

    def test_create_default(self):
        n = Integer()
        assert int(n) == 0

    def test_create_none(self):
        n = Integer(None)
        assert int(n) == 0

    def test_create_invalid(self):
        n = Integer("abc")
        assert int(n) == 0

    def test_is_instance_of_int(self):
        assert isinstance(Integer(5), int)


class TestIntegerRepr:
    def test_repr(self):
        assert repr(Integer(42)) == "Integer(42)"

    def test_str(self):
        assert str(Integer(42)) == "42"

    def test_negative_repr(self):
        assert repr(Integer(-7)) == "Integer(-7)"


class TestIntegerParity:
    def test_is_even_true(self):
        assert Integer(4).is_even() is True

    def test_is_even_false(self):
        assert Integer(3).is_even() is False

    def test_is_odd_true(self):
        assert Integer(3).is_odd() is True

    def test_is_odd_false(self):
        assert Integer(4).is_odd() is False

    def test_zero_is_even(self):
        assert Integer(0).is_even() is True


class TestIntegerSign:
    def test_is_positive(self):
        assert Integer(5).is_positive() is True
        assert Integer(-5).is_positive() is False
        assert Integer(0).is_positive() is False

    def test_is_negative(self):
        assert Integer(-5).is_negative() is True
        assert Integer(5).is_negative() is False
        assert Integer(0).is_negative() is False

    def test_is_zero(self):
        assert Integer(0).is_zero() is True
        assert Integer(1).is_zero() is False


class TestIntegerNumberTheory:
    def test_is_prime(self):
        assert Integer(2).is_prime() is True
        assert Integer(3).is_prime() is True
        assert Integer(4).is_prime() is False
        assert Integer(17).is_prime() is True
        assert Integer(1).is_prime() is False
        assert Integer(0).is_prime() is False
        assert Integer(-5).is_prime() is False

    def test_is_palindrome(self):
        assert Integer(121).is_palindrome() is True
        assert Integer(12321).is_palindrome() is True
        assert Integer(123).is_palindrome() is False
        assert Integer(-121).is_palindrome() is True  # abs value

    def test_is_perfect_square(self):
        assert Integer(4).is_perfect_square() is True
        assert Integer(9).is_perfect_square() is True
        assert Integer(16).is_perfect_square() is True
        assert Integer(8).is_perfect_square() is False
        assert Integer(-4).is_perfect_square() is False
        assert Integer(0).is_perfect_square() is True

    def test_is_perfect_cube(self):
        assert Integer(8).is_perfect_cube() is True
        assert Integer(27).is_perfect_cube() is True
        assert Integer(-8).is_perfect_cube() is True
        assert Integer(9).is_perfect_cube() is False

    def test_is_perfect_power(self):
        assert Integer(8).is_perfect_power(2) is True   # 2^3
        assert Integer(16).is_perfect_power(2) is True  # 2^4
        assert Integer(27).is_perfect_power(3) is True  # 3^3
        assert Integer(10).is_perfect_power(2) is False
        assert Integer(1).is_perfect_power(2) is True

    def test_is_armstrong(self):
        assert Integer(153).is_armstrong() is True   # 1^3 + 5^3 + 3^3 = 153
        assert Integer(370).is_armstrong() is True
        assert Integer(9474).is_armstrong() is True  # 4 digits
        assert Integer(123).is_armstrong() is False


class TestIntegerMath:
    def test_factorial(self):
        assert Integer(5).factorial() == 120
        assert Integer(0).factorial() == 1
        assert Integer(1).factorial() == 1

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            Integer(-1).factorial()

    def test_digits(self):
        assert Integer(12345).digits() == [1, 2, 3, 4, 5]
        assert Integer(0).digits() == [0]
        assert Integer(-789).digits() == [7, 8, 9]

    def test_digit_sum(self):
        assert Integer(12345).digit_sum() == 15
        assert Integer(999).digit_sum() == 27

    def test_digit_product(self):
        assert Integer(123).digit_product() == 6
        assert Integer(999).digit_product() == 729


class TestIntegerBaseConversion:
    def test_to_binary(self):
        assert Integer(10).to_binary() == "1010"
        assert Integer(0).to_binary() == "0"
        assert Integer(255).to_binary() == "11111111"

    def test_to_octal(self):
        assert Integer(8).to_octal() == "10"
        assert Integer(64).to_octal() == "100"

    def test_to_hex(self):
        assert Integer(255).to_hex() == "ff"
        assert Integer(16).to_hex() == "10"


class TestIntegerConversions:
    def test_to_integer(self):
        n = Integer(42)
        result = n.to_integer()
        assert isinstance(result, Integer)
        assert int(result) == 42

    def test_to_float(self):
        result = Integer(42).to_float()
        assert isinstance(result, Float)
        assert float(result) == 42.0

    def test_to_string(self):
        result = Integer(42).to_string()
        assert isinstance(result, String)
        assert str(result) == "42"

    def test_to_boolean(self):
        assert Integer(1).to_boolean().is_true()
        assert Integer(0).to_boolean().is_false()

    def test_to_list(self):
        result = Integer(123).to_list()
        assert isinstance(result, PyList)
        assert list(result) == [1, 2, 3]


class TestIntegerArithmetic:
    def test_addition(self):
        assert Integer(3) + Integer(2) == 5
        assert Integer(3) + 2 == 5

    def test_multiplication(self):
        assert Integer(3) * Integer(4) == 12

    def test_comparison(self):
        assert Integer(3) < Integer(5)
        assert Integer(5) > Integer(3)
        assert Integer(5) == Integer(5)
