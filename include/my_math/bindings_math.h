//
// Created by zhang on 2026/5/4.
//

#ifndef PYBINDPROJECT_EXAMPLE_H
#define PYBINDPROJECT_EXAMPLE_H

#include <pybind11/pybind11.h>
namespace py = pybind11;

class example {
};


void init_math(py::module_ &m);

#endif //PYBINDPROJECT_EXAMPLE_H
