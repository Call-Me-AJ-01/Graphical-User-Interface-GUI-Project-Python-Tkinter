# Creating GUI For Dictionary Bot

# Adjusting The Screen Resolution Graphics

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk

# Invoking meaning finder and translator
import Finding_Meaning as fm
import Translation as tran

# Creating Object for The Window and theme
root = tk.ThemedTk()

# Adding Theme for the window
root.get_themes()
root.set_theme('radiance')

# Creating The Title for the window
root.title('Dictionary App')

# Fixing The Size Of The Window
root.geometry('400x400')

root.config(bg='gray96')

# Creating Title
title = ttk.Label(root,text='Dictionary Application',font='timesnewroman 16 bold').pack(pady=10)

# Creating Frames

# Creating Frame 1
frame_1 = ttk.Frame(root,width=300,height=30)
frame_1.pack()

# Creating Label and Entry Field on Frame1
label1 = ttk.Label(frame_1,text='Enter The Word :',font='timesnewroman 10',justify=LEFT).pack(side=LEFT)
user_input = ttk.Entry(frame_1,width=30)
user_input.focus()
user_input.pack(padx=20)

# Creating Frame 2
frame_2 = ttk.Frame(root,width=300,height=30)
frame_2.pack(pady=10)

# Creating Label and combo box
label2 = ttk.Label(frame_2,text='Language : ',font='timesnewroman 10',justify=LEFT).pack(side=LEFT)

# Creating variable
com_val = StringVar()

# Setting variable
com_val.set('English')

# Creating combo box
combo = ttk.Combobox(frame_2,textvariable=com_val,values=('Tamil','English','Telugu','Hindi','Japanese','French'),state='readonly')
combo.pack(padx=60)

# Creating Frame 3
frame_3 = ttk.Frame(root,width=300,height=20)
frame_3.pack(pady=10)

# Creating Textbox
text_box = Text(frame_3,width=35,height=10,font='timesnewroman 10',wrap=WORD)
text_box.pack()

# Creating Function For Button
def display():
    word = fm.meaning(user_input.get())
    translated_word = tran.trans(word,com_val.get())
    text_box.delete(0.0,END)
    text_box.insert(INSERT,translated_word)

# Creating Button
button = ttk.Button(frame_3,text='Find Meaning',command=display).pack(pady=10)

# Displaying The Window
root.mainloop()