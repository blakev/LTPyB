#! /usr/bin/env python
# -*- coding: utf-8 -*-
# >>
#     LTPyB, 2016
# <<

from rply import LexerGenerator

lg = LexerGenerator()

lg.add('INTEGER',       r'\-?\d+')
lg.add('FLOAT',         r'\-?\d+\.\d+')
lg.add('OP_ASSIGNMENT', r'=')
lg.add('OP_EQUAL',      r'==')

lg.ignore(r'\s+')    # ignore whitespace
lg.ignore(r'#.*\n')  # ignore comments

lexer = lg.build()