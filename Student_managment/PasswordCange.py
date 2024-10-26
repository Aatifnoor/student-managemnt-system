from tkinter import *
from tkinter import messagebox as msg
from pymysql import *

class ChangePassword(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.l1=Label(self,text="Login Id",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l2=Label(self,text="Old Password",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l3=Label(self,text="New Password",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l4=Label(self,text="Confirm Password",bg='light blue',fg='red',font=('algerian',14),bd=6)
        

        self.t1=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t2=Entry(self,show='*',bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t3=Entry(self,show='*',bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t4=Entry(self,show='*',bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        
        self.b1=Button(self,text='Change',bg='light blue',fg='red',font=('Arial',14),bd=6,justify="center",command=self.change)
        
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.rowconfigure(index=4,pad=10)
        
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)        

        self.l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)

        self.l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)

        self.l3.grid(row=2,column=0)
        self.t3.grid(row=2,column=1)

        self.l4.grid(row=3,column=0)
        self.t4.grid(row=3,column=1)

        
        self.b1.grid(columnspan=2)
        self.pack()
    def change(self):
        con=connect(db='students',user='root',password='root',host='localhost')
        cur=con.cursor()
        uid=self.t1.get()
        pwd=self.t2.get()
        npwd=self.t3.get()
        cpwd=self.t4.get()
        if(npwd!=cpwd):
            msg.showerror('',"New Password and Confirm Password Must be Same")
            self.t3.delete(0,'end')
            self.t4.delete(0,'end')
            self.t3.focus()
        else:
            i=cur.execute("update login set password='%s' where userid='%s' and password='%s'"%(npwd,uid,pwd))
            if(i==1):
                con.commit()
                msg.showinfo('','Password Changed')
                self.t1.delete(0,'end')
                self.t2.delete(0,'end')
                self.t3.delete(0,'end')
                self.t4.delete(0,'end')
            else:
                msg.showerror('','Some Error Occur')
       