from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing software")

# -------------------------------------------------variables--------------------------------------------------------------------

        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.c_bill_no=StringVar()
        z=random.randint(1000,9999)
        self.c_bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.price=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
# ------------------------------------------product categories--------------------------------------------------------------        

        self.Category=["Select","Cloths","Cosmetics","Electronics items"]

        #subcategoryclothing
        self.subclothing=["Shirt","Pant","Shoe"]
        self.pant=["polo","tommy","apollo"]
        self.polo_price=1200
        self.tommy_price=800
        self.apollo_price=2000

        self.shirt=["Dravis","Raymond","wisley"]
        self.dravis_price=1100
        self.raymond_price=2500
        self.wisley_price=1500

        self.shoes=["Nike","Puma","Adidas"]
        self.nike_price=2000
        self.puma_price=1500
        self.adidas_price=1000
        
        #subcategorycosmetics
        self.subcosmetics=["Facewash","Shampoo","Oil"]
        self.facewash=["Himalayas","Nivia","Geornia"]
        self.himalaya_price=205
        self.nivia_price=408
        self.geornia_price=364

        self.shampoo=["Herbal","Letsliv","Dove"]
        self.herbal_price=345
        self.letliv_price=502
        self.dove_price=258

        self.oil=["Birdal","Asvini","Amazon"]
        self.birdal_price=307
        self.asvini_price=231
        self.amazon_price=406

        #subcategory_electronics
        self.subelectronics=["Mobile","TV","Laptop"]
        self.mobile=["Poco","Iphone","Samsung"]
        self.poco_price=20000
        self.iphone_price=80000
        self.samsung_price=40000

        self.tv=["Parasonic","Onida","LDD"]
        self.parasonic_price=30000
        self.onida_price=25000
        self.ldd_price=22000

        self.laptop=["HP","Dell","Lenovo"]
        self.hp_price=38000
        self.dell_price=72000
        self.lenovo_price=47000




        lbl_title=Label(self.root,text="BILLING SOFTWARE",font=("times",50,"bold"),bg="blue",fg="lightblue",bd=8)
        lbl_title.pack(fill=X)

#-----------------------------------------------time frame----------------------------------------------------------------
        def time():
                string = strftime('%H:%M:%S %p')
                lbl_time.config(text = string)
                lbl_time.after(1000, time)

        lbl_time=Label(lbl_title,font=("times",15,"bold"),bg="white",fg="blue",)
        lbl_time.place(x=0,y=2,width=130,height=40)
        time()
#------------------------------------------------main frame----------------------------------------------------------------

        main_frame=Frame(self.root,bd=8,relief=GROOVE,bg="lightblue",width=1520,height=620)
        main_frame.pack()

# ------------------------------------------------------customer frame----------------------------------------------------
        customer_frame=LabelFrame(main_frame,text="Customer Details",font=("times",15,"bold"),bg="skyblue",fg="black",bd=6)
        customer_frame.place(x=5,y=5,width=320,height=150)

        self.lbl_mob=Label(customer_frame,text="Mobile No.",font=("times",12,"bold"),bg="skyblue",fg="blue")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
        
        self.entry_mob=ttk.Entry(customer_frame,font=("times",12,"bold"),width=24,textvariable=self.c_phone)
        self.entry_mob.grid(row=0,column=1)

        self.lbl_name=Label(customer_frame,text="Name",font=("times",12,"bold"),bg="skyblue",fg="blue")
        self.lbl_name.grid(row=1,column=0,stick=W,padx=5,pady=3)
        
        self.entry_name=ttk.Entry(customer_frame,font=("times",12,"bold"),width=24,textvariable=self.c_name)
        self.entry_name.grid(row=1,column=1)

        self.lbl_mail=Label(customer_frame,text="Email",font=("times",12,"bold"),bg="skyblue",fg="blue")
        self.lbl_mail.grid(row=2,column=0,stick=W,padx=5,pady=3)
        
        self.entry_mail=ttk.Entry(customer_frame,font=("times",12,"bold"),width=24,textvariable=self.c_email)
        self.entry_mail.grid(row=2,column=1)


