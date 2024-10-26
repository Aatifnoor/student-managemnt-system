from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from datetime import *
class StudentDelete(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.l1=Label(self,text="Student Id",bg='light blue',fg='red',font=('algerian',14),bd=6)
        
        self.t1=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.b1=Button(self,text='Delete',bg='light blue',fg='red',font=('Arial',14),bd=6,justify="center",command=self.remove)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)        

        self.l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)

        
        
        self.b1.grid(row=4,column=0)
        self.pack()
    def remove(self):
        con=connect(db='students',user='root',password='root',host='localhost')
        cur=con.cursor()
        sid=int(self.t1.get())
        i=cur.execute("delete from studentmaster where sid=%d"%(sid))
        if(i==1):
            ans=msg.askyesno('','Are You Sure to Remove?')
            if(ans==True):
                con.commit()
            else:
                msg.showinfo('','Try Again')
        