from tkinter import *
from sqlite3 import *

class Employee_add_to_DB():
        
        def __init__(self, add_page):
            self.main_page = add_page
            
            # <- Base Start Point
            
            add_page.title("Employee")
            add_page.geometry("500x350")
            add_page.config(bg = "#e3dac9")
            add_page.resizable(0,0)
            
            # <- Base End Point
            #---------------------------------
            # <- Labeles Start Point
            
            add_page.ID = Label(add_page, text= "ID", bg = "#e3dac9", font=("Arial", 15))
            add_page.ID.place(x = 25, y = 25)
            
            add_page.FullName = Label(add_page, text= "Full Name", bg = "#e3dac9", font=("Arial", 15))
            add_page.FullName.place(x = 25, y = 75)
            
            add_page.Password = Label(add_page, text= "Password", bg = "#e3dac9", font=("Arial", 15))
            add_page.Password.place(x = 25, y = 125)
            
            add_page.Cam_Access = Label(add_page, text= "Cam Access", bg = "#e3dac9", font=("Arial", 15))
            add_page.Cam_Access.place(x = 25, y = 175)
            
            add_page.Data_Access = Label(add_page, text= "Data Access", bg = "#e3dac9", font=("Arial", 15))
            add_page.Data_Access.place(x = 25, y = 225)
            
            for i in range(1, 6):
                add_page.coloni = Label(add_page, text = ":", bg = "#e3dac9", font=("Arial", 20))
                add_page.coloni.place(x = 200, y = i*50-30)
                
            # <- Labeles End Point
            #---------------------------------
            # <- Entries Start Point
        
            add_page.ID_Entry = Entry(add_page)
            add_page.ID_Entry.config(font = 15, width=20)
            add_page.ID_Entry.place(x =225, y = 30)
        
            add_page.FullName_Entry = Entry(add_page)
            add_page.FullName_Entry.config(font = 15, width=20)
            add_page.FullName_Entry.place(x =225, y = 80)
            
            add_page.Password_Entry = Entry(add_page, show="*")
            add_page.Password_Entry.config(font = 15, width=20)
            add_page.Password_Entry.place(x =225, y = 130)
            
            Cam_Var = IntVar()
            
            add_page.Cam_Access_radio = Radiobutton(add_page, text="Yes", variable=Cam_Var, value=1, bg="#e3dac9", font=15)
            add_page.Cam_Access_radio.place(x=225, y=180)

            add_page.Cam_Access_radio = Radiobutton(add_page, text="No", variable=Cam_Var, value=0, bg="#e3dac9", font=15)
            add_page.Cam_Access_radio.place(x=300, y=180)
            
            Data_Var = IntVar()
            
            add_page.Data_Access_radio = Radiobutton(add_page, text="Yes", variable=Data_Var, value=1, bg="#e3dac9", font=15)
            add_page.Data_Access_radio.place(x=225, y=230)

            add_page.Data_Access_radio = Radiobutton(add_page, text="No", variable=Data_Var, value=0, bg="#e3dac9", font=15)
            add_page.Data_Access_radio.place(x=300, y=230)
        
            # <- Entries End Point
            #---------------------------------
            # <- FUNCS Start Point
            
            def to_db():
                
                db = connect("Project_Database.db")
                cursor = db.cursor()
                inserter = """INSERT INTO Employee
                            (ID, FullName, Password, Cam_Access, Data_Access) 
                            VALUES (?, ?, ?, ?, ?);"""
                data_raw = (add_page.ID_Entry.get(), 
                            add_page.FullName_Entry.get(),
                            add_page.Password_Entry.get(),
                            Cam_Var.get(),
                            Data_Var.get()
                            )
                cursor.execute(inserter, data_raw)
                db.commit()
                cursor.close()
            
            def remove_db():
                db = connect("Project_Database.db")
                cursor = db.execute("""SELECT * FROM Employee""")
                deleter = '''DELETE FROM Employee WHERE ID = '''+add_page.ID_Entry.get()+''' AND FullName = "'''+add_page.FullName_Entry.get()+'''" AND Password = "'''+add_page.Password_Entry.get()+'''" AND Cam_Access = '''+ str(Cam_Var.get()) + ''' AND Data_Access = '''+ str(Data_Var.get())
                db.execute(deleter)
                db.commit()
                cursor.close()
            # <- FUNCS End Point
            #---------------------------------
            # <- Buttons Start Point
            
            add_page.add_button = Button(add_page, text="Add to database", command= to_db, font="bold")
            add_page.add_button.place(x = 20, y = 280,width = 225, height=50)
            
            add_page.remove_button = Button(add_page, text="Remove from database", command= remove_db, font="bold")
            add_page.remove_button.place(x = 255, y = 280,width = 225, height=50)
            
window = Tk()    
gui = Employee_add_to_DB(window)
window.mainloop()