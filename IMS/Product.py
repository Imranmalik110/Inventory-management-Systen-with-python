from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class productclass:
    def __init__(self,root):
        self.root=root
        self.root.title("Product  managment system")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg='white')
        self.root.focus_force()
    #--------All variable==========#

        self.var_cat=StringVar()
        self.var_suplier=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_pid=StringVar()
    #=========Prodcut Frame--------#
        Product_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Product_frame.place(x=10,y=10,width=450,height=480)
    #=====Frame Title---------------#
        title=Label(Product_frame,text="Manage Product Details",font=('Guddy old sytle',18,'bold'),bg='#0f4d7d',fg='white').pack(side=TOP,fill=X)
        
        lbl_category=Label(Product_frame,text="Category",font=('Guddy old sytle',18),bg='white').place(x=30,y=60)
        lbl_supplier=Label(Product_frame,text="Supplier",font=('Guddy old sytle',18),bg='white').place(x=30,y=110)
        lbl_productname=Label(Product_frame,text="Name",font=('Guddy old sytle',18),bg='white').place(x=30,y=160)
        lbl_price=Label(Product_frame,text="Price",font=('Guddy old sytle',18),bg='white').place(x=30,y=210)
        lbl_qty=Label(Product_frame,text="Quantity",font=('Guddy old sytle',18),bg='white').place(x=30,y=260)
        lbl_status=Label(Product_frame,text="Status",font=('Guddy old sytle',18),bg='white').place(x=30,y=310)
    #------------Entry Widget-----------------------#
        cmb_cat=ttk.Combobox(Product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=('Guddy old style',15))
        cmb_cat.place(x=150,y=60,width=180)
        cmb_cat.current(0)
        
        cmb_sup=ttk.Combobox(Product_frame,textvariable=self.var_suplier,values=self.sup_list,state='readonly',justify=CENTER,font=('Guddy old style',15))
        cmb_sup.place(x=150,y=110,width=180)
        cmb_sup.current(0)
        
        txt_name=Entry(Product_frame,font=('Guddy old style',15),textvariable=self.var_name,bg='lightyellow').place(x=150,y=160,width=180)
        txt_price=Entry(Product_frame,font=('Guddy old style',15),textvariable=self.var_price,bg='lightyellow').place(x=150,y=210,width=180)
        txt_qty=Entry(Product_frame,font=('Guddy old style',15),textvariable=self.var_quantity,bg='lightyellow').place(x=150,y=260,width=180)
        
        cmb_staus=ttk.Combobox(Product_frame,textvariable=self.var_status,values=("activate"),state='readonly',justify=CENTER,font=('Guddy old style',15))
        cmb_staus.place(x=150,y=310,width=180)
        cmb_staus.current(0)
    #----------Button All---------------------#
        btn_add=Button(Product_frame,text='Save',font=('Guddy old style',15),bg='#2196f3',activebackground='#2196f3',fg='white',cursor='hand2',command=self.Add).place(x=10,y=400,width=100,height=40)
        btn_update=Button(Product_frame,text='Update',font=('Guddy old style',15),bg='#4caf50',activebackground='#4caf50',fg='white',cursor='hand2',command=self.Update).place(x=120,y=400,width=100,height=40)
        btn_delete=Button(Product_frame,text='Delete',font=('Guddy old style',15),bg='#f44336',activebackground='#f44336',fg='white',cursor='hand2',command=self.Delete).place(x=230,y=400,width=100,height=40)
        btn_clear=Button(Product_frame,text='Clear',command=self.Clear,font=('Guddy old style',15),bg='#607d8b',activebackground='#607d8b',fg='white',cursor='hand2').place(x=340,y=400,width=100,height=40)
    #-------SearchFrame----------------------------#
        SearchFrame=LabelFrame(self.root,text="search Product",font=('guddy old style',14,'bold'),bd=2,relief=GROOVE,bg='white')
        SearchFrame.place(x=480,y=10,width=600,height=80)
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("select","Category","Supplier","name"),state='readonly',justify=CENTER,font=('Guddy old style',15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
         
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=('Guddy old style',15),bg='lightyellow').place(x=200,y=10)
        btn_search=Button(SearchFrame,text='Search',font=('Guddy old style',15),bg='#4caf50',activebackground='#4caf50',fg='white',cursor='hand2',command=self.search).place(x=430,y=8,width=150,height=30)
        #---------Employee Details tree view----------------------------#
        P_frame=Frame(self.root,bd=3,relief=RIDGE,bg='white')
        P_frame.place(x=480,y=100,width=600,height=390)
        
        scrolly=Scrollbar(P_frame,orient=VERTICAL)
        scrollx=Scrollbar(P_frame,orient=HORIZONTAL)
        
        self.ProductTable=ttk.Treeview(P_frame,columns=("pid","Category","Supplier","name","price","qty","status"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("pid",text="product Id")
        self.ProductTable.heading("Category",text="Category Name")
        self.ProductTable.heading("Supplier",text="Supplier Name")
        self.ProductTable.heading("name",text=" Prodcut name")
        self.ProductTable.heading("price",text="Price ")
        self.ProductTable.heading("qty",text="Quantity")
        self.ProductTable.heading("status",text="Status")
       
        self.ProductTable['show']="headings"
        
        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("Category",width=120)
        self.ProductTable.column("Supplier",width=160)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=150)
        self.ProductTable.column("qty",width=120)
        self.ProductTable.column("status",width=120)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
    #=================function---------------------------------#
    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            self.cat_list.append("Empty")
            cur.execute("select name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("select")
                for i in cat:
                    self.cat_list.append(i[0])
        
            self.sup_list.append("select")
            cur.execute("select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("select")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
    def Add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="select" or self.var_suplier.get()=="select" or self.var_name.get()=="":
               messagebox.showerror("Error","All filed required",parent=self.root)
            else:
                cur.execute("select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                
                if row!=None:
                        messagebox.showerror("ERROR","This product already present,try differnt",parent=self.root)
                else:
                     cur.execute("insert into product(Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                             self.var_cat.get(),
                             self.var_suplier.get(),
                             self.var_name.get(),
                             self.var_price.get(),
                             self.var_quantity.get(),
                             self.var_status.get(),
                     ))
                     con.commit()
                     messagebox.showinfo("Success","Product Added Successfully",parent=self.root)
                     self.show()
                     self.Clear()
        except Exception as es:
               messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
    def show(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from product")
                rows=cur.fetchall()
                self.ProductTable.delete(*self.ProductTable.get_children())
                for row in rows:
                    self.ProductTable.insert('',END,values=row)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
    def get_data(self,ev):
            f=self.ProductTable.focus()
            content=self.ProductTable.item(f)
            row=content['values']
            self.var_pid.set(row[0])
            self.var_cat.set(row[1])
            self.var_suplier.set(row[2])
            self.var_name.set(row[3])
            self.var_price.set(row[4])
            self.var_quantity.set(row[5])
            self.var_status.set(row[6])
            
    def Update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
               messagebox.showerror("Error","please select product from list",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
               # print(row)
                if row==None:
                        messagebox.showerror("ERROR","Invalid product",parent=self.root)
                else:
                     cur.execute(" update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=? ",(
                            self.var_cat.get(),
                            self.var_suplier.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_quantity.get(),
                            self.var_status.get(),
                            self.var_pid.get()
                     ))
                     con.commit()
                     messagebox.showinfo("Success","product Updated Successfully",parent=self.root)
                     self.show()
                     self.Clear()
        except Exception as es:
               messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
    def Delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try: 
             if self.var_pid.get()=="":
               messagebox.showerror("Error","select Product From list",parent=self.root)
             else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                        messagebox.showerror("ERROR","Invalid Product Id",parent=self.root)
                else:
                     op=messagebox.askyesno("Confirm","Do you really want to delte the record?",parent=self.root)
                     if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Product Delete Successfully",parent=self.root)
                        self.Clear()
        except Exception as es:
             messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
    def Clear(self):
        
        self.var_cat.set("select"),
        self.var_suplier.set("select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_quantity.set(""),
        self.var_status.set("inactive"),
        self.var_pid.set(""),
        self.var_searchtxt.set("")
        self.var_searchby.set("select")
        self.show()
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="select":
                messagebox.showerror("Warning","Select Search by option",parent=self.root)
            elif self.var_searchby.get()=="":
                messagebox.showerror("Error","Search field should not be empty",parent=self.root)
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                        
                else:
                    messagebox.showerror("ERROR","No Record found!!!",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=productclass(root)
    root.mainloop()