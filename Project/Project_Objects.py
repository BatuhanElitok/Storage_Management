from Project_Classes import *
from tkinter import *
from tkcalendar import DateEntry
from sqlite3 import *

class Raw_add_to_DB():
        
        def __init__(self, add_page):
            self.main_page = add_page
            
            # <- Base Start Point
            
            add_page.title("Raw Material")
            add_page.geometry("500x500")
            add_page.config(bg = "#e3dac9")
            add_page.resizable(0,0)
            
            # <- Base End Point
            #---------------------------------
            # <- Labeles Start Point
            
            add_page.Name = Label(add_page, text= "Name", bg = "#e3dac9", font=("Arial", 15))
            add_page.Name.place(x = 25, y = 25)

            add_page.Date_of_purchase = Label(add_page, text= "Date of Purchase", bg = "#e3dac9", font=("Arial", 15))
            add_page.Date_of_purchase.place(x = 25, y = 75)
            
            add_page.Name_of_Supplier = Label(add_page, text= "Name of Supplier", bg = "#e3dac9", font=("Arial", 15))
            add_page.Name_of_Supplier.place(x = 25, y = 125)
            
            add_page.Storage_expiration_date = Label(add_page, text= "Storage Expiration Date", bg = "#e3dac9", font=("Arial", 15))
            add_page.Storage_expiration_date.place(x = 25, y = 175)
            
            add_page.Storage_code = Label(add_page, text= "Storage Code", bg = "#e3dac9", font=("Arial", 15))
            add_page.Storage_code.place(x = 25, y = 225)
            
            add_page.Description = Label(add_page, text= "Description", bg = "#e3dac9", font=("Arial", 15))
            add_page.Description.place(x = 25, y = 275)
            
            for i in range(1, 7):
                add_page.coloni = Label(add_page, text = ":", bg = "#e3dac9", font=("Arial", 20))
                add_page.coloni.place(x = 275, y = i*50-30)
                
            # <- Labeles End Point
            #---------------------------------
            # <- Entries Start Point
        
            add_page.Name_Entry = Entry(add_page)
            add_page.Name_Entry.config(font = 15, width=15)
            add_page.Name_Entry.place(x =300, y = 30)
            
            add_page.Date_of_purchase_Enrty = DateEntry(add_page, selectmode = "day",)
            add_page.Date_of_purchase_Enrty.config(width = 14,font = 15)
            add_page.Date_of_purchase_Enrty.place(x = 300, y = 80)
            
            add_page.Name_of_Supplier_Entry = Entry(add_page)
            add_page.Name_of_Supplier_Entry.config(font = 15, width=15)
            add_page.Name_of_Supplier_Entry.place(x =300, y = 130)
            
            add_page.Storage_expiration_date_Enrty = DateEntry(add_page, selectmode = "day",)
            add_page.Storage_expiration_date_Enrty.config(width = 14,font = 15)
            add_page.Storage_expiration_date_Enrty.place(x = 300, y = 180)
            
            add_page.Storage_code_Entry = Entry(add_page)
            add_page.Storage_code_Entry.config(font = 15, width=15)
            add_page.Storage_code_Entry.place(x =300, y = 230)
            
            add_page.Description_Entry = Entry(add_page)
            add_page.Description_Entry.config(font = 15, width=15)
            add_page.Description_Entry.place(x =300, y = 280)
            
            # <- Entries End Point
            #---------------------------------
            # <- FUNCS Start Point
            
            def to_db():
                
                db = connect("Project_Database.db")
                cursor = db.cursor()
                inserter = """INSERT INTO Raw_Materials
                            (Name, Date_of_purchase, Name_of_Supplier, Storage_expiration_date, Storage_code, Description) 
                            VALUES (?, ?, ?, ?, ?, ?);"""
                data_raw = (add_page.Name_Entry.get(), 
                            add_page.Date_of_purchase_Enrty.get(),
                            add_page.Name_of_Supplier_Entry.get(),
                            add_page.Storage_expiration_date_Enrty.get(),
                            add_page.Storage_code_Entry.get(),
                            add_page.Description_Entry.get()
                            )
                cursor.execute(inserter, data_raw)
                db.commit()
                cursor.close()
            
            def remove_db():
                db = connect("Project_Database.db")
                cursor = db.execute("""SELECT * FROM Raw_Materials""")
                deleter = '''DELETE FROM Employee WHERE Name = "'''+add_page.Name_Entry.get()+'''" AND Date_of_purchase = '''+add_page.Date_of_purchase_Enrty.get()+''' AND Name_of_Supplier = "'''+add_page.Name_of_Supplier_Entry.get()+'''" AND Storage_expiration_date = '''+ add_page.Storage_expiration_date_Enrty.get() + ''' AND   Description =  "'''+add_page.Description_Entry.get()+'''"'''
                db.execute(deleter)
                db.commit()
                cursor.close()
                    
            # <- FUNCS End Point
            #---------------------------------
            # <- Buttons Start Point

            add_page.Add_button = Button(add_page, text = "Add to Database", command= to_db)
            add_page.Add_button.place(x = 20, y = 330, width = 225, height=50)
            
            
            add_page.Add_button = Button(add_page, text = "Remove from Database", command= remove_db)
            add_page.Add_button.place(x = 255, y = 330, width = 225, height=50)
            
            
            
