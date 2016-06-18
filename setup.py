import setuptools.extension, Cython.Build
from setuptools.command.build_ext import build_ext as _build_ext

import Cython.Compiler.Options

COMPILE_ARGS = [
    '-DNDEBUG',
    '-DWINDOWS',
    '/Dand=&&',
    '/Dnot=!',
    '/Dor=||',
    '/Duint=size_t',
    ]

class build_ext(_build_ext):
    # See https://groups.google.com/forum/#!topic/cython-users/IZMENRz6__s
    def finalize_options(self):
        extension = setuptools.extension.Extension(
            name='main',
            sources=['main.pyx'],
            #libraries=LIBRARIES,
            #include_dirs=['src'],
            extra_compile_args=COMPILE_ARGS,
            language='c++',
            )

        module = Cython.Build.cythonize(
            [extension],
            language='c++',
            language_level=3,

            compiler_directives=dict(
                c_string_encoding='ascii',
                # c_string_type='unicode', # Why doesn't this work?
                )
            )
        self.distribution.ext_modules = module
        super(build_ext, self).finalize_options()

# setup(ext_modules = cythonize(
#            "main.pyx",                 # our Cython source
#            sources=["Test.h"],  # additional source file(s)
#            language="c++",             # generate C++ code
#            extra_compile_args=COMPILE_ARGS
#            cmdclass={
#                'build_ext': build_ext,
#                'clean': Clean,
#                'generate': Generate,
#                'local': Local,
#                },
#       ))

setuptools.setup(
    #name='test',
    cmdclass={
        'build_ext': build_ext,
        },
    )
