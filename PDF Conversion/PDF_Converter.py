from tkinter import *
from ttkthemes import themed_tk as tk
from tkinter import ttk
from tkinter import filedialog

# Adjusting The Screen Resolution Graphics
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Creating Object For The Window
root = tk.ThemedTk()

root.get_themes()
root.set_theme('radiance')

root.resizable(0,0)

root.config(bg='gray96')

# Declaring The Size Of The Window
root.title('PDF Converter')

# Fixing The Size Of The Window
root.geometry('450x400')

# Creating Function to Open File
def openfile():
    label1.config(text='')
    global filename
    filename = filedialog.askopenfilename(initialdir='/',title='Open File',
                                          filetypes=(('Word File','.docx'),('Text File','.txt')))
    entry1.insert("0",filename)

# Creating Function to Convert File
def save_file():
    label1.config(text='')
    global savefile
    savefile = filedialog.asksaveasfile(defaultextension='.pdf')
    entry2.insert("0", savefile.name)
    savefile.close()

def convert():
    label1.config(text='')
    try:
        from docx2pdf import convert
        if len(entry1.get())<2 or len(entry2.get())<2:
            if "0"+1:
                pass
        convert(entry1.get(),entry2.get())
        label1.config(text='Successfully Converted The Document...!',foreground='green')
    except:
        label1.config(text='Document Not Converted Successfully...!',foreground='red')

# Creating A frame
frame1 = ttk.Frame(root,width=500,height=10)
frame1.pack()

# Creating Label
title = ttk.Label(frame1,text='PDF CONVERTER',font=('timesnewroman',20,'bold','italic'))
title.pack(pady=(15,30))

# Creating frame2
frame2 = ttk.Frame(root,width=500,height=10)
frame2.pack()

# Creating Labelframe
browse = ttk.LabelFrame(frame2,text='Choose File')
browse.pack(side=LEFT,padx=10)

# Creating Label For Search Bar
entry1 = ttk.Entry(browse,width=30)
entry1.pack(padx=(10,10),pady=(3,13),side=LEFT)

# Creating Button For Search Bar
button = ttk.Button(browse,text='Browse',command=openfile)
button.pack(padx=(0,10),pady=(3,13))

# Creating frame3
frame3 = ttk.Frame(root,width=500,height=10)
frame3.pack(pady=15)

# Creating Labelframe
save = ttk.LabelFrame(frame3,text='Location To Save The File')
save.pack(side=LEFT,padx=10)

# Creating Label For Search Bar
entry2 = ttk.Entry(save,width=30)
entry2.pack(padx=(10,10),pady=(3,13),side=LEFT)

# Creating Button For Search Bar
button1 = ttk.Button(save,text='Browse',command=save_file)
button1.pack(padx=(0,10),pady=(3,13))

# Creating Frame4
frame4 = ttk.Frame(root,width=500)
frame4.pack(pady=(20,0))

# Creating Label
label1 = ttk.Label(frame4,text='',font=10,foreground='green')
label1.pack()

# Creating frame5
frame5 = ttk.Frame(root,width=500)
frame5.pack(pady=(20,0))

# Creating Button For Conversion
button2 = ttk.Button(frame5,text='Convert',command=convert)
button2.pack()

# Displaying The Window
root.mainloop()