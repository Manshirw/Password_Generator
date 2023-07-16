#password generater 
from tkinter import *  #importing module
import random, string

# initializing window

root = Tk()            
root.geometry("700x400") 
root.resizable(0,0)
root.title(" STRONG PASSWORD GENERATOR ")
# display content in window

Label(root, text = 'PASSWORD GENERATOR' , font =' algerian 15 bold').pack()
Label(root, text = 'SECURITY AS PRIORITY', font ='arial 15 bold').pack(side = BOTTOM)
# select password length 
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 6 , to_ = 30 , textvariable = pass_len , width = 15).pack()

#function to create password 
pass_str = StringVar()
def Generator():
    password = ''

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()
mainloop()