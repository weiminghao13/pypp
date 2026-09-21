"""
PyPP - Python Primitive Type Extensions

为 Python 内置类型（int, float, bool, str, list）提供丰富的实用方法和类型转换功能。
所有类型均正确继承自内置类型，支持原生运算和类型互操作。
"""

from __future__ import annotations

import math
from typing import Any, Callable, Iterable, Optional, Union

from .iter_object import SmartIterBigData, SmartIterSmallData, auto_choose_iterator, is_small_data


class Integer(int):
    """扩展整数类型，提供丰富的数学判断和转换方法。

    继承自内置 int，支持所有原生整数运算。
    """

    def __new__(cls, value: Union[int, float, str, bytes, None] = 0) -> "Integer":
        try:
            return super().__new__(cls, value if value is not None else 0)
        except (TypeError, ValueError):
            return super().__new__(cls, 0)

    def __repr__(self) -> str:
        return f"Integer({int(self)})"

    def __str__(self) -> str:
        return str(int(self))

    # ---- 奇偶判断 ----
    def is_even(self) -> bool:
        """判断是否为偶数。"""
        return self % 2 == 0

    def is_odd(self) -> bool:
        """判断是否为奇数。"""
        return self % 2 != 0

    # ---- 符号判断 ----
    def is_positive(self) -> bool:
        """判断是否为正数。"""
        return self > 0

    def is_negative(self) -> bool:
        """判断是否为负数。"""
        return self < 0

    def is_zero(self) -> bool:
        """判断是否为零。"""
        return self == 0

    # ---- 数论判断 ----
    def is_prime(self) -> bool:
        """判断是否为质数（素数）。"""
        n = int(self)
        if n < 2:
            return False
        if n < 4:
            return True
        if n % 2 == 0:
            return False
        return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))

    def is_palindrome(self) -> bool:
        """判断是否为回文数。"""
        s = str(abs(int(self)))
        return s == s[::-1]

    def is_perfect_square(self) -> bool:
        """判断是否为完全平方数。"""
        n = int(self)
        if n < 0:
            return False
        root = math.isqrt(n)
        return root * root == n

    def is_perfect_cube(self) -> bool:
        """判断是否为完全立方数。"""
        n = int(self)
        if n < 0:
            root = round((-n) ** (1 / 3))
            return -(root**3) == n
        root = round(n ** (1 / 3))
        return root**3 == n

    def is_perfect_power(self, base: int) -> bool:
        """判断是否为指定基数的完全幂（即 self == base^k，k为正整数）。"""
        if base <= 1:
            return False
        n = int(self)
        if n < 0:
            return False
        if n == 1:
            return True
        result = 1
        while result < n:
            result *= base
        return result == n

    def is_armstrong(self) -> bool:
        """判断是否为阿姆斯特朗数（自幂数）。"""
        n = int(self)
        if n < 0:
            return False
        s = str(n)
        power = len(s)
        return sum(int(d) ** power for d in s) == n

    # ---- 数学运算 ----
    def factorial(self) -> int:
        """计算阶乘。"""
        n = int(self)
        if n < 0:
            raise ValueError("factorial() not defined for negative numbers")
        return math.factorial(n)

    def digits(self) -> list[int]:
        """返回各位数字组成的列表。"""
        n = abs(int(self))
        return [int(d) for d in str(n)]

    def digit_sum(self) -> int:
        """计算各位数字之和。"""
        return sum(self.digits())

    def digit_product(self) -> int:
        """计算各位数字之积。"""
        result = 1
        for d in self.digits():
            result *= d
        return result

    # ---- 进制转换 ----
    def to_binary(self) -> str:
        """转换为二进制字符串（不带 0b 前缀）。"""
        return bin(int(self))[2:]

    def to_octal(self) -> str:
        """转换为八进制字符串（不带 0o 前缀）。"""
        return oct(int(self))[2:]

    def to_hex(self) -> str:
        """转换为十六进制字符串（不带 0x 前缀，小写）。"""
        return hex(int(self))[2:]

    # ---- 类型转换 ----
    def to_integer(self) -> "Integer":
        return Integer(int(self))

    def to_float(self) -> "Float":
        return Float(float(self))

    def to_string(self) -> "String":
        return String(str(int(self)))

    def to_boolean(self) -> "Boolean":
        return Boolean(bool(self))

    def to_list(self) -> "PyList":
        """将各位数字转换为列表。"""
        return PyList(self.digits())

    def show(self) -> None:
        """打印值。"""
        print(int(self))


