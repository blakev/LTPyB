#! /usr/bin/env python
# -*- coding: utf-8 -*-
# >>
#     LTPyB, 2016
# <<

class SymbolEntry(object):
    def __init__(self, sname, skind, stype):
        self.name = sname
        self.kind = skind
        self.type = stype


class SymbolTable(object):

    def __init__(self, shared):
        self.table = []
        self.shared = shared

    def __len__(self):
        return len(self.table)

    def error(self, text=""):
        if text:
            raise Exception('SymbolTable error: %s' % text)
        else:
            raise Exception('SymbolTable out of range')

    def insert_symbol(self, sname, skind, stype):
        pass
