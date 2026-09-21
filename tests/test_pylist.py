"""PyList 类型测试"""
import pytest
from pypp import PyList, Integer, Float, Boolean, String


class TestPyListCreation:
    def test_create_from_list(self):
        lst = PyList([1, 2, 3])
        assert list(lst) == [1, 2, 3]

    def test_create_from_tuple(self):
        lst = PyList((1, 2, 3))
        assert list(lst) == [1, 2, 3]

    def test_create_from_generator(self):
        lst = PyList(x for x in range(3))
        assert list(lst) == [0, 1, 2]

    def test_create_default(self):
        lst = PyList()
        assert list(lst) == []

    def test_create_none(self):
        lst = PyList(None)
        assert list(lst) == []

    def test_is_instance_of_list(self):
        assert isinstance(PyList([1, 2]), list)


class TestPyListRepr:
    def test_repr(self):
        assert repr(PyList([1, 2, 3])) == "PyList([1, 2, 3])"

    def test_str(self):
        assert str(PyList([1, 2, 3])) == "[1, 2, 3]"


class TestPyListBasic:
    def test_is_empty(self):
        assert PyList([]).is_empty() is True
        assert PyList([1]).is_empty() is False


class TestPyListConversions:
    def test_to_string(self):
        result = PyList([1, 2, 3]).to_string()
        assert isinstance(result, String)
        assert str(result) == "123"

    def test_to_string_strings(self):
        result = PyList(["a", "b", "c"]).to_string()
        assert str(result) == "abc"

    def test_to_integer_list(self):
        result = PyList([1, 2, 3]).to_integer_list()
        assert isinstance(result, PyList)
        assert all(isinstance(x, Integer) for x in result)
        assert [int(x) for x in result] == [1, 2, 3]

    def test_to_integer_list_from_strings(self):
        result = PyList(["1", "2", "3"]).to_integer_list()
        assert [int(x) for x in result] == [1, 2, 3]

    def test_to_integer_list_invalid(self):
        assert PyList(["a", "b"]).to_integer_list() is None

    def test_to_float_list(self):
        result = PyList([1, 2, 3]).to_float_list()
        assert all(isinstance(x, Float) for x in result)
        assert [float(x) for x in result] == [1.0, 2.0, 3.0]

    def test_to_float_list_invalid(self):
        assert PyList(["a", "b"]).to_float_list() is None

    def test_to_boolean_list(self):
        result = PyList([0, 1, "", "hello"]).to_boolean_list()
        assert all(isinstance(x, Boolean) for x in result)
        assert [bool(x) for x in result] == [False, True, False, True]

    def test_to_list(self):
        original = PyList([1, 2, 3])
        result = original.to_list()
        assert isinstance(result, PyList)
        assert list(result) == [1, 2, 3]
        assert result is not original


class TestPyListSorting:
    def test_sorted_list(self):
        result = PyList([3, 1, 4, 1, 5]).sorted_list()
        assert isinstance(result, PyList)
        assert list(result) == [1, 1, 3, 4, 5]

    def test_sorted_list_reverse(self):
        result = PyList([3, 1, 4]).sorted_list(reverse=True)
        assert list(result) == [4, 3, 1]

    def test_sorted_list_key(self):
        result = PyList(["banana", "apple", "cherry"]).sorted_list(key=len)
        assert list(result) == ["apple", "banana", "cherry"]

    def test_reverse(self):
        result = PyList([1, 2, 3]).reverse()
        assert isinstance(result, PyList)
        assert list(result) == [3, 2, 1]


class TestPyListSetOps:
    def test_unique(self):
        result = PyList([1, 2, 2, 3, 3, 3]).unique()
        assert isinstance(result, PyList)
        assert list(result) == [1, 2, 3]

    def test_unique_preserves_order(self):
        result = PyList([3, 1, 3, 2, 1]).unique()
        assert list(result) == [3, 1, 2]

    def test_flatten(self):
        result = PyList([1, [2, 3], [4, [5, 6]]]).flatten()
        assert list(result) == [1, 2, 3, 4, 5, 6]

    def test_flatten_already_flat(self):
        result = PyList([1, 2, 3]).flatten()
        assert list(result) == [1, 2, 3]

    def test_chunk(self):
        result = PyList([1, 2, 3, 4, 5]).chunk(2)
        assert len(result) == 3
        assert list(result[0]) == [1, 2]
        assert list(result[1]) == [3, 4]
        assert list(result[2]) == [5]

    def test_chunk_invalid_size(self):
        with pytest.raises(ValueError):
            PyList([1, 2, 3]).chunk(0)


class TestPyListFunctional:
    def test_map(self):
        result = PyList([1, 2, 3]).map(lambda x: x * 2)
        assert isinstance(result, PyList)
        assert list(result) == [2, 4, 6]

    def test_filter(self):
        result = PyList([1, 2, 3, 4, 5]).filter(lambda x: x % 2 == 0)
        assert list(result) == [2, 4]

    def test_reduce(self):
        result = PyList([1, 2, 3, 4]).reduce(lambda x, y: x + y)
        assert result == 10

    def test_reduce_with_initial(self):
        result = PyList([1, 2, 3]).reduce(lambda x, y: x + y, 10)
        assert result == 16

    def test_reduce_empty_no_initial(self):
        with pytest.raises(TypeError):
            PyList([]).reduce(lambda x, y: x + y)


class TestPyListStats:
    def test_frequency(self):
        result = PyList([1, 2, 2, 3, 3, 3]).frequency()
        assert result == {1: 1, 2: 2, 3: 3}

    def test_most_common(self):
        result = PyList([1, 2, 2, 3, 3, 3]).most_common()
        assert list(result) == [3, 2, 1]

    def test_most_common_n(self):
        result = PyList([1, 2, 2, 3, 3, 3]).most_common(2)
        assert list(result) == [3, 2]


class TestPyListNativeOps:
    def test_append(self):
        lst = PyList([1, 2])
        lst.append(3)
        assert list(lst) == [1, 2, 3]

    def test_indexing(self):
        lst = PyList([10, 20, 30])
        assert lst[0] == 10
        assert lst[-1] == 30

    def test_slicing(self):
        lst = PyList([1, 2, 3, 4, 5])
        assert lst[1:4] == [2, 3, 4]

    def test_len(self):
        assert len(PyList([1, 2, 3])) == 3

    def test_in(self):
        assert 2 in PyList([1, 2, 3])
