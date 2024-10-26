from PasswordCange import *
from SearchStudent import *
from DeleteStudent import *
from FeeCollection import *
from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from admission import *
class Administrator(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.b1=Button(self,text='Admission',bg='light blue',fg='red',font=('algerian',14),bd=6,command=self.show)
        self.b2=Button(self,text='Fee Collection',bg='light blue',fg='red',font=('algerian',14),bd=6,command=self.show2)
        self.b3=Button(self,text='Delete Student',bg='light blue',fg='red',font=('algerian',14),bd=6,command=self.show3)
        self.b4=Button(self,text='Password Change',bg='light blue',fg='red',font=('algerian',14),bd=6,command=self.show4)
        self.b5=Button(self,text='Search Student',bg='light blue',fg='red',font=('algerian',14),bd=6,command=self.show5)
        self.b6=Button(self,text='Exit',bg='light blue',fg='red',font=('algerian',14),bd=6,command=self.close)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)

        self.b1.grid(row=0,column=0)
        self.b2.grid(row=0,column=1)

        self.b3.grid(row=1,column=0)
        self.b4.grid(row=1,column=1)

        self.b5.grid(row=2,column=0)
        self.b6.grid(row=2,column=1)

        self.pack()
    def close(self):
        exit()
    def show(self):
        root=Tk()
        ob=Admission(root)
        root.title('Registration')
        root.geometry('450x700')
        root.mainloop()
    def show2(self):
        root=Tk()
        ob=StudentFee(root)
        root.title('Fee Form')
        root.geometry('450x300')
        root.mainloop()
    def show3(self):
        root=Tk()
        ob=StudentDelete(root)
        root.title('Delete Form')
        root.geometry('450x200')
        root.mainloop()
    def show4(self):
        root=Tk()
        ob=ChangePassword(root)
        root.title('Password Change')
        root.geometry('450x250')
        root.mainloop()
    def show5(self):
        root=Tk()
        ob=StudentSearch(root)
        root.title('Search Student')
        root.geometry('450x250')
        root.mainloop()