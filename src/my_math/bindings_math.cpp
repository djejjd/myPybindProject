//
// Created by zhang on 2026/5/4.
//

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <random>
#include <iostream>
#include <vector>
#include <utility>
namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

int mul(int i, int j) {
    return i * j;
}

int sub(int i, int j) {
    return i - j;
}

std::vector<float> generate_random_numbers(size_t count, int min, int max)
{
    std::vector<float> vector;
    vector.reserve(count);

    // 随机数设备
    std::random_device rd;
    // 梅森旋转引擎   高质量伪随机数
    std::mt19937 gen(rd());
    // 均匀整数分布
    std::uniform_real_distribution<float> dis(min, max);

    for (size_t i = 0; i < count; i++)
    {
        vector.push_back(dis(gen));
    }


    return vector;
}

void print_float()
{
    auto numbers = generate_random_numbers(5, 0, 10);
    for (int n : numbers) std::cout << n << " ";

}

std::pair<double, double> find_min_max(const std::vector<float> &arr)
{
    if (arr.empty())
    {
        throw std::runtime_error("empty array");
    }

    double min = arr[0];
    double max = arr[0];

    for (size_t i = 1; i < arr.size(); i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
        }
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }

    return {min, max};

}


void init_math(py::module_ &m) {
    m.doc() = "pybind11 example plugin"; // 可选的模块文档字符串
    m.def("add", &add, "A function that adds two numbers");
    m.def("mul", &mul, "A function that muls two numbers");
    m.def("sub", &sub, "A function that subs two numbers");
    m.def("print_float", &print_float, "A function that print random nmbers");
    m.def("find_min_max", &find_min_max,"A function that find min & max");
}