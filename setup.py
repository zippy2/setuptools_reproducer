#!/usr/bin/env python3

from setuptools import setup, Extension, Command

c_modules = []

module = Extension('mod1',
                   sources = ['mod1.c', 'common.c'],
                   include_dirs = [ "." ])
module.extra_compile_args.extend(['-DVAL=12'])

c_modules.append(module)

module = Extension('mod2',
                   sources = ['mod2.c', 'common.c'],
                   include_dirs = [ "." ])
module.extra_compile_args.extend(['-DVAL=42'])

c_modules.append(module)

setup(name = 'reproducer',
      version = '0.0.1',
      ext_modules = c_modules,
      package_dir = {
          '': 'build'
      }
)
