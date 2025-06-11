'''
Long-term Objective: Make a notepad. But it will have containers for each note. So kind of like a
a scrolling window with multiple notes. Each note will have a header. This is for a later
project where I plan to make a tool to help me automatically apply for jobs by detecting
the header text of an input element, and pulling up information that most closely matches the 
title of a note.
'''
# Short-term Objective: Make a notepad with containerized notes with header and body.
# To Do
    # [x] Deleting notes => delete file too
    # [] If all notes are deleted, reset note_id and note_number I guess
    # [] Need to make window scrollable );
    # [] test saving to a database for fun- probably easier to manage in the long run
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
    btn_sw_arr = []
    note_array = []     # I might need to keep track of all the notes?
    nt_idx = 0
    row_cnt = 0    # grid row count based on main window as parent

    #file_base_name = "containerNote_"
    file_num = 0
    file_ext = ".txt"
    note_dir = "saved_notes/"
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

        w_col = 0
        # Print Note List button
        btn_print_nt = tk.Button(frame_main_btns, text="Print Note List", command=window.print_nt_list)
        btn_print_nt.grid(column=w_col, row=0, padx=10, pady=10, sticky="w")
        w_col += 1

        # Load a Note button
        btn_load_nt = tk.Button(frame_main_btns, text="Load Notes", command=window.load_notes)
        btn_load_nt.grid(column=w_col, row=0, padx=10, pady=10, sticky="w")
        w_col += 1
        window.btn_sw_arr.append(btn_load_nt)

        # Add a New Note button
        btn_add_nt = tk.Button(frame_main_btns, text="Add New Note", command=window.create_note)
        btn_add_nt.grid(column=w_col, row=0, padx=10, pady=10, sticky="w")
        w_col += 1
        window.dis_btn(btn_add_nt)
        window.btn_sw_arr.append(btn_add_nt)

        print("Main Window initialized")
        window.frame.mainloop()  # keep window open

    def dis_btn(btn):
        btn.config(state="disabled")

    def enb_btn(btn):
        btn.config(state="normal")

    def switch_btn_state(btn1, btn2):
        window.dis_btn(btn1)
        window.enb_btn(btn2)
    
    def create_note(file_num=-1, header_txt="", body_txt=""):
        #newNote = aNote(window.frame, window.row_cnt)
        #if (file_num)
        newNote = aNote(window, file_num, header_txt, body_txt)
        window.note_array.append(newNote)
        window.nt_idx += 1

    # get list of files
    def get_file_list():
        dir = window.note_dir
        files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
        return files
    
    def print_nt_list():
        print(window.get_file_list())
    
    # load file
    def load_from_file(note_path):
        # Check if file exists
        if os.path.isfile(note_path):
            with open(note_path, "r") as f:
                dt_raw = f.read()
                dt_parts = dt_raw.split('\n\n', 1)
                data_h = dt_parts[0]
                data_b = dt_parts[1]
        return data_h, data_b

    def get_file_num(file_path):
        # without ".txt"
        str = file_path.rsplit(".txt", 1)[0]
        file_num = str.rsplit("_", 1)[1]
        return file_num
    
    def load_notes():
        # Get the list of files
        files = window.get_file_list()
        # Get their paths
        file_paths = [window.note_dir + f for f in files]
        for p in file_paths:
            header, body = window.load_from_file(p)
            file_num = window.get_file_num(p)
            window.create_note(file_num, header, body)

        b1, b2 = window.btn_sw_arr
        window.switch_btn_state(b1, b2)


    def test_run():
        # load notes
        # new notes
        # save notes
        pass


# run main window I suppose...
window()
