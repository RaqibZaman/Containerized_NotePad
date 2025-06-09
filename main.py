'''
Long-term Objective: Make a notepad. But it will have containers for each note. So kind of like a
a scrolling window with multiple notes. Each note will have a header. This is for a later
project where I plan to make a tool to help me automatically apply for jobs by detecting
the header text of an input element, and pulling up information that most closely matches the 
title of a note.
'''
# Short-term Objective: Make a notepad with containerized notes with header and body.
# Steps
    # 1.[x] Make a window
        # [] Need to make window scrollable );
    # 2.[x] Make editable field (note header, body)
    # 3.[] Must be able to save contents
        # 1.[x] test saving to a notepad
            # [x] when opening app, should automatically load any previous notes
        # 2.[] test saving to a database for fun- probably easier to manage in the long run
    # 4.[] Containerize each "note"
        # 0.[x] Add/Delete note btn
            # [] add/delete not btns functions
        # 1.[] Should be able to make multiple notes
        # 2.[] filename = basename + number
            # You added and deleted random files. Find file of biggest number x. New file will be x+1
        # 3.[] Deleting notes => delete file too
    # ...

### Dev notes ###
# Project idea: software development toolbelt
# Project idea: type search term once, search on multiple sites
    # google, google site:stackoverflow, site:reddit, chatgpt, Documentation source
        # You should be able to specify which websites you want to check in-app
        #automatically set windows in an organize fashion for quick manual parsing
###
# Dude, code is becoming a mess. Need to soon implement OOP
# Naming convenvtion idea: Parent_child_function?
# You need to call grid() or pack() to attach element to main window
# Functions have to be defined above its call
# Later, I can use Frame to be a single container for each note. Then have a function that replicates this for each note
# Please remember that += and =+ are NOT THE SAME!!!! Former is increment, later is make positive...
# ...
###############
### Imports ###
############### 
import subprocess
import os
import tkinter as tk                # import GUI library... pronounced "T K Inter ¯\_(ツ)_/¯"... also "as tk" to kind of encapsulate library if I import other libraries too      
from tkinter import ttk
from tkinter import scrolledtext

from aNote import aNote         # ugh... from file aNote import class aNote

# Note: I plan for now only to have 1 instance of Window attribute... so a singleton class
class window:
    # Class attributes for all windows... although atm is singleton
    frame = tk.Tk()
    note_array = []     # I might need to keep track of all the notes?
    nt_idx = 0
    row_cnt = 0    # grid row count based on main window as parent

    file_base_name = "containerNote_"
    file_num = 0
    file_ext = ".txt"
    note_path = "saved_notes/testNote.txt"

    def __init__(self):
        # instance attributes for a specific window... singleton though
        
        window.frame.title("Containerized Notes")
        window.frame.geometry("650x600")           #win size x, y

        # Enter Note Label
        label = tk.Label(window.frame, text="Enter your notes", font=("Courier", 16, "bold"))       # make label
        label.grid(column=0, row=window.row_cnt, pady=4, padx=10, sticky="w")                      # attach to main
        window.row_cnt += 1

        # main window buttons container
        frame_main_btns = tk.Frame(window.frame)
        frame_main_btns.grid(column=0, row=window.row_cnt, pady=0, padx=0, sticky="w")
        window.row_cnt += 1

        # Load a Note button
        btn_add_note = tk.Button(frame_main_btns, text="Load a Note?", command=window.create_note)
        btn_add_note.grid(column=0, row=0, padx=10, pady=10, sticky="w")

        # Add a New Note button
        btn_add_note = tk.Button(frame_main_btns, text="Add New Note", command=window.create_note)
        btn_add_note.grid(column=1, row=0, padx=10, pady=10, sticky="w")

        window.frame.mainloop()  # keep window open

        print("Main Window initialized")

    def inc_row_cnt():
        window.row_cnt += 1
    
    def create_note(header_txt="", body_txt=""):
        #newNote = aNote(window.frame, window.row_cnt)
        newNote = aNote(window, header_txt, body_txt)
        window.note_array.append(newNote)
        window.nt_idx += 1

    # load file
    def fn_load_from_file(note_path):
        # Check if file exists
        if os.path.isfile(note_path):
            with open(note_path, "r") as f:
                dt_raw = f.read()
                dt_parts = dt_raw.split('\n\n', 1)
                data_h = dt_parts[0]
                data_b = dt_parts[1]
        return data_h, data_b

    def load_note():
        # Get the list of files
        # Get their paths
        # fn_load_from_file(note_path)
        # create_note()
        pass


# run main window I suppose...
window()
