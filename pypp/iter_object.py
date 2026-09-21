"""
PyPP 智能迭代器模块

根据数据规模自动选择最优迭代器实现：
- 小数据场景：使用 SmartIterSmallData（全量加载，支持索引/切片/随机访问）
- 大数据场景：使用 SmartIterBigData（惰性加载，仅支持顺序遍历，节省内存）
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any, Generic, List, TypeVar

T = TypeVar("T")

# 不同类型的数据规模阈值（小于阈值为小数据）
_THRESHOLDS: dict[type, int] = {
    list: 1_000_000,
    tuple: 1_000_000,
    set: 1_000_000,
    frozenset: 1_000_000,
    dict: 1_000,
    str: 10_000,
}
_DEFAULT_THRESHOLD = 1_000_000


def is_small_data(value: Any) -> bool:
    """判断是否为「小数据」（可全量加载且规模在阈值内）。

    判断规则：
    1. 非可迭代对象 → False
    2. 不支持 len() → False（如生成器、文件对象）
    3. 空可迭代对象 → True
    4. 支持的类型按长度阈值判断
    """
    if not isinstance(value, Iterable):
        return False

    # 生成器/迭代器等不支持 len() 的对象 → 大数据
    try:
        length = len(value)
    except TypeError:
        return False

    # 空数据 → 小数据
    if length == 0:
        return True

    threshold = _THRESHOLDS.get(type(value), _DEFAULT_THRESHOLD)
    return length < threshold


def auto_choose_iterator(iterable: Iterable[T]) -> "SmartIterSmallData[T] | SmartIterBigData[T]":
    """根据数据规模自动选择最优迭代器。"""
    if is_small_data(iterable):
        return SmartIterSmallData(iterable)
    return SmartIterBigData(iterable)


class SmartIterSmallData(Iterator[T], Generic[T]):
    """小数据迭代器：全量加载到列表，支持索引、切片、随机访问和修改。

    适用于数据量较小、需要频繁随机访问或修改的场景。
    """

    def __init__(self, value: Iterable[T]) -> None:
        if not isinstance(value, Iterable):
            raise TypeError(f"{type(value).__name__} object is not iterable")
        self.data: List[T] = list(value)
        self._cursor = 0

    def __next__(self) -> T:
        if self._cursor < len(self.data):
            item = self.data[self._cursor]
            self._cursor += 1
            return item
        raise StopIteration

    def __iter__(self) -> "SmartIterSmallData[T]":
        return self

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int | slice) -> T | List[T]:
        return self.data[index]

    def __setitem__(self, index: int, value: T) -> None:
        self.data[index] = value

    def __repr__(self) -> str:
        return f"SmartIterSmallData({self.data!r})"

    def reset(self) -> None:
        """重置迭代游标到起始位置。"""
        self._cursor = 0

    def change(self, index: int, value: T) -> None:
        """修改指定位置的元素。"""
        self.data[index] = value

    def append(self, value: T) -> None:
        """追加元素。"""
        self.data.append(value)

    def to_list(self) -> List[T]:
        """转换为普通列表。"""
        return list(self.data)


class SmartIterBigData(Iterator[T], Generic[T]):
    """大数据迭代器：惰性加载，仅支持顺序遍历，节省内存。

    适用于数据量巨大、只需顺序遍历一次的场景。
    不支持 len()、索引访问和随机访问。
    """

    def __init__(self, iterable: Iterable[T]) -> None:
        if not isinstance(iterable, Iterable):
            raise TypeError(f"{type(iterable).__name__} object is not iterable")
        self._iterable = iterable
        self._iterator: Iterator[T] = iter(iterable)

    def __next__(self) -> T:
        try:
            return next(self._iterator)
        except StopIteration:
            self.reset()
            raise

    def __iter__(self) -> "SmartIterBigData[T]":
        return self

    def __repr__(self) -> str:
        return f"SmartIterBigData({self._iterable!r})"

    def reset(self) -> None:
        """重置迭代器到起始位置。"""
        self._iterator = iter(self._iterable)

    def __len__(self) -> int:
        raise TypeError("SmartIterBigData does not support len()")

    def __getitem__(self, index: int) -> T:
        raise NotImplementedError("Index access is not supported for SmartIterBigData")
