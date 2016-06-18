cdef extern from "Test.h":
    cdef cppclass Test:
        Test() except +
        int calc(int)

cdef class PyTest:
    cdef Test c_test      # hold a C++ instance which we're wrapping
    def __cinit__(self):
        self.c_test = Test()
    def calc(self, int x):
        return self.c_test.calc(x)
