#! /usr/bin/env python
# -*- coding: utf-8 -*-
# >>
#     LTPyB, 2016
# <<

import py
from rpython.rlib.parsing.ebnfparse import parse_ebnf, make_parse_function
from rpython.rlib.parsing.parsing import ParseError
from rpython.rlib.parsing.tree import RPythonVisitor, Symbol
from rpython.rlib.rarithmetic import ovfcheck_float_to_int


from ltpyb import ltpybdir


grammar_file = 'grammar.txt'
grammar = py.path.local(ltpybdir).join(grammar_file).read("rt")

try:
    regexes, rules, ToAST = parse_ebnf(grammar)
except ParseError, e:
    print e.nice_error_message(filename=grammar_file, source=grammar)
    raise
_parse = make_parse_function(regexes, rules, eof=True)


def parse(code):
    t = _parse(code)
    return ToAST().transform(t)


class Transformer(RPythonVisitor):
    def __init__(self):
        self.funclists = []
        self.scopes = []
        self.depth = -1


def source_to_ast(source):
    try:
        ast = parse(source)
    except ParseError as e:
        print e.nice_error_message(source=source)
        raise
    transformer = Transformer()
    return transformer.dispatch(ast)

