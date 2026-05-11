//
// Created by zhang on 2026/5/6.
//
#include "../../include/my_math/bindings_point.h"
#include "../../include/my_math/bindings_math.h"
#include "../../include/my_math/bindings_main.h"

namespace py = pybind11;

PYBIND11_MODULE(my_math, m) {        // 仅在这里定义模块
    m.doc() = "My math module";

    init_math(m);    // 将数学功能注册到模块中
    init_point(m);   // 将点功能注册到模块中
}