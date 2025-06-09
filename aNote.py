
# Let's make a class to instantiate every containerized note.
# This will save me a lot of headache and reduce the among of spagetti in my code
# As much as I like spagetti, it does not belong in my notes
# Purpose of class is to make a blueprint of my note that I can copy very easily with every instance
# ...

###############
### Imports ###
############### 
import subprocess
import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

#from main import *
class aNote:
    # Class attributes go here - is shared by all instances of aNote
    
    # I need to pass in the main_window object. Since all notes go inside it
    # I need to keep the main_window grid count for rows.
    # I need a helper method to get the list of "saved" notes. 
    # Disallow adding new notes until previous ones are loaded. 
        # Onces loaded, you can grey out the load notes button
    

    # __init__ is like a constructor
    def __init__(self, window, header_txt="", body_txt=""):
        #self.w = window
        self.f = window.frame
        self.r = window.row_cnt


        # Instance attributes go here - belongs to specific instance, not shared
            # unique file path

        #global main_row_cnt
        
        # note container
        note_container = tk.Frame(window.frame, borderwidth=1, relief="raised")
        note_container.grid(column=0, row=window.row_cnt, padx=10, pady=10, ipadx=5, ipady=5)
        #main_row_cnt += 1
        window.row_cnt += 1
        note_row_cnt = 0

        # Load note header & body
        #nt_h_data, nt_b_data = fn_load_from_file()
        

        # note header
        note_header = tk.Entry(note_container, width=60)
        note_header.insert(0, header_txt)
        note_header.grid(column=0, row=0, padx=(10,0), pady=(10,4), sticky="w")

        # Delete note button
        btn_delete_note = tk.Button(note_container, text="X", relief="sunken",
            bd=0, activeforeground="red", font=("Courier", 16, "bold"))
        btn_delete_note.grid(column=1, row=0, padx=0, pady=0, sticky="ne")

        # note body
        note_body = scrolledtext.ScrolledText(note_container, wrap=tk.WORD, width=60, height=5)
        note_body.insert(tk.INSERT, body_txt)
        note_body.grid(column=0, row=1, pady=0, padx=10, sticky="w")

        # Put note buttons into 1 container
        frame_note_btns = tk.Frame(note_container)
        frame_note_btns.grid(column=1, row=1, pady=0, padx=10)

        # Note Buttons (print, save to file, save to DB)
        btn_print = tk.Button(frame_note_btns, text="Print", command=lambda: aNote.fn_print(note_header,note_body))
        btn_print.grid(column=0, row=1, pady=2, padx=0, sticky="w")

        btn_save_file = tk.Button(frame_note_btns, text="Save File", command=lambda: aNote.fn_save_to_file(note_header, note_body))
        btn_save_file.grid(column=0, row=2, pady=2, padx=0, sticky="w")

        btn_save_db = tk.Button(frame_note_btns, text="Save DB", command=aNote.fn_save_to_db)
        btn_save_db.grid(column=0, row=3, pady=2, padx=0, sticky="w")
    
    #################
    ### Functions ###
    #################

    def add_note_container():
        pass

    # print to terminal
    def fn_print(note_header, note_body):
        # extract input of note header & footer
        data_h = note_header.get()
        data_b = note_body.get("1.0", "end-1c") # -1c deletes 1 character from end, which is newline
        print("entered note header:", data_h)
        print("entered note body:", data_b)

    # save to file
    def fn_save_to_file(note_header, note_body):
        data_h = note_header.get()
        data_b = note_body.get("1.0", "end-1c")
        with open(note_path, "w") as f:    # relative to script, make subdirectory "savedNotes"
            f.write(data_h)
            f.write('\n\n')
            f.write(data_b)
        # for testing purposes, it would be nice to immediately open the file too
        filepath = os.getcwd() + "\\saved_notes\\testNote.txt"
        os.startfile(filepath)

    # save to db (later. Next step: containerize notes? uniquly name files?)
    def fn_save_to_db():
        pass
