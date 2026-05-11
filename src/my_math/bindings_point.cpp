//
// Created by zhang on 2026/5/4.
//

#include "../../include/my_math/bindings_point.h"

#include <pybind11/pybind11.h>
#include <string>

namespace py = pybind11;

// ---------- 纯 C 函数：计算斐波那契数列 ----------
int fibonacci(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    int a = 0, b = 1;
    for (int i = 2; i <= n; ++i) {
        int c = a + b;
        a = b;
        b = c;
    }
    return b;
}

// ---------- 纯 C 风格的结构体 ----------
struct Point {
    double x, y;

    // 为了方便，添加一个构造函数（纯 C 中通常用初始化函数，这里简化）
    Point(double x_ = 0.0, double y_ = 0.0) : x(x_), y(y_) {}

    // 一个简单的成员函数
    double distance_to_origin() const {
        return std::sqrt(x * x + y * y);
    }
};

// ---------- 绑定 ----------
void init_point(py::module_ &m) {          // 模块名 "my_math"
    m.doc() = "示例模块：斐波那契和点结构体";

    // 1. 绑定纯函数
    m.def("fibonacci", &fibonacci, "计算第 n 项斐波那契数",
          py::arg("n"));

    // 2. 绑定结构体 Point
    py::class_<Point>(m, "Point")
        .def(py::init<double, double>(),   // 构造函数参数：x, y
             py::arg("x") = 0.0,           // 默认参数
             py::arg("y") = 0.0)
        .def_readwrite("x", &Point::x, "X 坐标")    // 暴露成员变量（可读写）
        .def_readwrite("y", &Point::y, "Y 坐标")
        .def("distance_to_origin", &Point::distance_to_origin,
             "计算点到原点的距离")
        .def("__repr__", [](const Point &p) {       // 让打印更好看
            return "Point(x=" + std::to_string(p.x) +
                   ", y=" + std::to_string(p.y) + ")";
        });
}