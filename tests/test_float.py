"""Float 类型测试"""
import math
import pytest
from pypp import Float, Integer, String, Boolean


class TestFloatCreation:
    def test_create_from_float(self):
        f = Float(3.14)
        assert float(f) == 3.14

    def test_create_from_int(self):
        f = Float(42)
        assert float(f) == 42.0

    def test_create_from_string(self):
        f = Float("3.14")
        assert float(f) == 3.14

    def test_create_default(self):
        f = Float()
        assert float(f) == 0.0

    def test_create_none(self):
        f = Float(None)
        assert float(f) == 0.0

    def test_is_instance_of_float(self):
        assert isinstance(Float(3.14), float)


class TestFloatRepr:
    def test_repr(self):
        assert repr(Float(3.14)) == "Float(3.14)"

    def test_str(self):
        assert str(Float(3.14)) == "3.14"


class TestFloatSign:
    def test_is_positive(self):
        assert Float(3.14).is_positive() is True
        assert Float(-3.14).is_positive() is False
        assert Float(0.0).is_positive() is False

    def test_is_negative(self):
        assert Float(-3.14).is_negative() is True
        assert Float(3.14).is_negative() is False

    def test_is_zero(self):
        assert Float(0.0).is_zero() is True
        assert Float(0.001).is_zero() is False


class TestFloatProperties:
    def test_is_integer(self):
        assert Float(3.0).is_integer() is True
        assert Float(3.14).is_integer() is False

    def test_is_nan(self):
        assert Float(float("nan")).is_nan() is True
        assert Float(3.14).is_nan() is False

    def test_is_inf(self):
        assert Float(float("inf")).is_inf() is True
        assert Float(float("-inf")).is_inf() is True
        assert Float(3.14).is_inf() is False

    def test_is_finite(self):
        assert Float(3.14).is_finite() is True
        assert Float(float("inf")).is_finite() is False
        assert Float(float("nan")).is_finite() is False


class TestFloatRounding:
    def test_floor(self):
        result = Float(3.7).floor()
        assert isinstance(result, Integer)
        assert int(result) == 3

    def test_floor_negative(self):
        result = Float(-3.7).floor()
        assert int(result) == -4

    def test_ceil(self):
        result = Float(3.2).ceil()
        assert isinstance(result, Integer)
        assert int(result) == 4

    def test_ceil_negative(self):
        result = Float(-3.2).ceil()
        assert int(result) == -3

    def test_round_to(self):
        result = Float(3.14159).round_to(2)
        assert isinstance(result, Float)
        assert abs(float(result) - 3.14) < 1e-9

    def test_round_to_zero(self):
        result = Float(3.7).round_to(0)
        assert float(result) == 4.0


class TestFloatConversions:
    def test_to_integer(self):
        result = Float(3.7).to_integer()
        assert isinstance(result, Integer)
        assert int(result) == 3

    def test_to_float(self):
        result = Float(3.14).to_float()
        assert isinstance(result, Float)
        assert float(result) == 3.14

    def test_to_string(self):
        result = Float(3.14).to_string()
        assert isinstance(result, String)

    def test_to_boolean(self):
        assert Float(1.0).to_boolean().is_true()
        assert Float(0.0).to_boolean().is_false()

    def test_to_list_raises(self):
        with pytest.raises(TypeError):
            Float(3.14).to_list()
