#! /usr/bin/env python
# -*- coding: utf-8 -*-
# >>
#     LTPyB, 2016
# <<

from rply.token import BaseBox


class IntBox(BaseBox):
    def __init__(self, value):
        self.value = int(value.getstr())

    def int(self):
        return self.value


class FloatBox(BaseBox):
    def __init__(self, value):
        self.value = float(value.getstr())

    def float(self):
        return self.value