#   --------------------------------------------------product frame------------------------------------------------------
        product_frame=LabelFrame(main_frame,text="Product Details",font=("times",15,"bold"),bg="skyblue",fg="black",bd=6)
        product_frame.place(x=330,y=5,width=560,height=150)

        self.lbl_product_category=Label(product_frame,text="Category",font=("times",12,"bold"),bg="skyblue",fg="blue")
        self.lbl_product_category.grid(row=0,column=0,stick=W,padx=5,pady=3)
        
        self.combo_product_category=ttk.Combobox(product_frame,value=self.Category,font=("times",12,"bold"),width=20,state="readonly")
        self.combo_product_category.current(0)
        self.combo_product_category.grid(row=0,column=1)
        self.combo_product_category.bind("<<ComboboxSelected>>",self.categories)

        self.lbl_product_type=Label(product_frame,text="Product Type",font=("times",12,"bold"),bg="skyblue",fg="blue")
        self.lbl_product_type.grid(row=1,column=0,stick=W,padx=5,pady=2)
        
        self.combo_product_type=ttk.Combobox(product_frame,font=("times",12,"bold"),width=20,state="readonly")
        self.combo_product_type.grid(row=1,column=1)
        self.combo_product_type.bind("<<ComboboxSelected>>",self.product_type)

        self.lbl_brand=Label(product_frame,text="Brand",font=("times",12,"bold"),bg="skyblue",fg="blue")
        self.lbl_brand.grid(row=2,column=0,stick=W,padx=5,pady=2)
        
        self.combo_brand=ttk.Combobox(product_frame,font=("times",12,"bold"),width=20,state="readonly",textvariable=self.product)
        self.combo_brand.grid(row=2,column=1)
        self.combo_brand.bind("<<ComboboxSelected>>",self.brand)

        self.lbl_quantity=Label(product_frame,text="Quantity",font=("times",12,"bold"),bg="skyblue",fg="blue")
        self.lbl_quantity.grid(row=0,column=3,stick=W,padx=5,pady=2)
        
        self.entry_quantity=ttk.Entry(product_frame,font=("times",12,"bold"),width=22,textvariable=self.qty)
        self.entry_quantity.grid(row=0,column=4)

        self.lbl_rate=Label(product_frame,text="Rate",font=("times",12,"bold"),bg="skyblue",fg="blue")
        self.lbl_rate.grid(row=1,column=3,stick=W,padx=5,pady=2)
        
        self.combo_rate=ttk.Combobox(product_frame,font=("times",12,"bold"),width=20,state="readonly",textvariable=self.price)
        self.combo_rate.grid(row=1,column=4)

