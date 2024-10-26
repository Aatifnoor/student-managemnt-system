from tkinter import *
from tkinter import messagebox as msg
from pymysql import *

class Admission(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.l1=Label(self,text="Student Id",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l2=Label(self,text="Student Name",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l3=Label(self,text="Father's Name",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l4=Label(self,text="Address",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l5=Label(self,text="City",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l6=Label(self,text="Pin Code",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l7=Label(self,text="Mobile No",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l8=Label(self,text="Class",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l9=Label(self,text="Year",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l10=Label(self,text="Total Fee",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l11=Label(self,text="User Name",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l12=Label(self,text="Password",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l13=Label(self,text="User Type",bg='light blue',fg='red',font=('algerian',14),bd=6)

        self.t1=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t2=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t3=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t4=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t5=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t6=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t7=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t8=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t9=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t10=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t11=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t12=Entry(self,show='*',bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t13=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")

        self.b1=Button(self,text='Save',bg='light blue',fg='red',font=('Arial',14),bd=6,justify="center",command=self.save)
        
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.rowconfigure(index=4,pad=10)
        self.rowconfigure(index=5,pad=10)
        self.rowconfigure(index=6,pad=10)
        self.rowconfigure(index=7,pad=10)
        self.rowconfigure(index=8,pad=10)
        self.rowconfigure(index=9,pad=10)
        self.rowconfigure(index=10,pad=10)
        self.rowconfigure(index=11,pad=10)
        self.rowconfigure(index=12,pad=10)
        self.rowconfigure(index=13,pad=10) 

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

        self.l5.grid(row=4,column=0)
        self.t5.grid(row=4,column=1)
        self.l6.grid(row=5,column=0)
        self.t6.grid(row=5,column=1)
        self.l7.grid(row=6,column=0)
        self.t7.grid(row=6,column=1)
        self.l8.grid(row=7,column=0)
        self.t8.grid(row=7,column=1)
        self.l9.grid(row=8,column=0)
        self.t9.grid(row=8,column=1)
        self.l10.grid(row=9,column=0)
        self.t10.grid(row=9,column=1)
        self.l11.grid(row=10,column=0)
        self.t11.grid(row=10,column=1)
        self.l12.grid(row=11,column=0)
        self.t12.grid(row=11,column=1)
        self.l13.grid(row=12,column=0)
        self.t13.grid(row=12,column=1)

        self.b1.grid(columnspan=2)
        self.pack()
    def save(self):
        con=connect(db='students',user='root',password='root',host='localhost')
        cur=con.cursor()
        sid=int(self.t1.get())
        sname=self.t2.get()
        fname=self.t3.get()
        address=self.t4.get()
        city=self.t5.get()
        pin=int(self.t6.get())
        phone=self.t7.get()
        cname=self.t8.get()
        year=self.t9.get()
        fee=int(self.t10.get())
        uname=self.t11.get()
        passwd=self.t12.get()
        utype=self.t13.get()
        i=cur.execute("insert into login values('%s','%s','%s')"%(uname,passwd,utype))
        if(i==1):
            j=cur.execute("insert into studentmaster values(%d,'%s','%s','%s','%s',%d,'%s','%s','%s',%d)"%(sid,sname,fname,address,city,pin,phone,cname,year,fee))
            if(j==1):
                msg.showinfo('Confirmation','Thanks for Registration')
                self.t1.delete(0,'end')
                self.t2.delete(0,'end')
                self.t3.delete(0,'end')
                self.t4.delete(0,'end')
                self.t5.delete(0,'end')
                self.t6.delete(0,'end')
                self.t7.delete(0,'end')
                self.t8.delete(0,'end')
                self.t9.delete(0,'end')
                self.t10.delete(0,'end')
                self.t11.delete(0,'end')
                self.t12.delete(0,'end')
                self.t13.delete(0,'end')
                con.commit()
                con.close()




