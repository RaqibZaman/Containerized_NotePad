'''
Long-term Objective: Make a notepad. But it will have containers for each note. So kind of like a
a scrolling window with multiple notes. Each note will have a header. This is for a later
project where I plan to make a tool to help me automatically apply for jobs by detecting
the header text of an input element, and pulling up information that most closely matches the 
title of a note.
'''
# Short-term Objective: Make a notepad with containerized notes with header and body.
# Steps
    # 1. Make a window
    # 2. Make a editable field
    # 3. Make containers for each editable field
    # 4. A container must be composed of
        # a) header
        # b) editable field
    # 5. Must be able to save contents
    # ...

# import GUI library... pronounced "T K Inter ¯\_(ツ)_/¯"... also "as tk" to kind of encapsulate library if I import other libraries too
import tkinter as tk            
from tkinter import ttk
from tkinter import scrolledtext

mWin = tk.Tk()                     # make [m]ain window
mWin.title("Containerized Notes")
mWin.geometry("550x600")           #win size

mylabel = tk.Label(mWin, text="Enter your notes")       # make label
mylabel.grid(column=0, row=0)                             # attach to main

# editable note title
noteHead = tk.Entry(mWin, width=60)
noteHead.grid(column=0, row=1, pady=10, padx=10)

# editable note field
notebody = scrolledtext.ScrolledText(mWin, wrap=tk.WORD, width=60, height=5)
notebody.grid(column=0, row=2, pady=10, padx=10)

# save button header and field



# Need to add word wrap to edible field

# Need to be able to save information, maybe as text file?

mWin.mainloop()                    # keep [m]ain window open
