# PybindProject

A C++/Python hybrid project that binds C++ code to Python using **pybind11**, providing efficient mathematical and geometric operations.

## Overview

PybindProject is a demonstration of how to create Python bindings for C++ libraries using pybind11. The project includes:

- **Math Module**: Mathematical operations implemented in C++
- **Point Module**: Geometric point handling and operations
- **Cross-platform Building**: Supports both CMake and Python setuptools for flexible building

## Features

- 🚀 High-performance C++ implementation bound to Python
- 📦 Easy installation via pip with setuptools
- 🏗️ CMake support for advanced build configurations
- 🧪 Comprehensive test suite
- 🔧 Modern Python packaging with pyproject.toml

## Project Structure

```
PybindProject/
├── CMakeLists.txt           # CMake build configuration
├── pyproject.toml          # Python project metadata
├── setup.py                # Setup script for pip installation
├── include/                # C++ header files
│   └── my_math/
│       ├── bindings_main.h
│       ├── bindings_math.h
│       └── bindings_point.h
├── src/                    # C++ source files
│   └── my_math/
│       ├── bindings_main.cpp
│       ├── bindings_math.cpp
│       └── bindings_point.cpp
├── python/                 # Python package
│   └── my_math/
│       └── __init__.py
├── tests/                  # Test suite
│   └── my_math_test.py
└── .gitignore             # Git ignore rules
```

## Requirements

- Python 3.7+
- C++ compiler (GCC, Clang, or MSVC)
- CMake 3.14+ (optional, for CMake builds)
- pybind11 2.10+

## Installation

### Option 1: Using pip (Recommended)

```bash
pip install .
```

### Option 2: Using CMake

```bash
mkdir build
cd build
cmake ..
make
```

## Usage

After installation, import the module in Python:

```python
import my_math

# Use the math module
# Example usage would go here based on your implementation

# Use the point module
# Example usage would go here based on your implementation
```

## Building & Development

### Build with setuptools (Python)

```bash
python setup.py build_ext --inplace
```

### Build with CMake

```bash
mkdir cmake-build-debug
cd cmake-build-debug
cmake ..
cmake --build .
```

## Testing

Run the test suite:

```bash
python -m pytest tests/
```

Or run the individual test file:

```bash
python tests/my_math_test.py
```

## Dependencies

- **pybind11**: For C++/Python bindings (>= 2.10)
- **setuptools**: For Python packaging
- **wheel**: For binary distribution

## Platform Support

- ✅ macOS (Apple Silicon & Intel)
- ✅ Linux (GCC/Clang)
- ✅ Windows (MSVC)

## Author

Created by Zhang

## License

[Add your license here]

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Build Issues

If you encounter build issues:

1. Ensure pybind11 is properly installed: `pip install pybind11`
2. Check that your C++ compiler is installed and accessible
3. For CMake builds, verify CMake version: `cmake --version`

### Import Errors

If you get import errors after building:

1. Make sure the built extension is in your Python path
2. Rebuild with `python setup.py build_ext --inplace` (for setuptools)
3. Verify the .so (or .pyd on Windows) file exists in the module directory

## References

- [pybind11 Documentation](https://pybind11.readthedocs.io/)
- [pybind11 GitHub Repository](https://github.com/pybind/pybind11)
- [CMake Documentation](https://cmake.org/documentation/)
