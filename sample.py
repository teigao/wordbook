import pandas as pd
import wordbook
import webbrowser
dataset = pd.DataFrame({"word":"simple","freq":"W1"},{"word":"hard","freq":"W2"},{"word":"example","freq":"W3"})
print(wordbook.generate_html(dataset))
