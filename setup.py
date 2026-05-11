from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension("my_math",
                      ["src/my_math/bindings_math.cpp",
                       "src/my_math/bindings_point.cpp",
                       "src/my_math/bindings_main.cpp"]),
]

setup(
    name="my_math",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)