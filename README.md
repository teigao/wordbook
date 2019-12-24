# wordbook Document

**Important: All dictionary files used in this module are get from 
<https://www.pdawiki.com/forum/?fromuid=260106>. They come from vocabulary.com, COCA 60000**

**the code of the html is UTF-8, if you want to open it in Word, please change the code to UTF-8 with Bom.** Tip: we can convert the html file to PDF in Microsoft Word.

This module is used to create wordbook automatically. This document will be divided into two parts:

- <a href="#easy_to_use">easy to use</a> for people have no much background knowledge on Python.
- <a href="#hard_to_use">more complex usage</a> provides function to handle dataset (pandas dataframe)

### <a name ="easy_to_use">easy to use</a>

Firstly, download Python runtime 3.6.8 from <https://www.python.org/downloads/release/python-368/>, for 32-bit machine, download the "Windows x86 executable installer", for 64-bit machine, download the "Windows x86-64 executable installer", then install the exe file on your machine.

**Important:** Please check the pip tool when you install Python.

![Image text](https://raw.githubusercontent.com/teigao/wordbook/master/image/install_python.png)

Then we can pip install the pandas library: open CMD as Administrator, type the following command:

```console
pip install pandas
```

![Image text](https://raw.githubusercontent.com/teigao/wordbook/master/image/install_pandas.png)

We can download this tool from <https://raw.githubusercontent.com/teigao/wordbook/master/wordbook.7z>, then unzip this file to any path. Then we can create a .py file besides this folder using the following command:

```python
import wordbook
wordbook.create_book('word_list_path','result_path')
```

The function wordbook.create_book requires two parameter, one for word_list, another for result_path. If you can't provide these parameters, it will use the sample word result generating a file to your desktop. Only one parameter, we can use wordbook.create_book(source_path= "").

You can refer to the sample.csv in the wordbook/_resource folder or change it directly.

After that, we can open CMD as Administrator, run the following commandv(change to your .py file path):

```console
python "C://***/***.py"
```

The output file will like below:

![Image text](https://raw.githubusercontent.com/teigao/wordbook/master/image/result.png)

### <a name="hard_to_use">more complex usage</a>

We can download this module from <https://raw.githubusercontent.com/teigao/wordbook/master/wordbook.7z>, then unzip this file and put the wordbook folder to the Python path. We can refer to the sample.py in the project list to get started.

**This module is developed under Python 3.6.8, before using this module, please put the wordbook folder under %PYTHONPATH%\Lib\site-packages. We also need to install pandas library before using this module** <- very important

>This module provides one function, `generate_html()` will receive a pandas dataframe data type and will generate a html file, you can print the result of this function and save the result as a html file manually.

**Important: We need to create a dataset with two columns, one column name is word and another is freq. The freq will not be queried, it only display after the word as a frequence of this word.**

How to use: Open python client as Administrator, then run the following script:

```python
import pandas as pd
import wordbook

dataset = pd.DataFrame(
    {'word': ['simple', 'hard', 'middle'], 'freq': ['W1', 'W2', 'W3']})

print(wordbook.generate_html(dataset))
```

We can change the style of the output file by changing the style.css file under _resource folder.



