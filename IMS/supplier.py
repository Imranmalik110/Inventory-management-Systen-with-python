from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class SupplierClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Managment System")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg='white')
        self.root.focus_force()
        #----------All the Vairble----------------#
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
#----------Title-----------------------------------#
        title=Label(self.root,text="Manage Supplier Details",font=('Guddy old sytle',20,'bold'),bg='#033054',fg='white').place(x=0,y=0,relwidth=1,height=50)
#---------Widgts---------------------------#
        lbl_invoice=Label(self.root,text="Invoice No",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=100)
        lbl_contact=Label(self.root,text="Contact",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=140)
        lbl_description=Label(self.root,text="Description",font=('Guddy old style',15,'bold'),bg='white').place(x=10,y=180)
        #-------Entry field--------------------------------------------#
        self.txt_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_invoice.place(x=150,y=60,width=200)
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_name.place(x=150,y=100,width=200)
        self.txt_contact=Entry(self.root,textvariable=self.var_contact,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_contact.place(x=150,y=140,width=200)
        self.txt_description=Text(self.root,font=('Guddy old style',15,'bold'),bg='lightyellow')
        self.txt_description.place(x=150,y=180,width=350,height=100)
    #-------------Button------------------#
        self.btn_add=Button(self.root,text="Save",font=('Guddy old style',15,'bold'),bg='#2196f3',activebackground='#2196f3',fg='white',cursor='hand2',command=self.Add_course)
        self.btn_add.place(x=30,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=('Guddy old style',15,'bold'),bg='#4caf50',activebackground='#4caf50',fg='white',cursor='hand2',command=self.updte_data)
        self.btn_update.place(x=150,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=('Guddy old style',15,'bold'),bg='#f44336',activebackground='#f44336',fg='white',cursor='hand2',command=self.Delete_data)
        self.btn_delete.place(x=270,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=('Guddy old style',15,'bold'),bg='grey',activebackground='grey',fg='white',cursor='hand2',command=self.clear)
        self.btn_clear.place(x=390,y=400,width=110,height=40)
    #-----------Search Panel----------------------------------------#
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Invoice No",font=('Guddy old style',15,'bold'),bg='white').place(x=620,y=60)
        txt_search_courseName=Entry(self.root,font=('Guddy old style',15,'bold'),textvariable=self.var_search,bg='lightyellow').place(x=730,y=60,width=180)
        btn_search=Button(self.root,text="Search",font=('Guddy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.search)
        btn_search.place(x=920,y=60,width=110,height=32)
        #----------------Content----------------#
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=620,y=120,width=470,height=340)
        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        self.courseTable=ttk.Treeview(self.c_frame,columns=("invoice","name","contact","desc"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)
        self.courseTable.heading("invoice",text="Invoice No")
        self.courseTable.heading("name",text="Name")
        self.courseTable.heading("contact",text="Contact No")
        self.courseTable.heading("desc",text="Description")
        self.courseTable["show"]='headings'
        self.courseTable.column("invoice",width=100)
        self.courseTable.column("name",width=100)
        self.courseTable.column("contact",width=100)
        self.courseTable.column("desc",width=200)
        self.courseTable.pack(fill=BOTH,expand=1)
        self.courseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show_Details()
        #-----------function-------#
    def Delete_data(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Wraning","Invoice No should be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",self.var_sup_invoice.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("warning","plese select Invoice No from list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete the record",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM  supplier where name=?",self.var_sup_invoice.get())
                        con.commit()
                        messagebox.showinfo("Success","Record Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def clear(self):
        self.show_Details()
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_description.delete('1.0',END)
        #self.txt_courseName.config(state=NORMAL)
    def updte_data(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Wraning","Invoice No Not not be Empty")
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("warning","select Supplier from list",parent=self.root)
                else:
                    cur.execute("update supplier set  name=?,contact=?,desc=? where invoice=?",(
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_description.get("1.0",END),
                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier  update Successfully",parent=self.root)
                    self.Clear_field()
                    self.show_Details()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
        
    def get_data(self,ev):
        self.txt_invoice.config(state='readonly')
        self.txt_name
        r=self.courseTable.focus()
        content=self.courseTable.item(r)
        row=content["values"]
    #    print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[3])
    def Clear_field(self):
        self.txt_invoice.delete(0,END)
        self.txt_name.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_description.delete('1.0',END)
    def Add_course(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Wraning","Invoice No Not not be Empty")
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("warning","Supplier Already Exists",parent=self.root)
                else:
                    cur.execute("insert into supplier(invoice,name,contact,desc) values(?,?,?,?)",(
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.Clear_field()
                    self.show_Details()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def show_Details(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute(f"select * from supplier where invoice LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)   
if __name__=="__main__":
    root=Tk()
    obj=SupplierClass(root)
    root.mainloop()