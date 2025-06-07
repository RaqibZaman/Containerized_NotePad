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
        # 1. test saving to a notepad
        # 2. test saving to a database for fun- probably easier to manage in the long run
    # ...

### Dev notes ###
# You need to call grid() or pack() to attach element to main window
# Functions have to be defined above its call
# Later, I can use Frame to be a single container for each note. Then have a function that replicates this for each note
# ...

import subprocess
import os
import tkinter as tk                # import GUI library... pronounced "T K Inter ¯\_(ツ)_/¯"... also "as tk" to kind of encapsulate library if I import other libraries too      
from tkinter import ttk
from tkinter import scrolledtext

main_window = tk.Tk()                     # make [m]ain window
main_window.title("Containerized Notes")
main_window.geometry("600x600")           #win size x, y

label = tk.Label(main_window, text="Enter your notes", font=("Courier", 16, "bold"))       # make label
label.grid(column=0, row=0, pady=4, padx=10, sticky="w")                      # attach to main

# note header
note_header = tk.Entry(main_window, width=60)
note_header.grid(column=0, row=1, pady=4, padx=10, sticky="w")

# note body
note_body = scrolledtext.ScrolledText(main_window, wrap=tk.WORD, width=60, height=5)
note_body.grid(column=0, row=2, pady=2, padx=10, sticky="w")

# print to terminal
def fn_print():
    # extract input of note header & footer
    data_h = note_header.get()
    data_b = note_body.get("1.0", "end-1c") # -1c deletes 1 character from end, which is newline
    print("entered note header:", data_h)
    print("entered note body:", data_b)

# save to file
def fn_save_to_file():
    data_h = note_header.get()
    data_b = note_body.get("1.0", "end-1c")
    with open("saved_notes/testNote.txt", "w") as f:    # relative to script, make subdirectory "savedNotes"
        f.write(data_h)
        f.write('\n\n')
        f.write(data_b)
    # for testing purposes, it would be nice to immediately open the file too
    filepath = os.getcwd() + "\\saved_notes\\testNote.txt"
    os.startfile(filepath)

# save to db (later. Next step: containerize notes? uniquly name files?)
def fn_save_to_db():
    # extract input of note header & footer
    #data_h = note_header.get()
    #data_b = note_body.get("1.0", "end-1c") # -1c deletes 1 character from end, which is newline
    #print("entered note header:", data_h)
    #print("entered note body:", data_b)
    print("nothing to see here...")

# Put note buttons into 1 container
btn_frame = tk.Frame(main_window)
btn_frame.grid(column=1, row=2, pady=0, padx=10)

# Note Buttons
btn_print = tk.Button(btn_frame, text="print", command=fn_print)
btn_print.grid(column=0, row=1, pady=2, padx=0, sticky="w")

btn_save_file = tk.Button(btn_frame, text="save file", command=fn_save_to_file)
btn_save_file.grid(column=0, row=2, pady=2, padx=0, sticky="w")

btn_save_db = tk.Button(btn_frame, text="save DB", command=fn_save_to_db)
btn_save_db.grid(column=0, row=3, pady=2, padx=0, sticky="w")



# Need to add word wrap to edible field

# Need to be able to save information, maybe as text file?

main_window.mainloop()                    # keep [m]ain window open
