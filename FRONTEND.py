from tkinter import *
import tkinter.filedialog
from PIL import ImageTk,Image

def open_file():
          global open_file_name
          
          image_file_name = tkinter.filedialog.askopenfilename(defaultextension=".png", filetypes=[("Image Files", "*.png")])
          open_file_name=ImageTk.PhotoImage(Image.open(image_file_name))
          #.configue run time pe change karna tau is se karwa sakty(label.configure name ko display kra de ga)
          label_1.configure(image=open_file_name)   
          
mood=Tk()
mood.title("Food Selection By Mood Detection")

width_win=500
height_win=600

screen_width=mood.winfo_screenwidth()
screen_height=mood.winfo_screenheight()

x_cord = (screen_width/2)-(width_win/2)
y_cord = (screen_height/2)-(height_win/2)

mood.geometry('%dx%d+%d+%d' %(width_win,height_win,x_cord,y_cord-15))

background_image= PhotoImage(file='landscape.png')
#background_label=Label(mood, image=background_image)
background_image.place(relwidth=1, relheight=1)

frame = Frame(mood, bd = 5,bg='red', highlightbackground = "maroon", highlightcolor = "red", highlightthickness = 3)
frame.place(relx=0.5, rely=0.08, relwidth=0.6, relheight=0.1, anchor='n')

label= Label (frame, text='Food Selection By Mood Detection', bg="red",fg="white", font="none 12 bold")
label.place(relwidth=1 , relheight=1)

image_frame=Frame(mood,bd=5, bg='maroon')
image_frame.place(relx=0.5, rely=0.23, relwidth=0.6, relheight=0.35, anchor='n')

img= Image.open("C://Users//hp//AppData//Local//Programs//Python//Python36//upload.png")
img = img.resize((290,200), Image.ANTIALIAS)
open_file_name= ImageTk.PhotoImage(img)

label_1=Label(image_frame,image=open_file_name)
label_1.pack()

label_frame=Frame(mood,bd=5, bg='maroon')
label_frame.place(relx=0.5, rely=0.63, relwidth=0.6, relheight=0.1, anchor='n')

label= Label (label_frame, text='MOOD', bg="red",fg="white", font="none 15 bold")
label.place(relwidth=1 , relheight=1)

btn_frame=Frame(mood)
btn_frame.place(relx=0.5, rely=0.78, relwidth=0.35, relheight=0.1, anchor='n')

button=Button(btn_frame,text="ADD IMAGE",font=30, bg="yellow", fg="red",command=open_file)
button.place(relx=0.5, relheight=1, relwidth=1, anchor='n')

mood.bind("<Return>", open_file)
mood.mainloop()
