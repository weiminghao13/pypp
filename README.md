# PyPP - Python Primitive Type Extensions

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://pypi.org/project/pypp/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-orange)](https://pypi.org/project/pypp/)

PyPP 是一个 Python 基础类型扩展库，为内置类型（`int`, `float`, `bool`, `str`, `list`）提供丰富的实用方法和类型转换功能。所有类型均正确继承自 Python 内置类型，支持原生运算和类型互操作。

## 特性

- **零依赖** — 纯 Python 实现，无需任何第三方库
- **原生兼容** — 继承自内置类型，可直接参与原生运算
- **类型安全** — 完整的类型注解，支持 IDE 智能提示
- **智能迭代器** — 根据数据规模自动选择最优实现
- **丰富方法** — 数论判断、文本处理、列表操作、类型转换

## 安装

```bash
pip install pypp-primitives
```

> 安装后使用 `import pypp` 导入模块。

## 快速开始

```python
from pypp import Integer, Float, Boolean, String, PyList
```

## Integer — 扩展整数

```python
num = Integer(42)

# 奇偶判断
num.is_even()        # True
num.is_odd()         # False

# 符号判断
num.is_positive()    # True
num.is_negative()    # False
num.is_zero()        # False

# 数论判断
Integer(17).is_prime()           # True
Integer(121).is_palindrome()     # True
Integer(16).is_perfect_square()  # True
Integer(27).is_perfect_cube()    # True
Integer(8).is_perfect_power(2)   # True (2^3)
Integer(153).is_armstrong()      # True

# 数学运算
Integer(5).factorial()    # 120
Integer(12345).digits()   # [1, 2, 3, 4, 5]
Integer(12345).digit_sum()   # 15
Integer(123).digit_product()  # 6

# 进制转换
Integer(255).to_binary()  # "11111111"
Integer(255).to_octal()   # "377"
Integer(255).to_hex()     # "ff"

# 原生运算（继承自 int）
Integer(3) + Integer(2)   # 5
Integer(3) * 4            # 12
```

## Float — 扩展浮点数

```python
f = Float(3.14)

f.is_positive()   # True
f.is_negative()   # False
f.is_zero()       # False
f.is_integer()    # False

# 特殊值判断
Float(float('nan')).is_nan()    # True
Float(float('inf')).is_inf()    # True
Float(3.14).is_finite()         # True

# 取整
Float(3.7).floor()      # Integer(3)
Float(3.2).ceil()       # Integer(4)
Float(3.14159).round_to(2)  # Float(3.14)
```

## Boolean — 扩展布尔值

```python
b = Boolean(True)

b.is_true()    # True
b.is_false()   # False
b.toggle()     # Boolean(False)

# 逻辑运算
Boolean(True) and Boolean(False)  # False
Boolean(False) or Boolean(True)   # True
```

## String — 扩展字符串

```python
s = String("Hello, World!")

# 基础判断
s.is_empty()        # False
s.is_palindrome()   # False
s.is_ascii()        # True
s.is_numeric()      # False
s.is_alpha()        # False

# 文本变换
s.reverse()              # String("!dlroW ,olleH")
s.upper()                # String("HELLO, WORLD!")
s.lower()                # String("hello, world!")
s.title_case()           # String("Hello, World!")
s.capitalize_first()     # String("Hello, World!")

# 命名风格转换
String("helloWorld").snake_case()    # String("hello_world")
String("hello_world").camel_case()   # String("helloWorld")
String("helloWorld").kebab_case()    # String("hello-world")

# 截断
String("hello world").truncate(8)    # String("hello...")

# 分割与统计
s.split()              # PyList(['Hello,', 'World!'])
s.words()              # PyList(['Hello,', 'World!'])
s.lines()              # 按行分割
s.count('l')           # 3
s.word_count()         # 2
s.length()             # 13

# 替换
s.replace('Hello', 'Hi')  # String("Hi, World!")

# 原生操作（继承自 str）
String("hello") + " " + String("world")  # "hello world"
String("hello")[0]                          # "h"
"ell" in String("hello")                    # True
```

## PyList — 扩展列表

```python
lst = PyList([3, 1, 4, 1, 5, 9, 2, 6])

# 基础
lst.is_empty()   # False

# 排序与反转
lst.sorted_list()           # PyList([1, 1, 2, 3, 4, 5, 6, 9])
lst.sorted_list(reverse=True)  # PyList([9, 6, 5, 4, 3, 2, 1, 1])
lst.reverse()               # PyList([6, 2, 9, 5, 1, 4, 1, 3])

# 集合操作
PyList([1, 2, 2, 3, 3, 3]).unique()   # PyList([1, 2, 3])
PyList([1, [2, 3], [4, [5]]]).flatten()  # PyList([1, 2, 3, 4, 5])
PyList([1, 2, 3, 4, 5]).chunk(2)      # PyList([[1,2], [3,4], [5]])

# 函数式操作
lst.map(lambda x: x * 2)               # 每个元素乘 2
lst.filter(lambda x: x % 2 == 0)       # 过滤偶数
lst.reduce(lambda x, y: x + y)         # 累加求和

# 统计
PyList([1, 2, 2, 3, 3, 3]).frequency()     # {1: 1, 2: 2, 3: 3}
PyList([1, 2, 2, 3, 3, 3]).most_common()   # PyList([3, 2, 1])

# 原生操作（继承自 list）
lst.append(7)
lst[0]
len(lst)
3 in lst
```

## 类型转换

所有类型都支持相互转换：

