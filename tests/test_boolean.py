"""Boolean 类型测试"""
import pytest
from pypp import Boolean, Integer, Float, String


class TestBooleanCreation:
    def test_create_true(self):
        b = Boolean(True)
        assert bool(b) is True

    def test_create_false(self):
        b = Boolean(False)
        assert bool(b) is False

    def test_create_from_int(self):
        assert Boolean(1).is_true()
        assert Boolean(0).is_false()
        assert Boolean(42).is_true()

    def test_create_from_string(self):
        assert Boolean("hello").is_true()
        assert Boolean("").is_false()

    def test_create_from_none(self):
        assert Boolean(None).is_false()

    def test_create_default(self):
        assert Boolean().is_false()

    def test_is_instance_of_int(self):
        assert isinstance(Boolean(True), int)


class TestBooleanRepr:
    def test_repr_true(self):
        assert repr(Boolean(True)) == "Boolean(True)"

    def test_repr_false(self):
        assert repr(Boolean(False)) == "Boolean(False)"

    def test_str_true(self):
        assert str(Boolean(True)) == "True"

    def test_str_false(self):
        assert str(Boolean(False)) == "False"


class TestBooleanJudgment:
    def test_is_true(self):
        assert Boolean(True).is_true() is True
        assert Boolean(False).is_true() is False

    def test_is_false(self):
        assert Boolean(False).is_false() is True
        assert Boolean(True).is_false() is False


class TestBooleanLogic:
    def test_toggle(self):
        b = Boolean(True)
        assert b.toggle().is_false()
        assert Boolean(False).toggle().is_true()

    def test_and(self):
        assert bool(Boolean(True) and Boolean(True)) is True
        assert bool(Boolean(True) and Boolean(False)) is False

    def test_or(self):
        assert bool(Boolean(False) or Boolean(True)) is True
        assert bool(Boolean(False) or Boolean(False)) is False


class TestBooleanConversions:
    def test_to_string(self):
        assert str(Boolean(True).to_string()) == "True"
        assert str(Boolean(False).to_string()) == "False"

    def test_to_integer(self):
        assert int(Boolean(True).to_integer()) == 1
        assert int(Boolean(False).to_integer()) == 0

    def test_to_float(self):
        assert float(Boolean(True).to_float()) == 1.0
        assert float(Boolean(False).to_float()) == 0.0

    def test_to_list_raises(self):
        with pytest.raises(TypeError):
            Boolean(True).to_list()
