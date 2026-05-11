cmake_minimum_required(VERSION 3.14)
project(my_math)

set(pybind11_DIR "/Users/lanser/miniconda3/envs/pybindproject/lib/python3.13/site-packages/pybind11/share/cmake/pybind11")
find_package(pybind11 REQUIRED)

pybind11_add_module(my_math
        src/my_math/bindings_point.cpp
        src/my_math/bindings_math.cpp
        src/my_math/bindings_main.cpp)
add_executable(new_target src/my_math/bindings_math.cpp
        src/my_math/bindings_math.h
        src/my_math/bindings_point.cpp
        src/my_math/bindings_point.h
        src/my_math/bindings_main.cpp
        src/my_math/bindings_main.h)