```python
# Integer → 其他
Integer(42).to_float()     # Float(42.0)
Integer(42).to_string()    # String("42")
Integer(42).to_boolean()   # Boolean(True)
Integer(123).to_list()     # PyList([1, 2, 3])

# String → 其他
String("123").to_integer()  # Integer(123)
String("3.14").to_float()   # Float(3.14)
String("hello").to_boolean() # Boolean(True)
String("abc").to_list()      # PyList(['a', 'b', 'c'])

# PyList → 其他
PyList([1, 2, 3]).to_string()        # String("123")
PyList([1, 2, 3]).to_integer_list()  # PyList([Integer(1), ...])
PyList([1, 2, 3]).to_float_list()    # PyList([Float(1.0), ...])
PyList([0, 1]).to_boolean_list()      # PyList([Boolean(False), Boolean(True)])
```

## 智能迭代器

PyPP 内置智能迭代器系统，根据数据规模自动选择最优实现：

```python
from pypp import auto_choose_iterator, is_small_data

# 小数据（< 阈值）：全量加载，支持索引/切片
small = auto_choose_iterator([1, 2, 3])  # SmartIterSmallData
small[0]  # 1
len(small)  # 3

# 大数据（≥ 阈值）或生成器：惰性加载，节省内存
gen = (x for x in range(10))
big = auto_choose_iterator(gen)  # SmartIterBigData
# 仅支持顺序遍历
for item in big:
    print(item)
```

**数据规模阈值：**

| 类型 | 阈值 |
|------|------|
| `list`, `tuple`, `set`, `frozenset` | 1,000,000 |
| `dict` | 1,000 |
| `str` | 10,000 |

## API 参考

### Integer

| 方法 | 说明 |
|------|------|
| `is_even()` | 判断是否为偶数 |
| `is_odd()` | 判断是否为奇数 |
| `is_positive()` | 判断是否为正数 |
| `is_negative()` | 判断是否为负数 |
| `is_zero()` | 判断是否为零 |
| `is_prime()` | 判断是否为质数 |
| `is_palindrome()` | 判断是否为回文数 |
| `is_perfect_square()` | 判断是否为完全平方数 |
| `is_perfect_cube()` | 判断是否为完全立方数 |
| `is_perfect_power(base)` | 判断是否为指定基数的完全幂 |
| `is_armstrong()` | 判断是否为阿姆斯特朗数 |
| `factorial()` | 计算阶乘 |
| `digits()` | 返回各位数字列表 |
| `digit_sum()` | 各位数字之和 |
| `digit_product()` | 各位数字之积 |
| `to_binary()` | 转换为二进制字符串 |
| `to_octal()` | 转换为八进制字符串 |
| `to_hex()` | 转换为十六进制字符串 |

### Float

| 方法 | 说明 |
|------|------|
| `is_positive()` | 判断是否为正数 |
| `is_negative()` | 判断是否为负数 |
| `is_zero()` | 判断是否为零 |
| `is_integer()` | 判断是否为整数值 |
| `is_nan()` | 判断是否为 NaN |
| `is_inf()` | 判断是否为无穷大 |
| `is_finite()` | 判断是否为有限值 |
| `floor()` | 向下取整 → Integer |
| `ceil()` | 向上取整 → Integer |
| `round_to(ndigits)` | 四舍五入到指定小数位 |

### Boolean

| 方法 | 说明 |
|------|------|
| `is_true()` | 判断是否为 True |
| `is_false()` | 判断是否为 False |
| `toggle()` | 取反 |

### String

| 方法 | 说明 |
|------|------|
| `is_empty()` | 判断是否为空字符串 |
| `is_palindrome()` | 判断是否为回文串 |
| `is_ascii()` | 检查是否只含 ASCII 字符 |
| `all_char(char)` | 检查是否只含指定字符 |
| `is_numeric()` | 判断是否为纯数字 |
| `is_alpha()` | 判断是否为纯字母 |
| `is_alphanumeric()` | 判断是否为字母数字 |
| `reverse()` | 反转字符串 |
| `upper()` / `lower()` | 大小写转换 |
| `strip(chars)` | 移除首尾字符 |
| `title_case()` | 标题格式 |
| `capitalize_first()` | 首字母大写 |
| `snake_case()` | 下划线命名 |
| `camel_case()` | 驼峰命名 |
| `kebab_case()` | 短横线命名 |
| `truncate(length, suffix)` | 截断字符串 |
| `split(sep)` | 分割 → PyList |
| `replace(old, new)` | 替换内容 |
| `words()` | 提取单词列表 |
| `lines()` | 按行分割 |
| `count(sub)` | 统计子串次数 |
| `length()` | 返回长度 |
| `word_count()` | 单词数量 |
| `line_count()` | 行数 |
| `append(value)` | 拼接字符串 |

### PyList

| 方法 | 说明 |
|------|------|
| `is_empty()` | 判断是否为空列表 |
| `to_string()` | 拼接为字符串 |
| `to_integer_list()` | 转换为整数列表 |
| `to_float_list()` | 转换为浮点数列表 |
| `to_boolean_list()` | 转换为布尔值列表 |
| `sorted_list(key, reverse)` | 返回排序后的新列表 |
| `reverse()` | 返回反转后的新列表 |
| `unique()` | 去重（保持顺序） |
| `flatten()` | 扁平化嵌套列表 |
| `chunk(size)` | 按大小分块 |
| `map(func)` | 对每个元素应用函数 |
| `filter(func)` | 按条件过滤 |
| `reduce(func, initial)` | 累积归约 |
| `frequency()` | 元素出现频率 |
| `most_common(n)` | 出现次数最多的元素 |
| `to_smart_iter()` | 转换为智能迭代器 |

## 开发

```bash
# 克隆项目
git clone https://github.com/yourusername/pypp.git
cd pypp

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 构建
python -m build

# 发布
twine upload dist/*
```

## 许可证

MIT License — 详见 [LICENSE](LICENSE) 文件。

## 作者

Hao Hao
