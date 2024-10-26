from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from admin import *
from student import *
from teacher import *
class Login(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.l1=Label(self,text="User Name",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l2=Label(self,text="Password",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l3=Label(self,text="User Type",bg='light blue',fg='red',font=('algerian',14),bd=6)

        self.t1=Entry(self,bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.t2=Entry(self,show='*',bg='light blue',fg='red',font=('algerian',14),bd=6)
        choice={'admin','student','teacher'}
        self.val=StringVar(self)
        self.val.set("    Select Value     ")
        self.t3=OptionMenu(self,self.val,*choice)

        self.b1=Button(self,text='login',bg='light blue',fg='red',font=('algerian',14),bd=6,command=self.check)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)

        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)
        self.l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)

        self.l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)

        self.l3.grid(row=2,column=0)
        self.t3.grid(row=2,column=1)

        self.b1.grid(columnspan=2)
        self.pack()
    def check(self):
        con=connect(db='students',user='root',password='root',host='localhost')
        cur=con.cursor()
        uid=self.t1.get()
        pwd=self.t2.get()
        utype=self.val.get()
        cur.execute("select usertype from login where userid='%s' and password='%s' and usertype='%s'"%(uid,pwd,utype))
        result=cur.fetchall()
        if(result[0][0]=='admin'):
            root=Tk()
            ob=Administrator(root)
            root.title("Admin Panel")
            root.geometry('450x250')
            root.mainloop()
        elif(result[0][0]=='student'):
            root=Tk()
            ob=Student(root)
            root.title("Student Panel")
            root.geometry('450x250')
            root.mainloop()
        elif(result[0][0]=='teacher'):
            root=Tk()
            ob=Teacher(root)
            root.title("Teacher Panel")
            root.geometry('450x250')
            root.mainloop()
root=Tk()
ob=Login(root)
root.title('Student Management System')
root.geometry('450x250')
root.mainloop()