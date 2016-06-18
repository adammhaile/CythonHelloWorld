from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules = cythonize(
           "main.pyx",                 # our Cython source
           sources=["Test.cpp"],  # additional source file(s)
           language="c++",             # generate C++ code
      ))
