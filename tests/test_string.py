"""String 类型测试"""
import pytest
from pypp import String, Integer, Float, Boolean, PyList


class TestStringCreation:
    def test_create_from_str(self):
        s = String("hello")
        assert str(s) == "hello"

    def test_create_from_int(self):
        s = String(42)
        assert str(s) == "42"

    def test_create_from_float(self):
        s = String(3.14)
        assert str(s) == "3.14"

    def test_create_default(self):
        s = String()
        assert str(s) == ""

    def test_create_none(self):
        s = String(None)
        assert str(s) == ""

    def test_is_instance_of_str(self):
        assert isinstance(String("hello"), str)


class TestStringRepr:
    def test_repr(self):
        assert repr(String("hello")) == "String('hello')"

    def test_str(self):
        assert str(String("hello")) == "hello"


class TestStringBasic:
    def test_is_empty(self):
        assert String("").is_empty() is True
        assert String("hello").is_empty() is False

    def test_length(self):
        assert String("hello").length() == 5
        assert String("").length() == 0

    def test_is_ascii(self):
        assert String("hello").is_ascii() is True
        assert String("你好").is_ascii() is False

    def test_all_char(self):
        assert String("aaa").all_char("a") is True
        assert String("aab").all_char("a") is False
        assert String("").all_char("a") is False

    def test_is_numeric(self):
        assert String("123").is_numeric() is True
        assert String("12.3").is_numeric() is False
        assert String("abc").is_numeric() is False

    def test_is_alpha(self):
        assert String("abc").is_alpha() is True
        assert String("abc123").is_alpha() is False

    def test_is_alphanumeric(self):
        assert String("abc123").is_alphanumeric() is True
        assert String("abc 123").is_alphanumeric() is False


class TestStringPalindrome:
    def test_is_palindrome_true(self):
        assert String("racecar").is_palindrome() is True
        assert String("A man a plan a canal Panama").is_palindrome() is True

    def test_is_palindrome_false(self):
        assert String("hello").is_palindrome() is False

    def test_empty_is_palindrome(self):
        assert String("").is_palindrome() is True


class TestStringTransform:
    def test_reverse(self):
        result = String("hello").reverse()
        assert isinstance(result, String)
        assert str(result) == "olleh"

    def test_upper(self):
        result = String("hello").upper()
        assert isinstance(result, String)
        assert str(result) == "HELLO"

    def test_lower(self):
        result = String("HELLO").lower()
        assert isinstance(result, String)
        assert str(result) == "hello"

    def test_strip(self):
        result = String("  hello  ").strip()
        assert isinstance(result, String)
        assert str(result) == "hello"

    def test_strip_chars(self):
        result = String("xxhelloxx").strip("x")
        assert str(result) == "hello"

    def test_title_case(self):
        result = String("hello world").title_case()
        assert str(result) == "Hello World"

    def test_capitalize_first(self):
        result = String("hello").capitalize_first()
        assert str(result) == "Hello"

    def test_snake_case(self):
        assert str(String("helloWorld").snake_case()) == "hello_world"
        assert str(String("Hello World").snake_case()) == "hello_world"

    def test_camel_case(self):
        assert str(String("hello_world").camel_case()) == "helloWorld"
        assert str(String("Hello World").camel_case()) == "helloWorld"

    def test_kebab_case(self):
        assert str(String("helloWorld").kebab_case()) == "hello-world"

    def test_truncate(self):
        result = String("hello world").truncate(8)
        assert str(result) == "hello..."
        assert len(str(result)) == 8

    def test_truncate_no_need(self):
        result = String("hi").truncate(10)
        assert str(result) == "hi"


class TestStringSplitReplace:
    def test_split(self):
        result = String("hello world").split()
        assert isinstance(result, PyList)
        assert list(result) == ["hello", "world"]

    def test_split_sep(self):
        result = String("a,b,c").split(",")
        assert list(result) == ["a", "b", "c"]

    def test_replace(self):
        result = String("hello").replace("l", "x")
        assert isinstance(result, String)
        assert str(result) == "hexxo"

    def test_words(self):
        result = String("hello world foo").words()
        assert list(result) == ["hello", "world", "foo"]

    def test_lines(self):
        result = String("line1\nline2\nline3").lines()
        assert list(result) == ["line1", "line2", "line3"]


class TestStringCount:
    def test_count(self):
        assert String("hello").count("l") == 2
        assert String("hello").count("z") == 0

    def test_word_count(self):
        assert String("hello world foo").word_count() == 3
        assert String("").word_count() == 0

    def test_line_count(self):
        assert String("a\nb\nc").line_count() == 3
        assert String("").line_count() == 0


class TestStringConversions:
    def test_to_integer(self):
        result = String("123").to_integer()
        assert isinstance(result, Integer)
        assert int(result) == 123

    def test_to_integer_invalid(self):
        assert String("abc").to_integer() is None

    def test_to_float(self):
        result = String("3.14").to_float()
        assert isinstance(result, Float)
        assert abs(float(result) - 3.14) < 1e-9

    def test_to_float_invalid(self):
        assert String("abc").to_float() is None

    def test_to_boolean(self):
        assert String("hello").to_boolean().is_true()
        assert String("").to_boolean().is_false()

    def test_to_list(self):
        result = String("abc").to_list()
        assert isinstance(result, PyList)
        assert list(result) == ["a", "b", "c"]

    def test_append(self):
        result = String("hello").append(" world")
        assert isinstance(result, String)
        assert str(result) == "hello world"


class TestStringNativeOps:
    def test_concatenation(self):
        assert String("hello") + " " + String("world") == "hello world"

    def test_indexing(self):
        assert String("hello")[0] == "h"
        assert String("hello")[-1] == "o"

    def test_slicing(self):
        assert String("hello")[1:4] == "ell"

    def test_in(self):
        assert "ell" in String("hello")
