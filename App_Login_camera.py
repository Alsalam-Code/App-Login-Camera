from tkinter import *

# App 1
root = Tk()
root.geometry('300x500')
root.title('Alsalam')
root.iconbitmap("image/logo2.ico")
root.resizable(False,False)
# root.attributes('-alpha',0.8)
#============== Define ==========
def one(enent=None):
  En1.insert(END,1)
def tow(enent=None):
  En1.insert(END,2)
def three(enent=None):
  En1.insert(END,3)
def fur(enent=None):
  En1.insert(END,4)
def five(enent=None):
  En1.insert(END,5)
def six(enent=None):
  En1.insert(END,6)
def seven(enent=None):
  En1.insert(END,7)
def et(enent=None):
  En1.insert(END,8)
def nine(enent=None):
  En1.insert(END,9)
def ten(enent=None):
  En1.insert(END,0)

def Del():
    En1.delete('0',END)
    Error.place(x=1000,y=1000)
def ok(enent=None):
    passow = En1.get()
    if passow == '5':
      win = Tk()
      win.geometry('300x300')
      win.title('alsalam')
      win.iconbitmap("image/logo2.ico")
      text = Label(win, text='yousef')
      text.pack()
      win.mainloop()
    else:
      global Error
      Error = Label(F1,text='Error Password!',fg='red', bg='#2C3E50', font=(17))
      Error.place(x=100,y=50)
      
#-------------- title -----------
title = Label(root, text='الدخول ممنوع', fg='white', bg='#D82148', font=('Stencil',22))
title.pack(fill=X)
#-------------- fram ------------
F1 = Frame(root, bg='#2C3E50')
F1.place(x=0, y=40,width=301,height=460)

title1 = Label(F1, text='Enter Password',fg='black', bg='white',font=('Arial Black',15))
title1.place(x=59, y=10)

En1 = Entry(F1, justify=CENTER, font=('Imact',25),bd=3,relief=RIDGE,width=14,bg='white',fg='black')
En1.place(x=21, y=77)
#============== Button ===========
Bt1 = Button(F1, text='1', fg='#F7F9F9', bg='black',bd=0,relief=GROOVE,cursor='hand2', font=('Impact',23),command=one)
Bt1.place(x=30, y=135, width=60, height=60)
Bt2 = Button(F1, text='2', fg='#F7F9F9', bg='black',cursor='hand2',bd=0, font=('Impact',23),command=tow)
Bt2.place(x=120, y=135, width=60, height=60)
Bt3 = Button(F1, text='3', fg='#F7F9F9', bg='black',bd=0,cursor='hand2', font=('Impact',23),command=three)
Bt3.place(x=210, y=135, width=60, height=60)

Bt4 = Button(F1, text='4', fg='#F7F9F9',cursor='hand2', bg='black',bd=0, font=('Impact',23),command=fur)
Bt4.place(x=30, y=220, width=60, height=60)
Bt5 = Button(F1, text='5', fg='#F7F9F9', bg='black',bd=0,cursor='hand2', font=('Impact',23),command=five)
Bt5.place(x=120, y=220, width=60, height=60)
Bt6 = Button(F1, text='6', fg='#F7F9F9', bg='black',bd=0,cursor='hand2', font=('Impact',23),command=six)
Bt6.place(x=210, y=220, width=60, height=60)

Bt7 = Button(F1, text='7', fg='#F7F9F9', bg='black',bd=0,cursor='hand2', font=('Impact',23),command=seven)
Bt7.place(x=30, y=300, width=60, height=60)
Bt8 = Button(F1, text='8', fg='#F7F9F9', bg='black',bd=0,cursor='hand2', font=('Impact',23),command=et)
Bt8.place(x=120, y=300, width=60, height=60)
Bt9 = Button(F1, text='9', fg='#F7F9F9', bg='black',bd=0,cursor='hand2', font=('Impact',23),command=nine)
Bt9.place(x=210, y=300, width=60, height=60)

Bt10 = Button(F1, text='0', fg='#0900FF',cursor='hand2', bg='black',bd=0, font=('Impact',23),command=ten)
Bt10.place(x=120, y=380, width=60, height=60)
Xl = Button(F1, text='❌', fg='#C2000A', bg='black', font=('Stencil',23),cursor='hand2',command=Del)
Xl.place(x=30, y=380, width=60, height=60)
OK = Button(F1, text='✔', fg='#196F3D', bg='black',cursor='hand2', font=('Stencil',23),command=ok)
OK.place(x=210, y=380, width=60, height=60)

input('Done')
root.mainloop()