class Product_add_to_DB():
        
        def __init__(self, add_page):
            self.main_page = add_page
            
            # <- Base Start Point
            
            add_page.title("Product")
            add_page.geometry("500x500")
            add_page.config(bg = "#e3dac9")
            add_page.resizable(0,0)
            
            # <- Base End Point
            #---------------------------------
            # <- Labeles Start Point
            
            add_page.Name = Label(add_page, text= "Name", bg = "#e3dac9", font=("Arial", 15))
            add_page.Name.place(x = 25, y = 25)

            add_page.Date_of_Production = Label(add_page, text= "Date of Production", bg = "#e3dac9", font=("Arial", 15))
            add_page.Date_of_Production.place(x = 25, y = 75)
            
            add_page.Name_of_Customer = Label(add_page, text= "Name of Customer", bg = "#e3dac9", font=("Arial", 15))
            add_page.Name_of_Customer.place(x = 25, y = 125)
            
            add_page.Product_expiration_date = Label(add_page, text= "Product Expiration Date", bg = "#e3dac9", font=("Arial", 15))
            add_page.Product_expiration_date.place(x = 25, y = 175)
            
            add_page.Storage_code = Label(add_page, text= "Storage Code", bg = "#e3dac9", font=("Arial", 15))
            add_page.Storage_code.place(x = 25, y = 225)
            
            add_page.list_of_raw_used = Label(add_page, text= "List of Raw Used", bg = "#e3dac9", font=("Arial", 15))
            add_page.list_of_raw_used.place(x = 25, y = 275)
            
            add_page.Description = Label(add_page, text= "Description", bg = "#e3dac9", font=("Arial", 15))
            add_page.Description.place(x = 25, y = 325)
            
            for i in range(1, 8):
                add_page.coloni = Label(add_page, text = ":", bg = "#e3dac9", font=("Arial", 20))
                add_page.coloni.place(x = 275, y = i*50-30)
                
            # <- Labeles End Point
            #---------------------------------
            # <- Entries Start Point
        
            add_page.Name_Entry = Entry(add_page)
            add_page.Name_Entry.config(font = 15, width=14)
            add_page.Name_Entry.place(x =300, y = 30)
            
            add_page.Date_of_Production_Enrty = DateEntry(add_page, selectmode = "day",)
            add_page.Date_of_Production_Enrty.config(width = 13,font = 15)
            add_page.Date_of_Production_Enrty.place(x = 300, y = 80)
            
            add_page.Name_of_Customer_Entry = Entry(add_page)
            add_page.Name_of_Customer_Entry.config(font = 15, width=14)
            add_page.Name_of_Customer_Entry.place(x =300, y = 130)
            
            add_page.Product_expiration_date_Enrty = DateEntry(add_page, selectmode = "day",)
            add_page.Product_expiration_date_Enrty.config(width = 13,font = 15)
            add_page.Product_expiration_date_Enrty.place(x = 300, y = 180)
            
            add_page.Storage_code_Entry = Entry(add_page)
            add_page.Storage_code_Entry.config(font = 15, width=14)
            add_page.Storage_code_Entry.place(x =300, y = 230)
            
            add_page.list_of_raw_used_Entry = Entry(add_page)
            add_page.list_of_raw_used_Entry.config(font = 15, width=14)
            add_page.list_of_raw_used_Entry.place(x =300, y = 280)
            
            add_page.Description_Entry = Entry(add_page)
            add_page.Description_Entry.config(font = 15, width=14)
            add_page.Description_Entry.place(x =300, y = 330)
            
            # <- Entries End Point
            #---------------------------------
            # <- FUNCS Start Point
            
            def to_db():
                
                db = connect("Project_Database.db")
                cursor = db.cursor()
                inserter = """INSERT INTO Products
                            (Name, Date_of_Production, Name_of_Customer, Product_expiration_date, Storage_code, list_of_raw_used, Description) 
                            VALUES (?, ?, ?, ?, ?, ?,?);"""
                data_raw = (add_page.Name_Entry.get(), 
                            add_page.Date_of_Production_Enrty.get(),
                            add_page.Name_of_Customer_Entry.get(),
                            add_page.Product_expiration_date_Enrty.get(),
                            add_page.Storage_code_Entry.get(),
                            add_page.list_of_raw_used_Entry.get(),
                            add_page.Description_Entry.get()
                            )
                cursor.execute(inserter, data_raw)
                db.commit()
                cursor.close()
            
            def remove_db():
                db = connect("Project_Database.db")
                cursor = db.execute("""SELECT * FROM Prodcuts""")
                deleter = '''DELETE FROM Employee WHERE Name = "'''+add_page.Name_Entry.get()+'''" AND Date_of_Production = '''+add_page.Date_of_Production_Enrty.get()+''' AND Name_of_Customer = "'''+add_page.Name_of_Customer_Entry.get()+'''" AND Product_expiration_date = '''+ add_page.Product_expiration_date_Enrty.get() + ''' AND list_of_raw_used = "'''+ add_page.list_of_raw_used_Entry.get()+'''" AND   Description =  "'''+add_page.Description_Entry.get()+'''"'''
                db.execute(deleter)
                db.commit()
                cursor.close()
                    
            # <- FUNCS End Point
            #---------------------------------
            # <- Buttons Start Point

            add_page.Add_button = Button(add_page, text = "Add to Database", command= to_db)
            add_page.Add_button.place(x = 20, y = 380, width = 225, height=50)
            
            add_page.Add_button = Button(add_page, text = "Remove from Database", command= remove_db)
            add_page.Add_button.place(x = 255, y = 380, width = 225, height=50)
