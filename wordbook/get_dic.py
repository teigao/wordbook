#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module is used to get defination of a word.
"""

__author__ = 'Teige Gao'

import pandas as pd
import os
import re

_current_path = os.path.dirname(__file__)
_root_folder = _current_path+"/_resource/"


def _get_dictionary(file_name):
    dictionary = pd.read_csv(open(
        _root_folder + file_name, 'r', encoding='UTF-8'), low_memory=False, index_col=0)
    return dictionary


voc_easy = _get_dictionary('voc_easy.csv')['voc_easy']
voc_more = _get_dictionary('voc_more.csv')['voc_more']
cn_define_fre = _get_dictionary('cn_define_fre.csv')['cn_define_fre']
easy_und = _get_dictionary('easy_und.csv')['easy_und']
word_place = _get_dictionary('word_place.csv')['word_place']


def _get_part(string):
    result = re.search('<div class="coca">.*', str(string))
    if result == None:
        return None
    else:
        return re.sub('<.*?>', ' ', result.group(0).replace('</span><span class="rank">', ' rank: ').replace('</span><span class="total">', ' count: '))


word_place_changed = word_place.apply(lambda x: _get_part(x))

if __name__ == '__main__':
    print('Welcome to use "wordbook" library, please use it with the import command!')
    print(word_place_changed.loc['simple'])
