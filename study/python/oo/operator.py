# _*_coding: UTF-8_*_
__author__ = 'bwh'

class operator(object):

    def __init__(self,name,score):
        self._name = name
        self._score  = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    def print_score(self):
        print("%s:%s"%(self._name,self._score))

