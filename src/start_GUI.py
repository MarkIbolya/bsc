# -*- coding: utf-8 -*-

from misc import check_if_exists
import sys

import Tkinter as tk


def openFile(value):
    if value==0:
        sys.argv = [e.get()]
        execfile('../gui/brute_force.py')
    elif value==1:
        sys.argv = [e.get()]
        execfile('../gui/links.py')
    elif value==2:
        sys.argv = [e.get()]
        execfile('../gui/words.py')

def checkUrl():
    url=e.get()
    if check_if_exists(url):
        label.configure(text="Az URL elérhető!")
        label.configure(fg="green")
        for i in range(3):
            button[i].configure(state='normal')
    else:
        label.configure(text="Az URL elérhetetlen!")
        label.configure(fg="red")



root = tk.Tk()

root.title("Módszer kiválasztása")
root.geometry('230x210+100+50')
app = tk.Frame(root)
app.grid()

label = tk.Label(app, text="Adjon meg egy URL-t:", font=("Helvetica", 16))
label.grid()

button=[]

for i in range(3):
    button.append(None)

e=tk.Entry(app)
e.grid()
label = tk.Label(app, text="Még nincs URL megadva", font=("Helvetica", 12))
label.grid()

check=tk.Button(app, text="Ellenőrzés", command=checkUrl)
check.grid()

button[0] = tk.Button(app, text="Brute Force",  command= lambda: openFile(0), state='disabled')
button[0].grid()
button[1] = tk.Button(app, text="Hivatkozások",  command= lambda: openFile(1), state='disabled')
button[1].grid()
button[2] = tk.Button(app, text="Legyakoribb szavak",  command= lambda: openFile(2), state='disabled')
button[2].grid()


root.mainloop()