class Float(float):
    """扩展浮点数类型，提供数值判断和转换方法。

    继承自内置 float，支持所有原生浮点运算。
    """

    def __new__(cls, value: Union[int, float, str, None] = 0.0) -> "Float":
        try:
            return super().__new__(cls, value if value is not None else 0.0)
        except (TypeError, ValueError):
            return super().__new__(cls, 0.0)

    def __repr__(self) -> str:
        return f"Float({float(self)})"

    def __str__(self) -> str:
        return str(float(self))

    # ---- 符号判断 ----
    def is_positive(self) -> bool:
        """判断是否为正数。"""
        return self > 0

    def is_negative(self) -> bool:
        """判断是否为负数。"""
        return self < 0

    def is_zero(self) -> bool:
        """判断是否为零。"""
        return self == 0

    def is_integer(self) -> bool:
        """判断是否为整数值（如 3.0）。"""
        return float(self).is_integer()

    def is_nan(self) -> bool:
        """判断是否为 NaN。"""
        return math.isnan(float(self))

    def is_inf(self) -> bool:
        """判断是否为无穷大。"""
        return math.isinf(float(self))

    def is_finite(self) -> bool:
        """判断是否为有限值。"""
        return math.isfinite(float(self))

    # ---- 取整 ----
    def floor(self) -> Integer:
        """向下取整。"""
        return Integer(math.floor(float(self)))

    def ceil(self) -> Integer:
        """向上取整。"""
        return Integer(math.ceil(float(self)))

    def round_to(self, ndigits: int = 0) -> "Float":
        """四舍五入到指定小数位。"""
        return Float(round(float(self), ndigits))

    # ---- 类型转换 ----
    def to_integer(self) -> Integer:
        return Integer(int(float(self)))

    def to_float(self) -> "Float":
        return Float(float(self))

    def to_string(self) -> "String":
        return String(str(float(self)))

    def to_boolean(self) -> "Boolean":
        return Boolean(bool(self))

    def to_list(self) -> "PyList":
        raise TypeError("Float object cannot be converted to list")

    def show(self) -> None:
        """打印值。"""
        print(float(self))


class Boolean(int):
    """扩展布尔类型，提供逻辑判断和转换方法。

    由于 Python 中 bool 不可被继承，此类继承自 int，
    但行为严格遵循布尔语义。
    """

    def __new__(cls, value: Any = False) -> "Boolean":
        return super().__new__(cls, 1 if bool(value) else 0)

    def __repr__(self) -> str:
        return f"Boolean({bool(self)})"

    def __str__(self) -> str:
        return str(bool(self))

    def __bool__(self) -> bool:
        return int(self) != 0

    # ---- 判断 ----
    def is_true(self) -> bool:
        """判断是否为 True。"""
        return bool(self)

    def is_false(self) -> bool:
        """判断是否为 False。"""
        return not bool(self)

    # ---- 逻辑运算 ----
    def toggle(self) -> "Boolean":
        """取反。"""
        return Boolean(not bool(self))

    # ---- 类型转换 ----
    def to_string(self) -> "String":
        return String(str(bool(self)))

    def to_integer(self) -> Integer:
        return Integer(int(self))

    def to_float(self) -> Float:
        return Float(float(self))

    def to_list(self) -> "PyList":
        raise TypeError("Boolean object cannot be converted to list")

    def show(self) -> None:
        """打印值。"""
        print(bool(self))


