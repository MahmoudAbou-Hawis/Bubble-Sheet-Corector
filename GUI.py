from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import Cropping
import Degree
import cv2
import pytesseract as tes

import EditSheet
root = Tk()
root.title("Bubble Sheet Corrector")
root.geometry("1350x700+0+0")

title = Label(root, text="Bubble Sheet Corrector", font=("times new roman", 30, "bold"), bg="#9900FF")
title.pack(side=TOP)

frame = LabelFrame(root, text="Menu", padx=10, pady=10, bd=8, bg='#FFCCFF')
frame.place(x=20, y=70, width=300, height=400)

frame1 = LabelFrame(root, text="perveiw", padx=10, pady=10, relief="solid")
frame1.place(x=380, y=70, width=700, height=500)

frame2 = LabelFrame(root, text="Parameters", padx=10, pady=10, bd=8, bg='#FFCCFF')
frame2.place(x=20, y=500, width=300, height=150)
lbl1= Label(frame2,text="Result:",fg='blue',font=(10))
lbl1.grid(row=0,column=0,padx=10,pady=10)
lbl2=Label(frame2,text="",fg='red',font=(25))
lbl2.grid(row=0,column=2,padx=10,pady=10)


panelA = None
Button1 = Button(frame, text="Browse Correct Answers", bg='#CC33CC', font=('Arial', 12, 'bold'),
                 command=lambda: upload_file())
Button1.place(x=45, y=30, width=200, height=40)


def upload_file():
    global panelA
    filename = filedialog.askopenfilename()
    if len(filename) > 0:
        im1 = cv2.imread(filename)
        im1 = Image.fromarray(im1)
        im1.thumbnail((500, 500))
        im1 = ImageTk.PhotoImage(im1)

        if panelA is None:
            panelA = Label(image=im1)
            panelA.image = im1
            panelA.pack(padx=10, pady=10)
            panelA.place(x=380, y=70, width=700, height=500)
        else:
            panelA = Label(image=im1)
            panelA.image = im1
            panelA.pack(padx=10, pady=10)
            panelA.place(x=380, y=70, width=700, height=500)
            # panelA.configure(image=im1)
            # panelA.place(x=380, y=70, width=700, height=500)
    p1 = Cropping.Cropping(filename)
    global x
    x = p1.run()
    print(x)

def upload_file2():
    global panelB
    global filename_2
    filename_2 = filedialog.askopenfilename()
    if len(filename_2) > 0:
        im1 = cv2.imread(filename_2)

        im1 = Image.fromarray(im1)
        im1.thumbnail((500, 500))
        im1 = ImageTk.PhotoImage(im1)

        if panelB is None:
            panelB = Label(image=im1)
            panelB.image = im1
            panelB.pack(padx=10, pady=10)
            panelB.place(x=380, y=70, width=700, height=500)
        else:
            panelB = Label(image=im1)
            panelB.image = im1
            panelB.pack(padx=10, pady=10)
            panelB.place(x=380, y=70, width=700, height=500)
            # panelB.configure(image=im1)
            # panelB.place(x=380, y=70, width=700, height=500)
    global p2
    p2 = Cropping.Cropping(filename_2)
    global y
    y = p2.run()
    print(y)

def button3_event():
    Corrct_list = y[0:len(y) // 2]
    Answer_list = y[len(y) // 2:len(y) - 1]
    g = Degree.Degree(Answer_list, Corrct_list)
    x_R = g.get_degree()
    total = 0
    for i in Answer_list:
        total += len(i)
    print(x_R, 'from ', total)
    lbl2.config(text=str(x_R))

    p2.Cropping_Result.clear()
    p2.Cropping_Result.append([])
    img=cv2.imread(filename_2)
    a,b,c,d=cv2.selectROI('select rois',img)

    im_cropped1=img[int(b):int(b+d),int(a):int(a+c)]
    cv2.imshow("cropped",im_cropped1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    id =tes.image_to_string(im_cropped1,lang='eng',config='--psm 6')
    edit = EditSheet.AddToSheet('/home/sofar/Documents/file.csv')
    edit.add_degree(str(id[0]),str(x_R))
    print(id[0])
panelB = None
Button2 = Button(frame, text="Browse Student Answers", bg='#CC33CC', font=('Arial', 12, 'bold'), command=upload_file2)
Button2.place(x=45, y=110, width=200, height=40)

Button3 = Button(frame, text="Calculate Result", bg='#CC33CC', font=('Arial', 12, 'bold'),command=button3_event)
Button3.place(x=45, y=180, width=200, height=40)

Button4 = Button(frame, text="Exit", bg='#9966FF', font=('Arial', 12, 'bold'), command=root.quit)
Button4.place(x=45, y=250, width=200, height=40)

root.mainloop()