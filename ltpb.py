#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~
# >>
#   Author: Blake VandeMerwe
#   Created: January 2017
# <<

"""
Python LTPB Interpreter.

Written in RPython for the Pypy tool-chain.
"""

import os

from textx.metamodel import metamodel_from_file


GRAMMAR_FILE = os.getenv('LTPB_GRAMMAR', './grammar.tx')


class LTPBCompiler(object):
    def __init__(self, backend=None):
        self.variables = None
        self.backend = backend

        self.model = metamodel_from_file(GRAMMAR_FILE)
        self.model.register_obj_processors({
            'PrintStatement': self.handle_print
        })

    def compile(self, filename, variables=None):
        variables = variables or {}
        if not os.path.exists(filename):
            raise IOError('file does not exist, %s' % filename)
        self.model.model_from_file(filename)

    def emit(self, instruction):
        self.backend.add_instruction(instruction)
        return instruction

    def handle_print(self, s):
        print s.var


x = LTPBCompiler()
x.compile('tests/grammar_0.bas')
