from tkinter import*
from PIL import Image,ImageTk
from employee import employeeclass
from supplier import SupplierClass
from Category import catergoryClass
from Product import productclass
from sales import salesclass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventroy managment system")
        self.root.geometry("1350x700")
        self.root.config(bg='white')
    #---Title of Main Window------------------------------------#
        self.logo=PhotoImage(file="Images/cart.png")
        #-------------------------title---Label----------------#
        title=Label(self.root,text="Inventory Management System",compound=LEFT,padx=20,font=('Guddy old sytle',35,'bold'),image=self.logo,bg='#010c48',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
    #----ButtonLogout----------------------------------------#
        btn_logout=Button(self.root,text='logout',font=('times new roman',20,'bold'),activebackground='yellow',bg='yellow',cursor='hand2').place(x=1100,y=10,height=40,width=150)
    #---Lable  Clock----------------------------------------#
        self.lbl_clock=Label(self.root,text=" Welcome to Inventory Management System\t\tDate: DD-MM-YYYY\t\t Time: HH:MM:SS",font=('Guddy old sytle',15),bg='#4d636d',fg='white')
        self.lbl_clock.place(x=0,y=60,relwidth=1,height=30)
    #-----Left Menu--------------------------------------------#
        self.left_logo=Image.open("Images/inventory.png")
        self.left_logo=self.left_logo.resize((180,180),Image.ANTIALIAS)
        self.left_logo=ImageTk.PhotoImage(self.left_logo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        LeftMenu.place(x=0,y=90,width=200,relheight=1)
        
        lbl_left=Label(LeftMenu,image=self.left_logo)
        lbl_left.pack(side=TOP,fil=X)
        
        lbl_menu=Label(LeftMenu,text="Menu",font=('times new roman',20),bg='#009688').pack(side=TOP,fill=X)
        self.side=PhotoImage(file="Images/forward_Icon.png")
        btn_employee=Button(LeftMenu,text="Employee",image=self.side,compound=LEFT,padx=5,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2',command=self.employee).pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Supplier",image=self.side,compound=LEFT,padx=5,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2',command=self.supplier).pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Category",command=self.category,image=self.side,compound=LEFT,padx=5,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Products",command=self.product,image=self.side,compound=LEFT,padx=5,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Sale",command=self.sales,image=self.side,compound=LEFT,padx=5,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Exit",image=self.side,compound=LEFT,padx=5,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
#---------Content Lable Show-------------------------------------------------------#
        self.lbl_employee=Label(self.root,text='Total Employee\n[0]',bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=('Guddy old style',20,'bold'))
        self.lbl_employee.place(x=320,y=120,width=300,height=150)
        
        self.lbl_supplier=Label(self.root,text='Total Supplier\n[0]',bd=5,relief=RIDGE,bg="#ff5222",fg="white",font=('Guddy old style',20,'bold'))
        self.lbl_supplier.place(x=650,y=120,width=300,height=150)
        
        self.lbl_category=Label(self.root,text='Total Category\n[0]',bd=5,relief=RIDGE,bg="#009688",fg="white",font=('Guddy old style',20,'bold'))
        self.lbl_category.place(x=1000,y=120,width=300,height=150)
        
        self.lbl_prodcut=Label(self.root,text='Total Products\n[0]',bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=('Guddy old style',20,'bold'))
        self.lbl_prodcut.place(x=320,y=300,width=300,height=150)
        
        self.lbl_sales=Label(self.root,text='Total Sales\n[0]',bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=('Guddy old style',20,'bold'))
        self.lbl_sales.place(x=650,y=300,width=300,height=150)
        
#-------footer Logo--------------------------------------------------------------#
        lbl_footer=Label(self.root,text='IMS-Inventory management System\n Devloped by Imran malik\n Contacts for any techincial support : imranim4205102@gmail.com',font=('times new roman',12),bg='#4d636d',fg='white').pack(side=BOTTOM,fill=X)
#=======================function========================================#
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeclass(self.new_win)
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SupplierClass(self.new_win)
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=catergoryClass(self.new_win)
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productclass(self.new_win)
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesclass(self.new_win)
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()