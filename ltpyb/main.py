#! /usr/bin/env python
# -*- coding: utf-8 -*-
# >>
#     LTPyB, 2016
# <<

from rpython.rlib.streamio import open_file_as_stream

from ltpyb.sourceparser import source_to_ast
from ltpyb.bytecode import compile_ast
from ltpyb.interpreter import Interpreter

import os


def ast(source):
    return source_to_ast(source)


def ast_to_bytecode(ast, filename):
    filename = unicode(os.path.abspath(filename))
    return compile_ast(ast, ast.scope, filename)


def bytecode(filename, source):
    source = ast(source)
    return ast_to_bytecode(source, filename)


def interpret(bc):
    intrepreter = Interpreter()
    intrepreter.run(bc)


def read_file(filename):
    f = open_file_as_stream(filename)
    data = f.readall()
    f.close()
    return data


def run(filename, source):
    bc = bytecode(filename, source)
    interpret(bc)
    return 0


def main():
    filename = 'test_program.pybas'

    print_bytecode = False
    print_ast = False

    source = read_file(filename)

    if print_ast:
        print ast(source).str()
        return 0

    elif print_bytecode:
        print bytecode(filename, source).str()
        return 0

    else:
        return run(filename, source)


if __name__ == '__main__':
    main()
