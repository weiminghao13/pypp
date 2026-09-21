"""智能迭代器测试"""
import pytest
from pypp.iter_object import (
    SmartIterBigData,
    SmartIterSmallData,
    auto_choose_iterator,
    is_small_data,
)


class TestIsSmallData:
    def test_small_list(self):
        assert is_small_data([1, 2, 3]) is True

    def test_empty_list(self):
        assert is_small_data([]) is True

    def test_small_tuple(self):
        assert is_small_data((1, 2, 3)) is True

    def test_small_set(self):
        assert is_small_data({1, 2, 3}) is True

    def test_small_dict(self):
        assert is_small_data({"a": 1}) is True

    def test_small_string(self):
        assert is_small_data("hello") is True

    def test_generator_is_not_small(self):
        gen = (x for x in range(10))
        assert is_small_data(gen) is False

    def test_non_iterable(self):
        assert is_small_data(42) is False
        assert is_small_data(None) is False

    def test_big_dict_is_not_small(self):
        big_dict = {f"key_{i}": i for i in range(1001)}
        assert is_small_data(big_dict) is False


class TestSmartIterSmallData:
    def test_creation(self):
        it = SmartIterSmallData([1, 2, 3])
        assert list(it) == [1, 2, 3]

    def test_creation_from_string(self):
        it = SmartIterSmallData("abc")
        assert list(it) == ["a", "b", "c"]

    def test_creation_non_iterable(self):
        with pytest.raises(TypeError):
            SmartIterSmallData(42)

    def test_iteration(self):
        it = SmartIterSmallData([1, 2, 3])
        result = []
        for item in it:
            result.append(item)
        assert result == [1, 2, 3]

    def test_len(self):
        it = SmartIterSmallData([1, 2, 3])
        assert len(it) == 3

    def test_getitem(self):
        it = SmartIterSmallData([10, 20, 30])
        assert it[0] == 10
        assert it[2] == 30

    def test_getitem_slice(self):
        it = SmartIterSmallData([1, 2, 3, 4, 5])
        assert it[1:4] == [2, 3, 4]

    def test_setitem(self):
        it = SmartIterSmallData([1, 2, 3])
        it[0] = 99
        assert it[0] == 99

    def test_reset(self):
        it = SmartIterSmallData([1, 2, 3])
        next(it)
        next(it)
        it.reset()
        assert next(it) == 1

    def test_change(self):
        it = SmartIterSmallData([1, 2, 3])
        it.change(1, 99)
        assert it[1] == 99

    def test_append(self):
        it = SmartIterSmallData([1, 2])
        it.append(3)
        assert list(it.data) == [1, 2, 3]

    def test_to_list(self):
        it = SmartIterSmallData([1, 2, 3])
        assert it.to_list() == [1, 2, 3]

    def test_repr(self):
        it = SmartIterSmallData([1, 2])
        assert "SmartIterSmallData" in repr(it)


class TestSmartIterBigData:
    def test_creation(self):
        it = SmartIterBigData([1, 2, 3])
        assert list(it) == [1, 2, 3]

    def test_creation_non_iterable(self):
        with pytest.raises(TypeError):
            SmartIterBigData(42)

    def test_iteration(self):
        it = SmartIterBigData([1, 2, 3])
        result = []
        for item in it:
            result.append(item)
        assert result == [1, 2, 3]

    def test_len_raises(self):
        it = SmartIterBigData([1, 2, 3])
        with pytest.raises(TypeError):
            len(it)

    def test_getitem_raises(self):
        it = SmartIterBigData([1, 2, 3])
        with pytest.raises(NotImplementedError):
            it[0]

    def test_reset(self):
        it = SmartIterBigData([1, 2, 3])
        next(it)
        it.reset()
        assert next(it) == 1

    def test_repr(self):
        it = SmartIterBigData([1, 2])
        assert "SmartIterBigData" in repr(it)


class TestAutoChooseIterator:
    def test_small_data_chooses_small(self):
        result = auto_choose_iterator([1, 2, 3])
        assert isinstance(result, SmartIterSmallData)

    def test_big_data_chooses_big(self):
        big_list = list(range(1_000_001))
        result = auto_choose_iterator(big_list)
        assert isinstance(result, SmartIterBigData)

    def test_generator_chooses_big(self):
        gen = (x for x in range(10))
        result = auto_choose_iterator(gen)
        assert isinstance(result, SmartIterBigData)
