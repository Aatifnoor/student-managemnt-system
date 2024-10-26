from tkinter import *
from tkinter import messagebox as msg
from pymysql import *

class StudentMarks(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.l1=Label(self,text="Student Id",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l2=Label(self,text="Year for Exam",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l3=Label(self,text="Subject 1",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l4=Label(self,text="Subject 2",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l5=Label(self,text="Subject 3",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l6=Label(self,text="Subject 4",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l7=Label(self,text="Subject 5",bg='light blue',fg='red',font=('algerian',14),bd=6)
        self.l8=Label(self,text="Subject 6",bg='light blue',fg='red',font=('algerian',14),bd=6)
        
        self.t1=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t2=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t3=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t4=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t5=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t6=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t7=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        self.t8=Entry(self,bg='light blue',fg='red',font=('Arial',14),bd=6,insertwidth=4,justify="center")
        
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
        
        self.b1.grid(columnspan=2)
        self.pack()
    def save(self):
        con=connect(db='students',user='root',password='root',host='localhost')
        cur=con.cursor()
        sid=int(self.t1.get())
        year=self.t2.get()
        sub1=int(self.t3.get())
        sub2=int(self.t4.get())
        sub3=int(self.t5.get())
        sub4=int(self.t6.get())
        sub5=int(self.t7.get())
        sub6=int(self.t8.get())
        i=cur.execute("insert into marks values(%d,'%s',%d,%d,%d,%d,%d,%d)"%(sid,year,sub1,sub2,sub3,sub4,sub5,sub6))
        if(i==1):
            msg.showinfo('Confirmation','Thanks for Exam')
            self.t1.delete(0,'end')
            self.t2.delete(0,'end')
            self.t3.delete(0,'end')
            self.t4.delete(0,'end')
            self.t5.delete(0,'end')
            self.t6.delete(0,'end')
            self.t7.delete(0,'end')
            self.t8.delete(0,'end')
            con.commit()
            con.close()