class String(str):
    """扩展字符串类型，提供丰富的文本处理和转换方法。

    继承自内置 str，支持所有原生字符串操作。
    """

    def __new__(cls, value: Any = "") -> "String":
        if value is None:
            return super().__new__(cls, "")
        return super().__new__(cls, str(value))

    def __repr__(self) -> str:
        return f"String({str.__repr__(self)})"

    def __str__(self) -> str:
        return str.__str__(self)

    # ---- 基础判断 ----
    def is_empty(self) -> bool:
        """判断是否为空字符串。"""
        return len(self) == 0

    def is_palindrome(self) -> bool:
        """判断是否为回文字符串（忽略大小写和空白）。"""
        cleaned = "".join(c.lower() for c in self if c.isalnum())
        return cleaned == cleaned[::-1]

    def is_ascii(self) -> bool:
        """检查是否只包含 ASCII 字符。"""
        return all(ord(c) < 128 for c in self)

    def all_char(self, char: str) -> bool:
        """检查是否只包含指定字符。"""
        if len(self) == 0:
            return False
        return all(c == char for c in self)

    def is_numeric(self) -> bool:
        """判断是否为纯数字字符串。"""
        return str.isdigit(self)

    def is_alpha(self) -> bool:
        """判断是否为纯字母字符串。"""
        return str.isalpha(self)

    def is_alphanumeric(self) -> bool:
        """判断是否为字母数字混合字符串。"""
        return str.isalnum(self)

    # ---- 变换 ----
    def reverse(self) -> "String":
        """反转字符串。"""
        return String(self[::-1])

    def upper(self) -> "String":  # type: ignore[override]
        """转换为大写。"""
        return String(str.upper(self))

    def lower(self) -> "String":  # type: ignore[override]
        """转换为小写。"""
        return String(str.lower(self))

    def strip(self, chars: Optional[str] = None) -> "String":  # type: ignore[override]
        """移除首尾指定字符。"""
        return String(str.strip(self, chars) if chars else str.strip(self))

    def title_case(self) -> "String":
        """转换为标题格式（每个单词首字母大写）。"""
        return String(str.title(self))

    def capitalize_first(self) -> "String":
        """首字母大写。"""
        if len(self) == 0:
            return String("")
        return String(self[0].upper() + self[1:])

    def snake_case(self) -> "String":
        """转换为 snake_case（下划线命名）。"""
        result = []
        for i, c in enumerate(str(self)):
            if c.isupper() and i > 0 and result[-1] != "_":
                result.append("_")
            result.append(c.lower())
        # 将空格和短横线替换为下划线，合并连续下划线
        text = "".join(result).replace(" ", "_").replace("-", "_")
        while "__" in text:
            text = text.replace("__", "_")
        return String(text.strip("_"))

    def camel_case(self) -> "String":
        """转换为 camelCase（驼峰命名）。"""
        words = self.replace("_", " ").replace("-", " ").split()
        if not words:
            return String("")
        return String(words[0].lower() + "".join(w.capitalize() for w in words[1:]))

    def kebab_case(self) -> "String":
        """转换为 kebab-case（短横线命名）。"""
        return String(self.snake_case().replace("_", "-"))

    def truncate(self, length: int, suffix: str = "...") -> "String":
        """截断字符串到指定长度，添加后缀。"""
        if len(self) <= length:
            return String(str(self))
        return String(self[: length - len(suffix)] + suffix)

    # ---- 分割与替换 ----
    def split(self, sep: Optional[str] = None, maxsplit: int = -1) -> "PyList":  # type: ignore[override]
        """分割字符串为 PyList。"""
        return PyList(str.split(self, sep, maxsplit))

    def replace(self, old: str, new: str, count: int = -1) -> "String":  # type: ignore[override]
        """替换字符串中的指定内容。"""
        return String(str.replace(self, old, new, count))

    def words(self) -> "PyList":
        """提取所有单词。"""
        return PyList(str.split(self))

    def lines(self) -> "PyList":
        """按行分割。"""
        return PyList(str.splitlines(self))

    # ---- 统计 ----
    def count(self, sub: str, start: int = 0, end: Optional[int] = None) -> int:  # type: ignore[override]
        """统计子字符串出现次数。"""
        if end is None:
            return str.count(self, sub, start)
        return str.count(self, sub, start, end)

    def length(self) -> int:
        """返回字符串长度。"""
        return len(self)

    def word_count(self) -> int:
        """统计单词数量。"""
        return len(str.split(self))

    def line_count(self) -> int:
        """统计行数。"""
        return len(str.splitlines(self)) if self else 0

    # ---- 类型转换 ----
    def to_string(self) -> "String":
        return String(str(self))

    def to_integer(self) -> Optional[Integer]:
        """转换为整数，失败返回 None。"""
        try:
            return Integer(int(str(self)))
        except (ValueError, TypeError):
            return None

    def to_float(self) -> Optional[Float]:
        """转换为浮点数，失败返回 None。"""
        try:
            return Float(float(str(self)))
        except (ValueError, TypeError):
            return None

    def to_boolean(self) -> Boolean:
        """转换为布尔值，空字符串返回 False。"""
        return Boolean(bool(self))

    def to_list(self) -> "PyList":
        """将每个字符转换为列表元素。"""
        return PyList(list(self))

    def append(self, value: str) -> "String":
        """拼接字符串（返回新对象，字符串不可变）。"""
        return String(str(self) + str(value))

    def show(self) -> None:
        """打印值。"""
        print(str(self))