#  ------------------------------------------------------bill frame------------------------------------------------------------       
        
        bill_frame=LabelFrame(main_frame,text="BILL",font=("times",15,"bold"),bg="white",fg="black",bd=6)
        bill_frame.place(x=900,y=5,width=450,height=500)

        scroll_y=Scrollbar(bill_frame,orient=VERTICAL)
        self.text_area=Text(bill_frame,yscrollcommand=scroll_y.set,bg="white",fg="black",font=("times",10,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.text_area.yview)
        self.text_area.pack(fill=BOTH,expand=1)

# -------------------------------------------------------bill counter frame----------------------------------------------------
        
        counter_frame=LabelFrame(main_frame,text="Bill Counter",font=("times",15,"bold"),bg="black",fg="white",bd=8)
        counter_frame.place(x=5,y=200,width=880,height=305)

        self.lbl_sub_total=Label(counter_frame,text="Sub Total",font=("times",12,"bold"),bg="black",fg="grey")
        self.lbl_sub_total.grid(row=0,column=0,stick=W,padx=5,pady=2)
        
        self.entry_sub_total=ttk.Entry(counter_frame,font=("times",12,"bold"),width=22,textvariable=self.sub_total)
        self.entry_sub_total.grid(row=0,column=1)

        self.lbl_GST=Label(counter_frame,text="GST",font=("times",12,"bold"),bg="black",fg="grey")
        self.lbl_GST.grid(row=0,column=2,stick=W,padx=8,pady=2)
        
        self.entry_GST=ttk.Entry(counter_frame,font=("times",12,"bold"),width=22,textvariable=self.tax_input)
        self.entry_GST.grid(row=0,column=3)

        self.lbl_total=Label(counter_frame,text="Total Amount",font=("times",12,"bold"),bg="black",fg="grey")
        self.lbl_total.grid(row=0,column=4,stick=W,padx=8,pady=2)
        
        self.entry_total=ttk.Entry(counter_frame,font=("times",12,"bold"),width=22,textvariable=self.total)
        self.entry_total.grid(row=0,column=5)

# -------------------------------------------------------button frame-----------------------------------------------------------        
        
        button_frame=Frame(counter_frame,bg="black")
        button_frame.place(x=100,y=50)

        self.add_to_cart=Button(button_frame,text="Add To Cart",command=self.additems,font=("times",15,"bold"),bg="green",fg="lightgreen")
        self.add_to_cart.grid(row=0,column=0,padx=40,pady=20)

        self.generate_bill=Button(button_frame,text="Generate Bill",command=self.gen_bill,font=("times",15,"bold"),bg="green",fg="lightgreen")
        self.generate_bill.grid(row=0,column=1,padx=40,pady=20)

        self.save_button=Button(button_frame,text="Save Bill",command=self.save_bill,font=("times",15,"bold"),bg="green",fg="lightgreen")
        self.save_button.grid(row=0,column=2,padx=40,pady=20)

        self.print_bill=Button(button_frame,text="Print Bill",command=self.iprint,font=("times",15,"bold"),bg="green",fg="lightgreen")
        self.print_bill.grid(row=1,column=0,padx=40,pady=20)

        self.clear_button=Button(button_frame,text="Clear",command=self.clear,font=("times",15,"bold"),bg="red",fg="white")
        self.clear_button.grid(row=1,column=1,padx=40,pady=20)

        self.exit=Button(button_frame,text="Exit",command=self.root.destroy,font=("times",15,"bold"),bg="red",fg="white")
        self.exit.grid(row=1,column=2,padx=40,pady=20)
        self.welcome()

# -------------------------------------------------------search box--------------------------------------------------------

        search_frame=Frame(main_frame,bd=4,bg="black")
        search_frame.place(x=200,y=520)

        self.lblbill=Label(search_frame,text="Bill Number",font=("times",15,"bold"),padx=10,bd=2,bg="red",fg="black")
        self.lblbill.grid(row=0,column=0,padx=2)

        self.entry_bill=ttk.Entry(search_frame,font=("times",12,"bold"),width=24,textvariable=self.search_bill)
        self.entry_bill.grid(row=0,column=1,padx=2)

        self.search_button=Button(search_frame,text="Search",command=self.find_bill,font=("times",15,"bold"),bg="green",fg="white",width=10)
        self.search_button.grid(row=0,column=2,padx=2)

#------------------------------------------------------button functions--------------------------------------------------------------
        self.l=[]

    def additems(self):
        Tax=10
        self.n=self.price.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
                messagebox.showerror("Invalid","Please select the Product")
        else:
                self.text_area.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t\t{self.m}")
                self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
                self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.price.get()))*Tax)/100)))
                self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.price.get()))*Tax)/100)))))        
    
    def gen_bill(self):
        if self.product.get()=="":
                messagebox.showerror("Error","Please Add Products to Cart")
        else:
                text=self.text_area.get(10.0,(10.0+float(len(self.l))))
                self.welcome()
                self.text_area.insert(END,text)
                self.text_area.insert(END,"\n ***********************************************************")
                self.text_area.insert(END,f"\n Sub Amount   :\t\t\t{self.sub_total.get()}")
                self.text_area.insert(END,f"\n GST          :\t\t\t{self.tax_input.get()}")
                self.text_area.insert(END,f"\n Total Amount :\t\t\t{self.total.get()}")
                self.text_area.insert(END,"\n***********************************************************")

    def save_bill(self):
        op=messagebox.askyesno("Request","Save Bill")
        if op>0:
                self.bill_data=self.text_area.get(1.0,END)
                f1=open('bills/'+str(self.c_bill_no.get())+".txt",'w')
                f1.write(self.bill_data)
                op=messagebox.showinfo("Saved",f"Bill No: {self.c_bill_no.get()} Saved Successsfully")
                f1.close()

    def iprint(self):
        a=self.text_area.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(a)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
                if i.split('.')[0]==self.search_bill.get():
                        f1=open(f'bills/{i}','r')
                        self.text_area.delete(1.0,END)
                        for d in f1:
                                self.text_area.insert(END,d)
                        f1.close()
                        found="yes"
        if found=='no':
                messagebox.showerror("Error","Invalid Bill No")

    def clear(self):
        self.text_area.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.c_bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.price.set(0)
        self.qty.set(0)
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()
# -----------------------------------------------------bill receipt texts------------------------------------------------------------------------        
        
    def welcome(self):
        self.text_area.delete(1.0,END)
        self.text_area.insert(END,"\t\t\tFAZIL RETAIL STORE")
        self.text_area.insert(END,f"\n\n Bill N0 : {self.c_bill_no.get()}")
        self.text_area.insert(END,f"\n Name    : {self.c_name.get()}")
        self.text_area.insert(END,f"\n Phone   : {self.c_phone.get()}")
        self.text_area.insert(END,f"\n Email    : {self.c_email.get()}")

        self.text_area.insert(END,"\n***********************************************************")
        self.text_area.insert(END,f"\n PRODUCTS\t\t\tQUANTITY\t\t\tRATE")
        self.text_area.insert(END,"\n***********************************************************")
