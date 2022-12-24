from Project_Objects import *
from Project_Visualize import *
from sqlite3 import *

class open_access_page():
    def __init__(self, access_page):
        self.main_page = access_page
        
        # <- Base Start Point
    
        access_page.title("User Panel")
        access_page.geometry("500x500")
        access_page.resizable(0,0)
        access_page.config(bg = "#e3dac9")
        
        # <- Base End Point
        #---------------------------------
        # <- Labeles Start Point
        
        access_page.login_label = Label(access_page, text = "LOGIN", font = ("Arial", 45, "bold"), bg = "#e3dac9",relief=SOLID)
        access_page.login_label.place(x = 150, y = 60)
        
        access_page.ID_label = Label(access_page, text = "ID", font = ("Arial", 17), bg = "#e3dac9")
        access_page.ID_label.place(x = 75, y = 200)
        
        access_page.Password_label = Label(access_page, text = "Password", font = ("Arial", 17), bg = "#e3dac9")
        access_page.Password_label.place(x = 75, y = 250)
        
        for i in range(1, 3):
                access_page.coloni = Label(access_page, text = ":", bg = "#e3dac9", font=("Arial", 20))
                access_page.coloni.place(x = 200, y = i*50+145)
                
        # <- Labeles End Point
        #---------------------------------
        # <- Entries Start Point
        
        access_page.ID_Entry = Entry(access_page)
        access_page.ID_Entry.config(width = 20, font = 15)
        access_page.ID_Entry.place(x = 225, y =205)
        
        access_page.Password_Entry = Entry(access_page, show = "*")
        access_page.Password_Entry.config(width = 20, font = 15)
        access_page.Password_Entry.place(x = 225, y =255)
        
        # <- Entries End Point
        #---------------------------------
        # <- FUNCS Start Point
        
        def login():
            db = connect("Project_Database.db")
            cursor = db.cursor()
            cursor.execute('''SELECT * FROM Employee WHERE ID = '''+access_page.ID_Entry.get())
            data = cursor.fetchall()
            if access_page.Password_Entry.get() == data[0][2]:
                if data[0][3] == 1 and data[0][4] == 1:
                    access_page.destroy()
                    window = Tk()  
                    Raw_add_to_DB(window)
                    main_window = Tk()
                    Visualize(main_window)
                    window2 = Tk()
                    Product_add_to_DB(window2)
                    window.mainloop()
                    main_window.mainloop()
                    window2.mainloop() 
                    
                elif data[0][3] == 1:
                    access_page.destroy()
                    main_window = Tk()
                    Visualize(main_window)
                    main_window.mainloop()
                
                elif data[0][4] == 1:
                    access_page.destroy()
                    window = Tk()
                    Raw_add_to_DB(window)
                    window2 = Tk()
                    Product_add_to_DB(window2)
                    window.mainloop() 
                    window2.mainloop() 
                
                
        # <- FUNCS End Point 
        #--------------------------------
        # <- Buttons Start Point
        
        access_page.login_button = Button(access_page, text="Login", font=(20),command=login, bg="green")
        access_page.login_button.place(x = 75, y =305, width=150, height = 35)
        
        access_page.exit_button = Button(access_page, text="Exit", font=(20),command=exit, bg="red")
        access_page.exit_button.place(x = 260, y =305, width=150, height = 35)
        

        
window = Tk()
gui = open_access_page(window)
window.mainloop()