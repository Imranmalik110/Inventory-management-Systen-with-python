from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class salesclass:
    def __init__(self,root):
        self.root=root
        self.root.title("sales  managment system")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg='white')
        self.root.focus_force()
    #-----All Varaibale--------------#
        self.bill_list=[]
        self.var_invoice=StringVar()
#--------Title of Frame--------------------#
        lbl_title=Label(self.root,text="View Customer Bills",font=('Guddy old sytle',30,'bold'),bg='#184a45',fg='white').pack(side=TOP,fill=X,padx=10,pady=10)
    #-------Widget------------#
        lbl_invoice=Label(self.root,text="Invoice No",font=('times new roman',15),bg='white').place(x=50,y=100)    
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=('times new roman',15),bg='lightyellow').place(x=160,y=100,width=180,height=28)    
        
        btn_search=Button(self.root,text="Search",command=self.search,font=('times new roman',15),bg='#2196f3',fg='white',cursor='hand2').place(x=360,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="Clear",font=('times new roman',15),bg='lightgrey',cursor='hand2').place(x=490,y=100,width=120,height=28)
#--------Sales Area------------------------------------#
        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=200,height=330)
        scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_frame,font=('Guddy old style',15),bg='white',yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)
#--------------Bill Area------------#
        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=280,y=140,width=400,height=330)
        
        lbl2_title=Label(bill_frame,text="Customer Bill Area",font=('Guddy old style',20),bg='orange').pack(side=TOP,fill=X)
        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,font=('Guddy old style',15),bg='lightyellow',yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
#--------Image ICon---------------------#
        self.im1=Image.open("Images/bill_photo.jpg")
        self.im1=self.im1.resize((400,350),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)
        self.lbl_im1=Label(self.root,image=self.im1,bd=0)
        self.lbl_im1.place(x=700,y=140)
        self.show()
#==================================Function====================#
    def show(self):
        self.bill_list[:]
        self.sales_list.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
    def get_data(self,ev):
        index=self.sales_list.curselection()
        file_name=self.sales_list.get(index)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice No should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice No",parent=self.root)
    def clear(self):
        self.show()
                        
if __name__=="__main__":
    root=Tk()
    obj=salesclass(root)
    root.mainloop()