# PybindProject

一个使用 **pybind11** 将 C++ 代码绑定到 Python 的 C++/Python 混合项目，提供高效的数学和几何运算功能。

## 项目概述

PybindProject 是一个演示如何使用 pybind11 为 C++ 库创建 Python 绑定的示例项目。该项目包含：

- **数学模块**：用 C++ 实现的基本数学运算（加法、乘法、减法、随机数生成）
- **点模块**：几何点处理和斐波那契数列计算
- **跨平台构建**：支持 CMake 和 Python setuptools 两种构建方式

## 主要特性

- 🚀 高性能 C++ 实现绑定到 Python
- 📦 通过 pip 轻松安装，使用 setuptools
- 🏗️ 支持 CMake 进行高级构建配置
- 🧪 完整的测试套件
- 🔧 现代 Python 打包，使用 pyproject.toml

## 项目结构

```
PybindProject/
├── CMakeLists.txt           # CMake 构建配置
├── pyproject.toml          # Python 项目元数据
├── setup.py                # pip 安装的设置脚本
├── include/                # C++ 头文件
│   └── my_math/
│       ├── bindings_main.h
│       ├── bindings_math.h
│       └── bindings_point.h
├── src/                    # C++ 源文件
│   └── my_math/
│       ├── bindings_main.cpp
│       ├── bindings_math.cpp
│       └── bindings_point.cpp
├── python/                 # Python 包
│   └── my_math/
│       └── __init__.py
├── tests/                  # 测试套件
│   └── my_math_test.py
└── .gitignore             # Git 忽略规则
```

## 功能模块详细说明

### 数学模块 (bindings_math)

提供基本的数学运算功能：

- `add(i, j)`: 整数加法运算
- `mul(i, j)`: 整数乘法运算
- `sub(i, j)`: 整数减法运算
- `generate_random_numbers(count, min, max)`: 生成指定数量的随机浮点数

### 点模块 (bindings_point)

提供几何点操作和数学计算：

- `fibonacci(n)`: 计算第 n 项斐波那契数列
- `Point` 类：二维点结构体
  - 构造函数：`Point(x=0.0, y=0.0)`
  - 方法：`distance_to_origin()` - 计算到原点的距离

## 系统要求

- Python 3.7+
- C++ 编译器 (GCC、Clang 或 MSVC)
- CMake 3.14+ (可选，用于 CMake 构建)
- pybind11 2.10+

## 安装方法

### 方法一：使用 pip（推荐）

```bash
pip install .
```

### 方法二：使用 CMake

```bash
mkdir build
cd build
cmake ..
make
```

## 使用示例

安装完成后，在 Python 中导入模块使用：

```python
import my_math

# 数学运算
result_add = my_math.add(5, 3)  # 返回 8
result_mul = my_math.mul(4, 7)  # 返回 28
result_sub = my_math.sub(10, 4) # 返回 6

# 生成随机数
random_nums = my_math.generate_random_numbers(5, 0, 10)
print(random_nums)  # 输出 5 个 0-10 之间的随机浮点数

# 斐波那契数列
fib_10 = my_math.fibonacci(10)  # 返回 55

# 点操作
point = my_math.Point(3.0, 4.0)
distance = point.distance_to_origin()  # 返回 5.0
```

## 构建与开发

### 使用 setuptools 构建（Python）

```bash
python setup.py build_ext --inplace
```

### 使用 CMake 构建

```bash
mkdir cmake-build-debug
cd cmake-build-debug
cmake ..
cmake --build .
```

## 测试

运行测试套件：

```bash
python -m pytest tests/
```

或直接运行测试文件：

```bash
python tests/my_math_test.py
```

## 依赖项

- **pybind11**: C++/Python 绑定库 (>= 2.10)
- **setuptools**: Python 打包工具
- **wheel**: 二进制分发包

## 支持平台

- ✅ macOS (Apple Silicon & Intel)
- ✅ Linux (GCC/Clang)
- ✅ Windows (MSVC)

## 作者

张 (Zhang)

## 许可证

[请添加您的许可证信息]

## 贡献指南

欢迎贡献！请遵循以下步骤：

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

## 故障排除

### 构建问题

如果遇到构建问题：

1. 确保 pybind11 已正确安装：`pip install pybind11`
2. 检查 C++ 编译器是否已安装并可访问
3. 对于 CMake 构建，验证 CMake 版本：`cmake --version`

### 导入错误

如果构建后出现导入错误：

1. 确保构建的扩展在 Python 路径中
2. 使用 `python setup.py build_ext --inplace` 重新构建（setuptools）
3. 验证 .so 文件（Windows 上为 .pyd）是否存在于模块目录中

## 参考资料

- [pybind11 文档](https://pybind11.readthedocs.io/)
- [pybind11 GitHub 仓库](https://github.com/pybind/pybind11)
- [CMake 文档](https://cmake.org/documentation/)
