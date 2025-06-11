
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

class aNote:
    # Class attrs
    max_id = 0
    base_file_name = "containerNote_"
    id_list= []

    def __init__(self, window, file_num, header_txt, body_txt):
        # Instance attrs
        self.header_txt = header_txt
        self.body_txt = body_txt
        self.note_dir = window.note_dir

        # note id needs to iterate from max id. Check file_num against max_id
        if aNote.get_max_id == file_num:
            self.note_id = file_num + 1
        else:
            self.note_id = file_num
        aNote.id_list.append(self.note_id)      # keep track of existing notes by id

        self.note_path = self.get_note_path() # depends on self.note_id
        
        # note container
        note_container = tk.Frame(window.frame, borderwidth=1, relief="raised")
        note_container.grid(column=0, row=window.row_cnt, padx=10, pady=10, ipadx=5, ipady=5)
        window.row_cnt += 1
        self.note_container = note_container    # Why???

        # note header
        note_header = tk.Entry(note_container, width=60)
        note_header.insert(0, self.header_txt)
        note_header.grid(column=0, row=0, padx=(10,0), pady=(10,4), sticky="w")
        
        # Delete note button
        btn_delete_note = tk.Button(note_container, text="X", relief="sunken",
            bd=0, activeforeground="red", font=("Courier", 16, "bold"), command=lambda: aNote.delete_note(self))
        btn_delete_note.grid(column=2, row=0, padx=0, pady=0, sticky="ne")

        # note body
        note_body = scrolledtext.ScrolledText(note_container, wrap=tk.WORD, width=60, height=5)
        note_body.insert(tk.INSERT, self.body_txt)
        note_body.grid(column=0, row=1, pady=0, padx=10, sticky="w")

        #### START frame_note_btns ###
        frame_note_btns = tk.Frame(note_container)
        frame_note_btns.grid(column=1, row=1, pady=0, padx=10)

        btn_print = tk.Button(frame_note_btns, text="Print", command=lambda: aNote.print_note(note_header,note_body))
        btn_print.grid(column=0, row=1, pady=2, padx=0, sticky="w")

        btn_save_file = tk.Button(frame_note_btns, text="Save File", command=lambda: aNote.save_to_file(self, note_header, note_body))
        btn_save_file.grid(column=0, row=2, pady=2, padx=0, sticky="w")

        btn_save_db = tk.Button(frame_note_btns, text="Save DB", command=aNote.fn_save_to_db)
        btn_save_db.grid(column=0, row=3, pady=2, padx=0, sticky="w")
        #### END frame_note_btns ###

        ### START debug_frame ###
        frame_debug = tk.Frame(note_container)
        frame_debug.grid(column=0, row=2, pady=0, padx=10, sticky="w")
        
        # Note ID
        btn_delete_note = tk.Button(frame_debug, text=("id: " + str(self.note_id)), relief="sunken", bd=1)
        btn_delete_note.grid(column=0, row=0, padx=(0,2), pady=0, sticky="w")

        # note_path
        btn_delete_note = tk.Button(frame_debug, text=self.note_path, relief="sunken", bd=1)
        btn_delete_note.grid(column=1, row=0, padx=(0,2), pady=0, sticky="w")
        ### END debug_frame ###

    
    #################
    ### Functions ###
    #################

    def get_note_path(self):
        note_path = self.note_dir + self.base_file_name + str(self.note_id) + ".txt"
        return note_path
    
    # def update_note_path(self):
    #     self.note_path = self.get_note_path()
    
    def get_max_id():
        if aNote.id_list:
            return max(aNote.id_list)
        return 0
    
    def delete_note(self):
        # delete frame
        aNote.id_list.remove(self.note_id)
        self.note_container.destroy()
        # still need to garbage collect the instance of aNote... if it ain't broke, don't fix it ¯\_(ツ)_/¯
        # delete file
        print(self.note_path)
        if os.path.exists(self.note_path):
            os.remove(self.note_path)
        else:
            print("Something is wrong... file does not exist to delete?????????????")

    # print to terminal
    def print_note(note_header, note_body):
        # extract input of note header & footer
        data_h = note_header.get()
        data_b = note_body.get("1.0", "end-1c") # -1c deletes 1 character from end, which is newline
        print("entered note header:" + "\n", data_h)
        print("entered note body:" + "\n", data_b)
    
    # save to file
    def save_to_file(self, note_header, note_body):
        data_h = note_header.get()
        data_b = note_body.get("1.0", "end-1c")
        
        with open(self.note_path, "w") as f:    # relative to script, make subdirectory "savedNotes"
            f.write(data_h)
            f.write('\n\n')
            f.write(data_b)
        
        # for testing purposes, it would be nice to immediately open the file too
        start_file_path = "\\" + self.note_path.replace("/", "\\")
        filepath = os.getcwd() + start_file_path
        os.startfile(filepath)  # open's saved file

    # save to db (later. Next step: containerize notes? uniquly name files?)
    def fn_save_to_db():
        pass
