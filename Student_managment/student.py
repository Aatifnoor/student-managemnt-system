from FeePaid import *
from ShowMarks import *
from tkinter import *
from tkinter import messagebox as msg
from PasswordCange import *
from pymysql import *
class Student(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.b1=Button(self,text="Show Marks",bg='light blue',fg='red',font=('algerian',14),bd=6,command=self.show1)
        self.b2=Button(self,text="Change Password",bg='light blue',fg='red',font=('algerian',14),bd=6,command=self.show4)
        self.b3=Button(self,text="Fee paid",bg='light blue',fg='red',font=('algerian',14),bd=6,command=self.show2)
        self.b4=Button(self,text="Exit",bg='light blue',fg='red',font=('algerian',14),bd=6,command=self.close)

        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)

        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)

        self.b1.grid(row=0,column=0)
        self.b2.grid(row=0,column=1)
        
        self.b3.grid(row=1,column=0)
        self.b4.grid(row=1,column=1)

        self.pack()
    def close(self):
        exit()
    def show4(self):
        root=Tk()
        ob=ChangePassword(root)
        root.title('Password Change')
        root.geometry('450x250')
        root.mainloop()
    def show1(self):
        root=Tk()
        ob=MarkShow(root)
        root.title('MArks Form')
        root.geometry('450x250')
        root.mainloop()
    def show2(self):
        root=Tk()
        ob=PaidFee(root)
        root.title('MArks Form')
        root.geometry('450x250')
        root.mainloop()