# ---------------------------------------------------category to product_type-------------------------------------------------------------------
    def categories(self,event=""):
        if self.combo_product_category.get()=="Cloths":
                self.combo_product_type.config(value=self.subclothing)
                self.combo_product_type.current(0)

        if self.combo_product_category.get()=="Cosmetics":
                self.combo_product_type.config(value=self.subcosmetics)
                self.combo_product_type.current(0)

        if self.combo_product_category.get()=="Electronics items":
                self.combo_product_type.config(value=self.subelectronics)
                self.combo_product_type.current(0)
# -------------------------------------------------------product_type to brand----------------------------------------------------------------------
    def product_type(self,event=""):
        if self.combo_product_type.get()=="Shirt":
                self.combo_brand.config(value=self.shirt)
                self.combo_brand.current(0)

        if self.combo_product_type.get()=="Pant":
                self.combo_brand.config(value=self.pant)
                self.combo_brand.current(0)

        if self.combo_product_type.get()=="Shoe":
                self.combo_brand.config(value=self.shoes)
                self.combo_brand.current(0)

        if self.combo_product_type.get()=="Facewash":
                self.combo_brand.config(value=self.facewash)
                self.combo_brand.current(0)

        if self.combo_product_type.get()=="Shampoo":
                self.combo_brand.config(value=self.shampoo)
                self.combo_brand.current(0)

        if self.combo_product_type.get()=="Oil":
                self.combo_brand.config(value=self.oil)
                self.combo_brand.current(0)

        if self.combo_product_type.get()=="Mobile":
                self.combo_brand.config(value=self.mobile)
                self.combo_brand.current(0)

        if self.combo_product_type.get()=="TV":
                self.combo_brand.config(value=self.tv)
                self.combo_brand.current(0)

        if self.combo_product_type.get()=="Laptop":
                self.combo_brand.config(value=self.laptop)
                self.combo_brand.current(0)

# -----------------------------------------------------------brand to rate-----------------------------------------------------------------------
    def brand(self,event=""):
        if self.combo_brand.get()=="polo":
                self.combo_rate.config(value=self.polo_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="tommy":
                self.combo_rate.config(value=self.tommy_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="apollo":
                self.combo_rate.config(value=self.apollo_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Dravis":
                self.combo_rate.config(value=self.dravis_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Raymond":
                self.combo_rate.config(value=self.raymond_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="wisley":
                self.combo_rate.config(value=self.wisley_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Nike":
                self.combo_rate.config(value=self.nike_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Puma":
                self.combo_rate.config(value=self.puma_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Adidas":
                self.combo_rate.config(value=self.adidas_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Himalayas":
                self.combo_rate.config(value=self.himalaya_price)
                self.combo_rate.current(0)   
                self.qty.set(1)

        if self.combo_brand.get()=="Nivia":
                self.combo_rate.config(value=self.nivia_price)
                self.combo_rate.current(0)    
                self.qty.set(1)

        if self.combo_brand.get()=="Geornia":
                self.combo_rate.config(value=self.geornia_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Herbal":
                self.combo_rate.config(value=self.herbal_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Letsliv":
                self.combo_rate.config(value=self.letliv_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Dove":
                self.combo_rate.config(value=self.dove_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Birdal":
                self.combo_rate.config(value=self.birdal_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Asvini":
                self.combo_rate.config(value=self.asvini_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Amazon":
                self.combo_rate.config(value=self.amazon_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Poco":
                self.combo_rate.config(value=self.poco_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Iphone":
                self.combo_rate.config(value=self.iphone_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Samsung":
                self.combo_rate.config(value=self.samsung_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Parasonic":
                self.combo_rate.config(value=self.parasonic_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Onida":
                self.combo_rate.config(value=self.onida_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="LDD":
                self.combo_rate.config(value=self.ldd_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="HP":
                self.combo_rate.config(value=self.hp_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Dell":
                self.combo_rate.config(value=self.dell_price)
                self.combo_rate.current(0)
                self.qty.set(1)

        if self.combo_brand.get()=="Lenovo":
                self.combo_rate.config(value=self.lenovo_price)
                self.combo_rate.current(0)
                self.qty.set(1)

if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()

