from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from datetime import *
class StudentFee(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.dt=datetime.now()
        self.ndate=str(self.dt.year)+"-"+str(self.dt.month)+"-"+str(self.dt.day)
        
        self.l1=Label(self,text="Student Id",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l2=Label(self,text="Student Name",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l3=Label(self,text="Total Fee",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l4=Label(self,text="Fee Paid",bg='light blue',fg='red',font=('algerian',14),bd=6)
        
        self.t1=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t2=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t3=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t4=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        
        self.b1=Button(self,text='Search',bg='light blue',fg='red',font=('Arial',14),bd=6,justify="center",command=self.search)
        self.b2=Button(self,text='Fee Paid',bg='light blue',fg='red',font=('Arial',14),bd=6,justify="center",command=self.paid)
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

        self.b1.grid(row=4,column=0)
        self.b2.grid(row=4,column=1)
        self.pack()
    def search(self):
        con=connect(db='students',user='root',password='root',host='localhost')
        cur=con.cursor()
        sid=int(self.t1.get())
        cur.execute("select sname,total_fee from studentmaster where sid=%d"%(sid))
        record=cur.fetchall()
        if(len(record)==1):
            self.t2.insert(0,record[0][0])
            self.t3.insert(0,record[0][1])
            con.close()
    def paid(self):
        con=connect(db='students',user='root',password='root',host='localhost')
        cur=con.cursor()
        sid=int(self.t1.get())
        fee=int(self.t4.get())
        tfee=int(self.t3.get())
        if(tfee<fee):
            msg.showerror('',"Total Fee are more than fee paid")
        else:
            i=cur.execute("update studentmaster set total_fee=total_fee-%d where sid=%d"%(fee,sid))
            if(i==1):
                j=cur.execute("insert into fee values(%d,'%s',%d)"%(sid,self.ndate,fee))
                if(j==1):
                    con.commit()
                    msg.showinfo('Confirm','Fee Paid Thanks')
        