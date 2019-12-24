# wordbook Document

**Important: All dictionary files used in this module are get from 
<https://www.pdawiki.com/forum/?fromuid=260106>. They come from vocabulary.com, COCA 60000**

This module is used to create wordbook automatically. This document will be divided into two parts:

- <a href="#easy_to_use">easy to use</a>
- <a href="#hard_to_use">generate function for dataset</a>

### <a name ="easy_to_use">easy to use</a>

Firstly, download Python runtime 3.6.8 from <https://www.python.org/downloads/release/python-368/>, for 32-bit machine, download the "Windows x86 executable installer", for 64-bit machine, download the "Windows x86-64 executable installer", then install the exe file on your machine.

We can download this tool from <https://raw.githubusercontent.com/teigao/wordbook/master/wordbook.7z>, then unzip this file and put the wordbook folder to the Python path. We can refer to the sample.py in the project list to get started.


### <a name="hard_to_use">generate function for dataset</a>



We can download this module from <https://raw.githubusercontent.com/teigao/wordbook/master/wordbook.7z>, then unzip this file and put the wordbook folder to the Python path. We can refer to the sample.py in the project list to get started.

**This module is developed under Python 3.6.8, before using this module, please put the wordbook folder under %PYTHONPATH%\Lib\site-packages. We also need to install pandas library before using this module** <- very important

>This module provides one function, `generate_html()` will receive a pandas dataframe data type and will generate a html file to the _resource/wordbook.html under the root folder of wordbook. **Important: We need to create a dataset with two columns, one column name is word and another is freq. The freq will not be queried, it only display after the word as a frequence of this word.**

How to use: Open python client as Administrator, then run the following script:

```python
import pandas as pd
import wordbook

dataset = pd.DataFrame(
    {'word': ['simple', 'hard', 'middle'], 'freq': ['W1', 'W2', 'W3']})

print(wordbook.generate_html(dataset))
```

The output file will like below:

![Image text](https://raw.githubusercontent.com/teigao/wordbook/master/image/result.png)


We can change the style of the output file by changing the style.css file under _resource folder.

The result will be saved at _resource/wordbook.html under %PYTHONPATH%\Lib\site-packages\wordbook, **the code of the html is UTF-8, if you want to open it in Word, please change the code to UTF-8 with Bom.** Tip: we can convert the html file to PDF in Microsoft Word.


