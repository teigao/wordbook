# wordbook Document
This module is used to create wordbook automatically. 

**Important: All dictionary files used in this module are get from 
<https://www.pdawiki.com/forum/?fromuid=260106>. They come from vocabulary.com, COCA 60000**

We can download this module from <https://github.com/teigao/wordbook/blob/master/wordbook.7z>, then unzip this file and put the wordbook folder to the Python path. We can refer to the sample.py in the project list to get started.

**This module is developed under Python 3.6.8, before using this module, please put the wordbook folder under %PYTHONPATH%\Lib\site-packages. We also need to install pandas library before using this module** <- very important

>This module provides one function, `generate_html()` will receive a pandas dataframe data type and will generate a html file to the _resource/wordbook.html under the root folder of wordbook.

How to use: Open python client as Administrator, then run the following script:

```python
import pandas as pd
import wordbook

dataset = pd.DataFrame({"word": "simple", "freq": "W1"}, {
                       "word": "hard", "freq": "W2"}, {"word": "example", "freq": "W3"})

print(wordbook.generate_html(dataset))
```

The result will be saved at _resource/wordbook.html under %PYTHONPATH%\Lib\site-packages\wordbook, **the code of the html is UTF-8, if you want to open it in Word, please change the code to UTF-8 with Bom.** Tip: we can convert the html file to PDF in Microsoft Word.


