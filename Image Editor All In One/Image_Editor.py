from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog
import os

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = ThemedTk()
root.resizable(0,0)
root.get_themes()
root.set_theme('radiance')

photo = PhotoImage(file='download.png')
root.iconphoto(False,photo)

root.title('Image Editor')
root.geometry('600x550')

tab_obj = ttk.Notebook(root)
tab_obj.pack(fill=BOTH,expand=True)

frame4 = Frame(tab_obj,width=600,height=550,background='white')
frame4.pack()

img = ttk.Label(frame4,image=photo)
img.place(x=360,y=50)
tab4 = tab_obj.add(frame4,text='About')

intro = Label(frame4,text='AJ INDUSTRIES',font=('timesnewroman',20,'bold'),bg='white')
intro.place(x=170,y=10)
founder = Label(frame4,text='FOUNDER',font=('timesnewroman',10,'bold'),bg='white')
founder.place(x=20,y=90)
name = Label(frame4,text='Adhavan Janarthanan (AJ)',font=('timesnewroman',10,'italic'),bg='white')
name.place(x=60,y=120)
contact = Label(frame4,text='Reach Me @ : adhi.jana02@gmail.com',font=('timesnewroman',10),bg='white')
contact.place(x=60,y=150)
about = Label(frame4,text='APPLICATION DETAILS',font=('timesnewroman',10,'bold'),bg='white')
about.place(x=20,y=180)
img_com = Label(frame4,text='Image Compressor:',font=('timesnewroman',10,'bold'),bg='white')
img_com.place(x=40,y=210)
abt_img_com = Label(frame4,text='IMAGE COMPRESSOR compress the given image to a required size.',font=('timesnewroman',10),bg='white')
abt_img_com.place(x=60,y=240)
img_con = Label(frame4,text='Image Convertor:',font=('timesnewroman',10,'bold'),bg='white')
img_con.place(x=40,y=270)
img_con_abt = Label(frame4,text='IMAGE CONVERTOR has a ability to convert the given image to a ',font=('timesnewroman',10),bg='white')
img_con_abt.place(x=60,y=300)
img_con_abt_con = Label(frame4,text='required format and also has a ability to resize the Image.',font=('timesnewroman',10),bg='white')
img_con_abt_con.place(x=40,y=330)
pdf_con = Label(frame4,text='PDF Convertor:',font=('timesnewroman',10,'bold'),bg='white')
pdf_con.place(x=40,y=360)
pdf_con_abt = Label(frame4,text='PDF CONVERTER converts the given document to a PDF Document.',font=('timesnewroman',10),bg='white')
pdf_con_abt.place(x=60,y=390)
frame1 = ttk.Frame(tab_obj,width=600,height=550)
frame1.pack()

tab1 = tab_obj.add(frame1,text='Image Compressor')

# Image Compressor
# Creating Function to Open File
def openfile_com():
    entry1.delete(0,END)
    entry2.delete(0,END)
    label1.config(text='')
    global filename
    filename = filedialog.askopenfilename(initialdir='/',title='Open File',
                                          filetypes=(('JPEG','.jpeg'),('PNG','.png'),('JPG','.jpg'),('BMP','.bmp'),('TIFF','.tiff'),('Tiff','.tif'),('All Files','*.*')))
    if filename != None:
        entry1.insert("0",filename)

# Creating Function to Convert File
def save_file_com():
    entry2.delete(0,END)
    dic={'PNG':'.png','JPG':'.jpg','JPEG':'.jpeg','BMP':'.bmp','TIFF(.tiff)':'.tiff','TIFF(.tif)':'.tif'}
    label1.config(text='')
    global savefile
    try:
        savefile = filedialog.asksaveasfile(defaultextension='.'+filename.rsplit(".",1)[1])
    except:
        savefile = filedialog.asksaveasfile(defaultextension='.jpeg')
    if savefile.name != None:
        entry2.insert("0", savefile.name)
    savefile.close()

def compress():
    from PIL import Image
    if savefile.name != entry2.get():
        os.remove(savefile.name)
    try:
        picture = Image.open(entry1.get())
        picture.save(entry2.get(), optimize=True, quality=int(entry3.get()))
        label1.config(text='Image Compressed Successfully...!',foreground='green')
    except:
        os.remove(entry2.get())
        label1.config(text='Image Not Compressed Successfully...!',foreground='red')

# Creating Label
title = ttk.Label(frame1,text='IMAGE COMPRESSOR',font=('timesnewroman',20,'bold'),foreground='gray')
title.place(x=110,y=10)

