# -*- coding: utf-8 -*-

import src.words as words
import sys
import Tkinter as tk
import ScrolledText

global url
url = sys.argv[0]
global gui_words
global words
global editArea
def gui_words(url):
    for i in words.words_freq(url):
        #print i[0].decode('utf-8'), str(i[1])
        try:
            editArea.insert('end', i[0].encode('utf8', 'replace') + ", megemlítve: ".decode('utf-8') + str(i[1]) + "\n")
        except:
            pass
        
global label
global label2

root = tk.Tk()

root.title("Leggyakrabban használt szavak")
root.geometry('750x550+100+50')
app = tk.Frame(root)
app.grid()

label = tk.Label(app, text="A megadott URL: " + url, font=("Helvetica", 16))
label.grid()

button = tk.Button(app, text="Szavak keresése", command=lambda: gui_words(url))
button.grid()

editArea = ScrolledText.ScrolledText(
    master=app,
    wrap=tk.WORD,
    width=50,
    height=10
)
editArea.grid()

label2 = tk.Label(app, text="", font=("Helvetica", 12), fg="green")
label2.grid()

root.mainloop()








