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

#root.resizable(0,0)

root.config(bg='gray96')

# Declaring The Size Of The Window
root.title('Image Compressor')

# Fixing The Size Of The Window
root.geometry('520x450')

# Creating Function to Open File
def openfile():
    entry1.delete(0,END)
    label1.config(text='')
    global filename
    filename = filedialog.askopenfilename(initialdir='/',title='Open File',
                                          filetypes=(('PNG','.png'),('JPG','.jpg'),('JPEG','.jpeg'),('BMP','.bmp'),('TIFF','.tiff'),('Tiff','.tif'),('All Files','*.*')))
    entry1.insert("0",filename)

# Creating Function to Convert File
def save_file():
    entry2.delete(0,END)
    dic={'PNG':'.png','JPG':'.jpg','JPEG':'.jpeg','BMP':'.bmp','TIFF(.tiff)':'.tiff','TIFF(.tif)':'.tif'}
    label1.config(text='')
    global savefile
    savefile = filedialog.asksaveasfile(defaultextension='.'+filename.rsplit(".",1)[1])
    entry2.insert("0", savefile.name)
    savefile.close()

def compress():
    from PIL import Image
    try:
        picture = Image.open(filename)
        picture.save(savefile.name, optimize=True, quality=int(entry3.get()))
        label1.config(text='Image Compressed Successfully...!',foreground='green')
    except:
        label1.config(text='Image Not Compressed Successfully...!',foreground='red')

# Creating A frame
frame1 = ttk.Frame(root,width=500)
frame1.pack()

# Creating Label
title = ttk.Label(frame1,text='IMAGE COMPRESSOR',font=('timesnewroman',20,'bold'),foreground='gray')
title.pack(pady=(10,15))

# Creating frame2
frame2 = ttk.Frame(root,width=500)
frame2.pack(pady=(10,10))

# Creating Labelframe
browse = ttk.LabelFrame(frame2,text='Choose Image')
browse.pack(side=LEFT,padx=10)

# Creating Label For Search Bar
entry1 = ttk.Entry(browse,width=30)
entry1.pack(padx=(10,10),pady=(3,13),side=LEFT)

# Creating Button For Search Bar
button = ttk.Button(browse,text='Browse',command=openfile)
button.pack(padx=(0,10),pady=(3,13))

# Creating Frame3
frame3 = ttk.Frame(root,width=500)
frame3.pack(pady=(10,10))

# Creating Label
convert_label = ttk.Label(frame3,text='Compress Percentage: ')
convert_label.pack(side=LEFT,padx=(0,10))

# Creating Scale Bar and variable
var = DoubleVar()

def scale_value(value):
    label1.config(text='')
    entry3.config(state=NORMAL)
    entry3.delete(0,END)
    entry3.insert('0',int(float(value)))
    entry3.config(state='readonly')

scale = ttk.Scale(frame3,variable=var,orient=HORIZONTAL,command=scale_value,from_=1,to=100)
scale.pack(side=LEFT,padx=(10,0))

# Creating Entry
entry3 = ttk.Entry(frame3,width=10)
entry3.pack(padx=(20,0))
entry3.config(state='readonly')

# Creating frame4
frame4 = ttk.Frame(root,width=500)
frame4.pack(pady=(10,5))

# Creating Labelframe
save = ttk.LabelFrame(frame4,text='Location To Save The Image')
save.pack(side=LEFT,padx=10)

# Creating Label For Search Bar
entry2 = ttk.Entry(save,width=30)
entry2.pack(padx=(10,10),pady=(3,13),side=LEFT)

# Creating Button For Search Bar
button1 = ttk.Button(save,text='Browse',command=save_file)
button1.pack(padx=(0,10),pady=(3,13))

# Creating Frame 5
frame5 = ttk.Frame(root,width=500)
frame5.pack(pady=(0,10))

label1 = ttk.Label(frame5,text='')
label1.pack(pady=(10,20))
button3 = ttk.Button(frame5,text='Convert',command=compress)
button3.pack()

# Displaying The Window
root.mainloop()