# Creating Labelframe
browse = ttk.LabelFrame(frame1,text='Choose Image')
browse.place(x=90,y=80)

# Creating Label For Search Bar
entry1 = ttk.Entry(browse,width=30)
entry1.pack(padx=(10,10),pady=(3,13),side=LEFT)

# Creating Button For Search Bar
button = ttk.Button(browse,text='Browse',command=openfile_com)
button.pack(padx=(0,10),pady=(3,13))

# Creating Label
convert_label = ttk.Label(frame1,text='Compress Percentage: ')
convert_label.place(x=90,y=190)

# Creating Scale Bar and variable
var = DoubleVar()

def scale_value(value):
    label1.config(text='')
    entry3.config(state=NORMAL)
    entry3.delete(0,END)
    entry3.insert('0',int(float(value)))
    entry3.config(state='readonly')

scale = ttk.Scale(frame1,variable=var,orient=HORIZONTAL,command=scale_value,from_=1,to=100)
scale.place(x=300,y=190)

# Creating Entry
entry3 = ttk.Entry(frame1,width=10)
entry3.place(x=430,y=190)
entry3.config(state='readonly')

# Creating Labelframe
save = ttk.LabelFrame(frame1,text='Location To Save The Image')
save.place(x=90,y=250)

# Creating Label For Search Bar
entry2 = ttk.Entry(save,width=30)
entry2.pack(padx=(10,10),pady=(3,13),side=LEFT)

# Creating Button For Search Bar
button1 = ttk.Button(save,text='Browse',command=save_file_com)
button1.pack(padx=(0,10),pady=(3,13))

label1 = ttk.Label(frame1,text='')
label1.place(x=150,y=370)
button3 = ttk.Button(frame1,text='Compress',command=compress)
button3.place(x=220,y=430)
# --------------------------------------------------------------------------------
def openfile():
    eentry1.delete(0,END)
    eentry2.delete(0,END)
    llabel1.config(text='')
    global filename1
    filename1 = filedialog.askopenfilename(initialdir='/',title='Open File',
                                          filetypes=(('JPEG','.jpeg'),('PNG','.png'),('JPG','.jpg'),('BMP','.bmp'),('TIFF','.tiff'),('Tiff','.tif'),('All Files','*.*')))
    if filename1 != None:
        eentry1.insert("0",filename1)

def save_file():
    eentry2.delete(0,END)
    dic={'PNG':'.png','JPG':'.jpg','JPEG':'.jpeg','BMP':'.bmp','TIFF(.tiff)':'.tiff','TIFF(.tif)':'.tif'}
    llabel1.config(text='')
    global savefile1
    savefile1 = filedialog.asksaveasfile(defaultextension=dic[com.get()])
    if savefile1.name != None:
        eentry2.insert("0", savefile1.name)
    savefile1.close()

def convert():
    llabel1.config(text='')
    try:
        import cv2
        img = cv2.imread(eentry1.get(), 1)
        cv2.imwrite(eentry2.get(), img)
        if check.get()!=0:
            img1 = cv2.imread(eentry2.get(), 1)
            img1 = cv2.resize(img1, (int(width_entry.get()),int(height_entry.get())))
            cv2.imwrite(eentry2.get(),img1)
            llabel1.config(text='Successfully Converted And Resized The Image!',foreground='green')
        else:
            llabel1.config(text='Successfully Converted The Image!', foreground='green')
    except:
        os.remove(eentry2.get())
        llabel1.config(text='Image Not Converted Successfully...  !',foreground='red')

frame2 = ttk.Frame(tab_obj,width=600,height=550)
frame2.pack()

# Creating Label
title = ttk.Label(frame2,text='IMAGE CONVERTOR',font=('timesnewroman',20,'bold'),foreground='gray')
title.place(x=140,y=10)

# Creating Labelframe
browse = ttk.LabelFrame(frame2,text='Choose Image')
browse.place(x=90,y=80)

# Creating Label For Search Bar
eentry1 = ttk.Entry(browse,width=30)
eentry1.pack(padx=(10,10),pady=(3,13),side=LEFT)

# Creating Button For Search Bar
bbutton = ttk.Button(browse,text='Browse',command=openfile)
bbutton.pack(padx=(0,10),pady=(3,13))

# Creating Label
convert_label = ttk.Label(frame2,text='Convert To: ')
convert_label.place(x=140,y=190)

