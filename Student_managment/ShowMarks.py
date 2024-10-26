from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from datetime import *
class MarkShow(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.dt=datetime.now()
        self.ndate=str(self.dt.year)+"-"+str(self.dt.month)+"-"+str(self.dt.day)
        
        self.l1=Label(self,text="Student Id",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.t1=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.l2=Label(self,text="For Year",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.t2=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.l3=Label(self,text="Total Marks",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.t3=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.l4=Label(self,text="Percentae %",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.t4=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        
        
        
        self.b1=Button(self,text='Show',bg='light blue',fg='red',font=('Arial',14),bd=6,justify="center",command=self.total)
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
    def total(self):
        con=connect(db='students',user='root',password='root',host='localhost')
        cur=con.cursor()
        sid=int(self.t1.get())
        year=self.t2.get()
        cur.execute("select * from marks where sid=%d and year='%s'"%(sid,year))
        result=cur.fetchall()
        if(len(result)==1):
            total=result[0][2]+result[0][3]+result[0][4]+result[0][5]+result[0][6]+result[0][7]
            per=total/6
            self.t3.insert(0,total)
            self.t4.insert(0,per)
    