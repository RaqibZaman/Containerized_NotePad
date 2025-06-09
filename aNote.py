
# Let's make a class to instantiate every containerized note.
# This will save me a lot of headache and reduce the among of spagetti in my code
# As much as I like spagetti, it does not belong in my notes
# Purpose of class is to make a blueprint of my note that I can copy very easily with every instance
# ...

class aNote:
    # Class attributes go here - is shared by all instances of aNote
    
    # I probably need to pass in the main_window object. Since all notes go inside it
    # I need to keep the main_window grid count for rows.
    # 

    # __init__ is like a constructor
    def __init__(self):
        # Instance attributes go here - belongs to specific instance, not shared
