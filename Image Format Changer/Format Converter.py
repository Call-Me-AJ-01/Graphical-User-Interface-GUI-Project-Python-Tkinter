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
root.title('Image Editor')

# Fixing The Size Of The Window
root.geometry('500x500')

# Creating Function to Open File
def openfile():
    label1.config(text='')
    global filename
    filename = filedialog.askopenfilename(initialdir='/',title='Open File',
                                          filetypes=(('PNG','.png'),('JPG','.jpg'),('JPEG','.jpeg'),('BMP','.bmp'),('TIFF','.tiff'),('Tiff','.tif'),('All Files','*.*')))
    entry1.insert("0",filename)

# Creating Function to Convert File
def save_file():
    dic={'PNG':'.png','JPG':'.jpg','JPEG':'.jpeg','BMP':'.bmp','TIFF(.tiff)':'.tiff','TIFF(.tif)':'.tif'}
    label1.config(text='')
    global savefile
    savefile = filedialog.asksaveasfile(defaultextension=dic[com.get()])
    entry2.insert("0", savefile.name)
    savefile.close()

def convert():
    label1.config(text='')
    try:
        import cv2
        img = cv2.imread(entry1.get(), 1)
        cv2.imwrite(entry2.get(), img)
        if check.get()!=0:
            img1 = cv2.imread(entry2.get(), 1)
            img1 = cv2.resize(img1, (int(width_entry.get()),int(height_entry.get())))
            cv2.imwrite(entry2.get(),img1)
            label1.config(text='Successfully Converted And Resized The Image!',foreground='green')
        else:
            label1.config(text='Successfully Converted The Image!', foreground='green')
    except:
        label1.config(text='Image Not Converted Successfully...!',foreground='red')

# Creating A frame
frame1 = ttk.Frame(root,width=500)
frame1.pack()

# Creating Label
title = ttk.Label(frame1,text='IMAGE EDITOR',font=('timesnewroman',20,'bold'),foreground='gray')
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
convert_label = ttk.Label(frame3,text='Convert To: ')
convert_label.pack(side=LEFT,padx=(0,10))

# Creating Combo Box and variable
com = StringVar()
com.set('JPEG')
com_box = ttk.Combobox(frame3,textvariable=com,values=('JPG','JPEG','PNG','BMP','TIFF(.tif)','TIFF(.tiff)'))
com_box.pack(padx=(10,0))
com_box.config(state='readonly')

# Creating frame4
frame4 = ttk.Frame(root,width=500)
frame4.pack(pady=(10,10))

# Creating Labelframe
save = ttk.LabelFrame(frame4,text='Location To Save The Image')
save.pack(side=LEFT,padx=10)

# Creating Label For Search Bar
entry2 = ttk.Entry(save,width=30)
entry2.pack(padx=(10,10),pady=(3,13),side=LEFT)

# Creating Button For Search Bar
button1 = ttk.Button(save,text='Browse',command=save_file)
button1.pack(padx=(0,10),pady=(3,13))

# Creating Frame5
frame5 = ttk.Frame(root,width=500)
frame5.pack(pady=(10,10))

def dis():
    if check.get()!=0:
        width_entry.config(state=NORMAL)
        height_entry.config(state=NORMAL)
    else:
        width_entry.config(state='readonly')
        height_entry.config(state='readonly')

# Creating Check Button
check = IntVar()
check.set(0)
check_button = ttk.Checkbutton(frame5,text='Resize Image',variable=check,command=dis)
check_button.pack(side=LEFT,padx=(0,15))

width_label = ttk.Label(frame5,text='Width: ')
width_label.pack(side=LEFT)

width_entry = ttk.Entry(frame5,width=10)
width_entry.pack(side=LEFT)
width_entry.config(state='readonly')

height_label = ttk.Label(frame5,text='  Height: ')
height_label.pack(side=LEFT)

height_entry = ttk.Entry(frame5,width=10)
height_entry.pack()
height_entry.config(state='readonly')

# Creating Frame 6
frame6 = ttk.Frame(root,width=500)
frame6.pack(pady=(10,10))

label1 = ttk.Label(frame6,text='')
label1.pack(pady=(10,20))
button3 = ttk.Button(frame6,text='Convert',command=convert)
button3.pack()

# Displaying The Window
root.mainloop()