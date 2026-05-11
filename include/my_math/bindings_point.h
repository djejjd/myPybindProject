//
// Created by zhang on 2026/5/4.
//

#ifndef EXAMPLE_BINDINGS_H
#define EXAMPLE_BINDINGS_H

#include <pybind11/pybind11.h>
namespace py = pybind11;

class bindings
{
};

void init_point(py::module_ &m);

#endif //EXAMPLE_BINDINGS_H