# Creating Combo Box and variable
com = StringVar()
com.set('JPEG')
com_box = ttk.Combobox(frame2,textvariable=com,values=('JPG','JPEG','PNG','BMP','TIFF(.tif)','TIFF(.tiff)'))
com_box.place(x=250,y=190)
com_box.config(state='readonly')

# Creating Labelframe
save = ttk.LabelFrame(frame2,text='Location To Save The Image')
save.place(x=90,y=250)

# Creating Label For Search Bar
eentry2 = ttk.Entry(save,width=30)
eentry2.pack(padx=(10,10),pady=(3,13),side=LEFT)

# Creating Button For Search Bar
bbutton1 = ttk.Button(save,text='Browse',command=save_file)
bbutton1.pack(padx=(0,10),pady=(3,13))

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
check_button = ttk.Checkbutton(frame2,text='Resize Image',variable=check,command=dis)
check_button.place(x=30,y=350)

width_label = ttk.Label(frame2,text='Width: ')
width_label.place(x=210,y=350)

width_entry = ttk.Entry(frame2,width=10)
width_entry.place(x=270,y=350)
width_entry.config(state='readonly')

height_label = ttk.Label(frame2,text='  Height: ')
height_label.place(x=370,y=350)

height_entry = ttk.Entry(frame2,width=10)
height_entry.place(x=450,y=350)
height_entry.config(state='readonly')

llabel1 = ttk.Label(frame2,text='')
llabel1.place(x=140,y=410)
button3 = ttk.Button(frame2,text='Convert',command=convert)
button3.place(x=230,y=450)

tab2 = tab_obj.add(frame2,text='Image Converter')

# -------------------------------------------------------------------------------------------------------------
#Tab 3

def openfile_pdf():
    eeentry1.delete(0,END)
    eeentry2.delete(0,END)
    lllabel1.config(text='')
    global filename2
    filename2 = filedialog.askopenfilename(initialdir='/',title='Open File',
                                          filetypes=(('Word File','.docx'),('All Files','*.*')))
    if filename2 != None:
        eeentry1.insert("0",filename2)

def save_file_pdf():
    eeentry2.delete(0,END)
    dic={'PNG':'.png','JPG':'.jpg','JPEG':'.jpeg','BMP':'.bmp','TIFF(.tiff)':'.tiff','TIFF(.tif)':'.tif'}
    lllabel1.config(text='')
    global savefile1
    savefile2 = filedialog.asksaveasfile(defaultextension='.pdf')
    if savefile2.name != None:
        eeentry2.insert("0", savefile2.name)
    savefile2.close()

def convert_pdf():
    lllabel1.config(text='')
    try:
        from docx2pdf import convert
        if len(eeentry1.get())<2 or len(eeentry2.get())<2:
            if "0"+1:
                pass
        convert(eeentry1.get(),eeentry2.get())
        lllabel1.config(text='Successfully Converted The Document...!',foreground='green')
    except:
        lllabel1.config(text='Document Not Converted Successfully...!',foreground='red')

frame3 = ttk.Frame(tab_obj,width=600,height=550)
frame3.pack()

title = ttk.Label(frame3,text='PDF CONVERTOR',font=('timesnewroman',20,'bold'),foreground='gray')
title.place(x=140,y=10)

# Creating Labelframe
browse = ttk.LabelFrame(frame3,text='Choose A File')
browse.place(x=90,y=80)

# Creating Label For Search Bar
eeentry1 = ttk.Entry(browse,width=30)
eeentry1.pack(padx=(10,10),pady=(3,13),side=LEFT)

# Creating Button For Search Bar
bbbutton = ttk.Button(browse,text='Browse',command=openfile_pdf)
bbbutton.pack(padx=(0,10),pady=(3,13))

save = ttk.LabelFrame(frame3,text='Location To Save The File')
save.place(x=90,y=180)

# Creating Label For Search Bar
eeentry2 = ttk.Entry(save,width=30)
eeentry2.pack(padx=(10,10),pady=(3,13),side=LEFT)

# Creating Button For Search Bar
bbbutton1 = ttk.Button(save,text='Browse',command=save_file_pdf)
bbbutton1.pack(padx=(0,10),pady=(3,13))

lllabel1 = ttk.Label(frame3,text='')
lllabel1.place(x=140,y=300)
bbbutton3 = ttk.Button(frame3,text='Convert',command=convert_pdf)
bbbutton3.place(x=230,y=350)

tab3 = tab_obj.add(frame3,text='PDF Converter')

root.mainloop()
