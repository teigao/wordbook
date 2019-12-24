#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module is used to get defination of a word. 
This module provides two functions, 
one for querying word and another for generating wordbook, 
it will provides a html string. For more information, I would suggest you referring to: https://github.com/teigao/wordbook
"""

__author__ = 'Teige Gao'

from wordbook import get_dic
import os
import webbrowser
import pandas as pd 
from shutil import copyfile
import winreg

_current_path = os.path.dirname(__file__)
_project_root_folder = _current_path+"/_resource/"

def _get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    return winreg.QueryValueEx(key, "Desktop")[0]

def _query_word(word, fre=''):
    """
    This function will return a defination of a word.
    """
    word_item = '<div class = "word_ite"><span class = "word_def_w">' + \
        word + '</span><span class = "lon_def"> ' + str(fre) + '</span></div>'
    if word in get_dic.voc_easy.index:
        voc_easy = '<div class = "explaincard_content" style="font-style:italic">' + \
            get_dic.voc_easy.loc[word] + '</div>'
    else:
        voc_easy = ''
    if word in get_dic.voc_more.index:
        voc_more = '<div class = "explaincard_content">' + \
            get_dic.voc_more.loc[word] + '</div>'
    else:
        voc_more = ''
    if word in get_dic.cn_define_fre.index:
        cn_define_fre = '<div class = "explaincard_content">' + \
            get_dic.cn_define_fre.loc[word] + '</div>'
    else:
        cn_define_fre = ''
    if word in get_dic.easy_und.index:
        easy_und = '<div class = "explaincard_content">' + \
            get_dic.easy_und.loc[word] + '</div>'
    else:
        easy_und = ''
    if voc_easy != '' or voc_more != '':
        voc = '<div class = "explaincard"><div class = "explaincard_title">&nbsp;&nbsp;Explation E-E</div>' + \
            voc_easy + voc_more + '</div>'
    else:
        voc = ''
    if cn_define_fre != '' or easy_und != '':
        vvv = '<div class = "explaincard"><div class = "explaincard_title">&nbsp;&nbsp;Explation C-E</div>' + \
            cn_define_fre + easy_und + '</div>'
    else:
        vvv = ''
    if voc != '' or vvv != '':
        result = word_item + voc + vvv
    else:
        result = None
    return result


def generate_html(dataset):
    """
    This function will return a html of wordbook quried by the dataset. You can use print() function to get the result and saved it as html file manually.
    """
    html_style = open(
        _project_root_folder + 'style.css', 'r', encoding='UTF-8').read()
    
    temp = dataset.apply(lambda x: _query_word(
        x['word'], x['freq']), axis=1).tolist()
    result = '''<html>
    <head>
        <style>
            ''' + html_style + '''
        </style>
    </head>
    <body>
        ''' + "\n".join(s for s in temp if s is not None) + '''    
    </body>
</html>'''
    return result
    

def create_book(source_path = _project_root_folder + 'sample.csv', result_saved_path = _get_desktop() + '\\result.html'):
    temp_html = open(_project_root_folder + 'wordbook.html', 'w', encoding='UTF-8')
    word_dataset = pd.read_csv(open(
        source_path, 'r', encoding='UTF-8'), low_memory=False)
    generated_html = generate_html(word_dataset)
    temp_html.write(generated_html)
    temp_html.close()
    saved_html_path = 'file:///' + result_saved_path
    copyfile(_project_root_folder + 'wordbook.html',result_saved_path)
    webbrowser.open_new_tab(saved_html_path)
    message = "The html has been generated to " + result_saved_path
    print(message)
    return None

if __name__ == '__main__':
    print('Welcome to use "wordbook" library, please use it with the import command!')
