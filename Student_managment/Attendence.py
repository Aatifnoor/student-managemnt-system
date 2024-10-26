from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from datetime import *
class StudentAttendence(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.dt=datetime.now()
        self.ndate=str(self.dt.year)+"-"+str(self.dt.month)+"-"+str(self.dt.day)
        
        self.l1=Label(self,text="Student Id",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.t1=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.b1=Button(self,text='Present',bg='light blue',fg='red',font=('Arial',14),bd=6,justify="center",command=self.present)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)        

        self.l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)

        self.b1.grid(columnspan=2)
        self.pack()
    def present(self):
        con=connect(db='students',user='root',password='root',host='localhost')
        cur=con.cursor()
        sid=int(self.t1.get())
        i=cur.execute("insert into attendence values(%d,'%s')"%(sid,self.ndate))
        if(i==1):
            con.commit()
            self.t1.delete(0,'end')
