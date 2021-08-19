from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class catergoryClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Managment System")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg='white')
        self.root.focus_force()
#--------All variabele Delecaration------------------#
        self.var_cat_Id=StringVar()
        self.var_cat_name=StringVar()
#-------Title of Frame--------------------------------------------------
        title=Label(self.root,text="Manage Category Details",font=('Guddy old sytle',30,'bold'),bg='#184a45',fg='white').pack(side=TOP,fill=X,padx=10,pady=10)
#----------Widgets-------------------------------------------------#
        lbl_categoryname=Label(self.root,text="Enter Category Name",font=('Guddy old style',30),bg='white').place(x=50,y=100)
        txt_categoryname=Entry(self.root,textvariable=self.var_cat_name,font=('Guddy old style',18),bg='lightyellow').place(x=50,y=170,width=300)
#---------Button --------------------------------------------------#
        btn_add=Button(self.root,text="ADD",font=('Guddy old style',15),fg='white',bg='#4caf50',activebackground='#4caf50',cursor='hand2',command=self.Add_category).place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",font=('Guddy old style',15),fg='white',bg='red',activebackground='red',cursor='hand2',command=self.delete_category).place(x=520,y=170,width=150,height=30)
#------Category Details-------------------------------------------#  
        self.c_frame=Frame(self.root,bd=3,relief=RIDGE)
        self.c_frame.place(x=680,y=100,width=400,height=100)
        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        self.catergoryTable=ttk.Treeview(self.c_frame,columns=("cid","name"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.catergoryTable.xview)
        scrolly.config(command=self.catergoryTable.yview)
        self.catergoryTable.heading("cid",text="C_ID")
        self.catergoryTable.heading("name",text="Category Name")
        self.catergoryTable["show"]='headings'
        self.catergoryTable.column("cid",width=100)
        self.catergoryTable.column("name",width=100)
        self.catergoryTable.pack(fill=BOTH,expand=1)
        self.catergoryTable.bind("<ButtonRelease-1>",self.get_data)
        self.show_category()
#----------Images--------------------------------------#
        self.im1=Image.open("Images/Invent.jpg")
        self.im1=self.im1.resize((500,260),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)
        self.lbl_im1=Label(self.root,image=self.im1)
        self.lbl_im1.place(x=50,y=220)
        
        self.im2=Image.open("Images/Category.jpg")
        self.im2=self.im2.resize((500,260),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)
        self.lbl_im2=Label(self.root,image=self.im2)
        self.lbl_im2.place(x=580,y=220)
#-----------Function --------------------------------#
    def clear(self):
        self.var_cat_name.set("")
    def Add_category(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        if self.var_cat_name.get()=="":
            messagebox.showerror("Error","Category Name must be required",parent=self.root)
        else:
            cur.execute("select * from category where name=?",(self.var_cat_name.get(),))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","Category Name Already Exits",parent=self.root)
            else:
                cur.execute("insert into category(name) values(?)",(self.var_cat_name.get(),))
                con.commit()
                messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
                self.show_category()
                self.clear()
    def show_category(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.catergoryTable.delete(*self.catergoryTable.get_children())
            for row in rows:
                self.catergoryTable.insert('',END,values=row)
        except Exception as es:
             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def get_data(self,ev):
        self.var_cat_name
        r=self.catergoryTable.focus()
        content=self.catergoryTable.item(r)
        row=content["values"]
    #    print(row)
        self.var_cat_name.set(row[1])
    def delete_category(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_name.get()=="":
                messagebox.showerror("Wraning","Category should be required",parent=self.root)
            else:
                cur.execute("select * from category where name=?",(self.var_cat_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("warning","plese select Category from list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete the Category",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM  category where name=?",(self.var_cat_name.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Category Deleted Successfully",parent=self.root)
                        self.clear()
                        self.show_category()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
if __name__=="__main__":
    root=Tk()
    obj=catergoryClass(root)
    root.mainloop()