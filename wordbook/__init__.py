#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module is used to get defination of a word. 
This module provides two functions, 
one for querying word and another for generating wordbook, 
it will provides a html string.
"""

__author__ = 'Teige Gao'

from wordbook import get_dic


def query_word(word, fre = ''):
    """
    This function will return a defination of a word.
    """
    word_item = '<div class = "word_ite"><span class = "word_def_w">' + \
        word + '</span><span class = "lon_def"> ' + fre + '</span></div>'
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
        voc = '<div class = "explaincard"><div class = "explaincard_title">&nbsp&nbspExplation E-E</div>' + \
            voc_easy + voc_more + '</div>'
    else:
        voc = ''
    if cn_define_fre != '' or easy_und != '':
        vvv = '<div class = "explaincard"><div class = "explaincard_title">&nbsp&nbspExplation C-E</div>' + \
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
    This function will return a html of wordbook quried by the dataset.
    """
    temp = dataset.apply(lambda x: query_word(
        x['word'], x['freq']), axis=1).tolist()
    result = '''<html>
    <head>
        <style>
            body {
                text-align: left;
                color: #000000;
                padding: 0px;
                margin: 0px;
            }
            .word_ite {font-size: 2em;}
            .lon_def {font-size: 0.5em;}
            .explaincard {
                margin:0px; 
                padding-top: 15px;
                padding-left: 15px;
                padding-right: 15px;
                padding-bottom: 10px;
            }
            .explaincard_title {
                color: #000000;
                font-weight: bold;
                border-left:5px solid #1282e2; 
                margin-bottom: 10px;
            }
            .explaincard_content {
                margin-bottom: 5px;
                line-height: 1.5em;
                margin-top: 5px;
                color: #000000;
            }
            .hr_more_define {
                border:none;
                border-top: 1px solid #B3E5FC;
            }
            .hw {
                display:none;
            }
            .pt {
                display:none;
                }
            .word-frequency {
                margin-bottom:3px;
                }
            .coca2 {
                margin-top:5px;
                }
            .coca_desc {
                margin-top:3px;
                }
            .pos_v {
                display: inline;
                vertical-align:middle;
                padding:1px 2px 1px 2px;
                text-align: center;
                border-radius: 5px;
                margin: 0px 3px 0px 0px;
                font-size:12px;
                color: #ffffff;
                background: #4CAF50;
            }
            .pos_n {
                display: inline;
                vertical-align:middle;
                padding:1px 2px 1px 2px;
                text-align: center;
                border-radius: 5px;
                margin: 0px 3px 0px 0px;
                font-size:12px;
                color: #ffffff;
                background: #03A9F4;
            }
            .pos_j {
                display: inline;
                vertical-align:middle;
                padding:1px 2px 1px 2px;
                text-align: center;
                border-radius: 5px;
                margin: 0px 3px 0px 0px;
                font-size:12px;
                color: #ffffff;
                background: #f9320c;
            }
            .pos_r {
                display: inline;
                vertical-align:middle;
                padding:1px 2px 1px 2px;
                text-align: center;
                border-radius: 5px;
                margin: 0px 3px 0px 0px;
                font-size:12px;
                color: #ffffff;
                background: #7200da;
            }
            .pos_u {
                display: inline;
                vertical-align:middle;
                padding:1px 2px 1px 2px;
                text-align: center;
                border-radius: 5px;
                margin: 0px 3px 0px 0px;
                font-size:12px;
                color: #ffffff;
                background: #ff5f2e;
            }
            .label {
                padding:1px 2px 1px 2px;
                text-align: center;
                border-radius: 5px;
                margin: 3px;
                text-transform:capitalize;
                font-size:12px;
                border:1px solid;
            }    
            .label-primary {
                color: rgb(18,130, 226);
                border-color: rgb(18,130,226);
            }
            .label-success {
            color: rgb(18,130, 226);
                border-color: rgb(18,130,226);
            }
            .label-info {
            color: rgb(18,130, 226);
                border-color: rgb(18,130,226);
            }
            .label-warning {
            color: rgb(18,130, 226);
                border-color: rgb(18,130,226);
            }
            .rank {
                font-style: italic;
            }
            .total {
                font-style: italic;
            }
            .rank:before {
                content: " RANK ";
                font-weight: normal;
                font-style: normal;
            }
            .rank:after {
                content: " FREQ ";
                font-weight: normal;
                font-style: normal;
            }
            .table {
                display: none;
            }
            .pos {
                background: #4CAF50;
                color:#ffffff;
                border-radius: 2px;
                padding: 1.5px;
                padding-top: 0px;
                padding-bottom: 0px;
                font-size: 0.9em;
            }
            .pos:after {
                content: ".";
            }
            .rank {
                display: inline;
                vertical-align:middle;
            }
            .total {
                display: inline;
                vertical-align:middle;
            }
        </style>
    </head>
    <body>''' + "".join(temp) + '''    
    </body>
</html>'''
    return result


if __name__ == '__main__':
    print('Welcome to use "wordbook" library, please use it with the import command!')
