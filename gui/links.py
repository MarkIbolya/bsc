# -*- coding: utf-8 -*-

import src.links as lnks
import sys
import Tkinter as tk
import ScrolledText

global url
global editArea
global gui_links
global lnks
global label2
url = sys.argv[0]

def gui_links(url):
    i = 0
    links = lnks.Links(url)
    for link in links.out_links():
        i += 1
        editArea.insert('1.0', link + "\n")
    if i == 0:
        label2.configure(fg="red")
        label2.configure(text="Az oldalon nem található link.")
    else:
        label2.configure(text=str(i) + " link találva.")
        
root = tk.Tk()

root.title("Linkek keresése")
root.geometry('750x550+100+50')
app = tk.Frame(root)
app.grid()

label = tk.Label(app, text="A megadott URL: " + url, font=("Helvetica", 16))
label.grid()

button = tk.Button(app, text="Indítás", command=lambda: gui_links(sys.argv[0]))
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








