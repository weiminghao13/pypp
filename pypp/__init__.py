"""
PyPP - Python Primitive Type Extensions

为 Python 内置类型提供丰富的实用方法和类型转换功能。
"""

from .core import Boolean, Float, Integer, PyList, String
from .iter_object import SmartIterBigData, SmartIterSmallData, auto_choose_iterator, is_small_data

__version__ = "1.0.0"
__author__ = "Hao Hao"

__all__ = [
    "Integer",
    "Float",
    "Boolean",
    "String",
    "PyList",
    "SmartIterSmallData",
    "SmartIterBigData",
    "auto_choose_iterator",
    "is_small_data",
    "__version__",
]
