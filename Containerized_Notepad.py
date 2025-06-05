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

import tkinter as tk            # import GUI library
m = tk.Tk()                     # make [m]ain window
m.geometry("500x300")   #win size
l = tk.Label(m, text="test")    # Label function pulled from tk
l.pack()                        # Add label to main window

m.mainloop()                    # keep [m]ain window open