class PyList(list):
    """扩展列表类型，提供丰富的列表操作和类型转换方法。

    继承自内置 list，支持所有原生列表操作。
    内置智能迭代器系统，根据数据规模自动选择最优实现。
    """

    def __init__(self, value: Optional[Iterable] = None) -> None:
        if value is None:
            super().__init__()
        elif isinstance(value, (SmartIterSmallData, SmartIterBigData)):
            super().__init__(list(value))
        else:
            super().__init__(value)

    def __repr__(self) -> str:
        return f"PyList({list.__repr__(self)})"

    def __str__(self) -> str:
        return list.__repr__(self)

    # ---- 基础判断 ----
    def is_empty(self) -> bool:
        """判断是否为空列表。"""
        return len(self) == 0

    # ---- 类型转换 ----
    def to_string(self) -> String:
        """将所有元素拼接为字符串。"""
        return String("".join(str(item) for item in self))

    def to_integer_list(self) -> Optional["PyList"]:
        """转换为整数列表，任一元素无法转换时返回 None。"""
        try:
            converted = [int(item) for item in self]
        except (ValueError, TypeError):
            return None
        return PyList([Integer(x) for x in converted])

    def to_float_list(self) -> Optional["PyList"]:
        """转换为浮点数列表，任一元素无法转换时返回 None。"""
        try:
            converted = [float(item) for item in self]
        except (ValueError, TypeError):
            return None
        return PyList([Float(x) for x in converted])

    def to_boolean_list(self) -> "PyList":
        """转换为布尔值列表。"""
        return PyList([Boolean(item) for item in self])

    def to_list(self) -> "PyList":
        """返回新的 PyList 副本。"""
        return PyList(list(self))

    # ---- 排序与反转 ----
    def sorted_list(self, key: Optional[Callable[[Any], Any]] = None, reverse: bool = False) -> "PyList":
        """返回排序后的新列表。"""
        return PyList(sorted(self, key=key, reverse=reverse))

    def reverse(self) -> "PyList":  # type: ignore[override]
        """返回反转后的新列表。"""
        return PyList(self[::-1])

    # ---- 集合操作 ----
    def unique(self) -> "PyList":
        """去重，保持原有顺序。"""
        seen = set()
        result = []
        for item in self:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return PyList(result)

    def flatten(self) -> "PyList":
        """扁平化嵌套列表。"""
        result = []
        for item in self:
            if isinstance(item, (list, tuple, PyList)):
                result.extend(PyList(item).flatten())
            else:
                result.append(item)
        return PyList(result)

    def chunk(self, size: int) -> "PyList":
        """按指定大小分块。"""
        if size <= 0:
            raise ValueError("chunk size must be positive")
        return PyList([PyList(self[i : i + size]) for i in range(0, len(self), size)])

    # ---- 函数式操作 ----
    def map(self, func: Callable[[Any], Any]) -> "PyList":
        """对每个元素应用函数。"""
        return PyList([func(item) for item in self])

    def filter(self, func: Callable[[Any], bool]) -> "PyList":
        """按条件过滤元素。"""
        return PyList([item for item in self if func(item)])

    def reduce(self, func: Callable[[Any, Any], Any], initial: Optional[Any] = None) -> Any:
        """累积归约。"""
        if initial is not None:
            result = initial
            items = self
        else:
            if len(self) == 0:
                raise TypeError("reduce() of empty sequence with no initial value")
            result = self[0]
            items = self[1:]
        for item in items:
            result = func(result, item)
        return result

    # ---- 统计 ----
    def frequency(self) -> dict[Any, int]:
        """统计每个元素出现次数。"""
        result: dict[Any, int] = {}
        for item in self:
            result[item] = result.get(item, 0) + 1
        return result

    def most_common(self, n: Optional[int] = None) -> "PyList":
        """返回出现次数最多的元素列表。"""
        freq = self.frequency()
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        if n is not None:
            sorted_items = sorted_items[:n]
        return PyList([item for item, _ in sorted_items])

    # ---- 智能迭代器 ----
    def to_smart_iter(self):
        """根据数据规模自动选择最优迭代器。"""
        return auto_choose_iterator(list(self))

    def show(self) -> None:
        """打印列表内容。"""
        print(list(self))
