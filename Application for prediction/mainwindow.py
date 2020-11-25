from tkinter import *
from tkinter import filedialog,messagebox
import numpy as np
from tkinter import ttk

from PIL import Image,ImageTk, ImageSequence
from time import sleep
import os
root=Tk()
root.title('Anomaly Based IDS')
root.geometry('437x768+700+100')
root.resizable(width=False, height=False)


#prediction
def prediction(dataset):
    import numpy as np
    import pandas as pd
    import pickle
    global c
    model=pickle.load(open('modelfordemo.pickle','rb'))
    results=model.predict(pd.read_csv(dataset).drop('Unnamed: 0',axis=1))
    c=0
    for i in results:
        if i ==1:
            c+=1


#file explorer
def data_set():
    global dataset
    root.filename=filedialog.askopenfilename(initialdir='/Users/priya/Desktop/FINAL',title='Select A File',filetype=(("CSV File","*.csv"),("All files","*.*"))) 
    dataset=os.path.basename(root.filename)

def scan():
    prediction(dataset)
   
    win = Toplevel()
    l1= Label(win, text='Scanning Data Packets....')
    l1.place(relx=0.0, rely=1.0, anchor='sw')
    l1.config(font=('Aerial' ,23))
    win.title('Scanning Data Packets')
    win.geometry('600x500+700+100')
    canvas =Canvas(win,height=450,width=600)
    canvas.pack()
    sequence = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                                Image.open(
                                r'loading.gif'))]
    image = canvas.create_image(310,230,image=sequence[0])
    def animate(counter):
        canvas.itemconfig(image, image=sequence[counter])
        win.after(20, lambda: animate((counter+1) % len(sequence)))
    animate(1)
    def afterfunc():
        win.destroy()
        
        finalresult()
        

        
    win.after(8000,afterfunc)
    
def finalresult():    
    if c==0:
        messagebox.showinfo("Scan Results", "Scan Complete \nNo Anomaly Detected\nSystem is Safe!")
    else:
        messagebox.showerror("Scan Results",("WARNING \n"+str(c)+" Unsafe Packet(s) Detected!\nTake Action Immediately") )



    


load=Image.open('background.jpg')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img1=PhotoImage(file='button.png')
btn1=Button(root,image=img1,bd=0,bg='#121418',activebackground='#121418',command=data_set)
btn1.place(relx=.5, rely=.55, anchor="center")
img.place(x=0,y=0)
img2=PhotoImage(file='button1.png')
btn2=Button(root,image=img2,bd=0,bg='#121418',activebackground='#121418',command=scan)
btn2.place(relx=.5, rely=.65, anchor="center")


root.mainloop()
