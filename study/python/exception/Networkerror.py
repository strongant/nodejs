# _*_coding: UTF-8_*_
__author__ = 'bwh'

class Networkerror(RuntimeError):
    def __init__(self,arg):
        self.args = arg