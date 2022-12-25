from Project_Classes import *
from tkinter import *
import cv2 as cv
from sqlite3 import *
from prettytable import PrettyTable
from tkinter import messagebox
from imutils import resize


class Visualize:
    global list_of_raw_materials, list_of_products
    db = connect("Project_Database.db")
    list_of_raw_materials = []
    list_of_products = []
    
    for row in db.execute('SELECT Name FROM Raw_Materials'):
        if row[0] in list_of_raw_materials:
            pass
        else:
            list_of_raw_materials.append(row[0])
            
    for row in db.execute('SELECT Name FROM Products'):
        if row[0] in list_of_products:
            pass
        else:
            list_of_products.append(row[0])
        

    def __init__(self, main_page):
        self.main_page = main_page
        
        # <- Base Start Point
        
        main_page.title("Visualization")
        main_page.geometry("500x275")
        main_page.config(bg = "#e3dac9")
        main_page.resizable(0,0)
        
        # <- Base End Point
        #---------------------------------
        # <- Labelling Start Point
        
        main_page.raw_material_label = Label(main_page, text = "Raw Material", bg = "#e3dac9", font=("Arial", 17))
        main_page.raw_material_label.place(x = 25, y = 25)
        
        main_page.colon = Label(main_page, text = ":", bg = "#e3dac9", font=("Arial", 20))
        main_page.colon.place(x = 175, y = 20)
        
        main_page.Product_label = Label(main_page, text = "Product", bg = "#e3dac9", font=("Arial", 17))
        main_page.Product_label.place(x = 25, y = 75)
        
        main_page.colon = Label(main_page, text = ":", bg = "#e3dac9", font=("Arial", 20))
        main_page.colon.place(x = 175, y = 70)
        
        
        # <- Labelling End Point
        #---------------------------------
        # <- Option Menus Start Point
        
        main_page.raw_material_var = StringVar(main_page)
        main_page.raw_material_var.set("-")
        main_page.raw_material_option_menu = OptionMenu(main_page, main_page.raw_material_var, *list_of_raw_materials)
        main_page.raw_material_option_menu.config(width = 15, justify=CENTER)
        main_page.raw_material_option_menu.place(x = 195, y = 25)
        
        main_page.product_var = StringVar(main_page)
        main_page.product_var.set("-")
        main_page.product_option_menu = OptionMenu(main_page, main_page.product_var, *list_of_products)
        main_page.product_option_menu.config(width = 15, justify=CENTER)
        main_page.product_option_menu.place(x = 195, y = 75)
        
        # <- Option Menus End Point
        #---------------------------------
        # <- Show FUNCS Start Point
        
        def show_raw_material():
            image_of_raw_material = cv.imread("Images/Raw Materials/"+main_page.raw_material_var.get()+".png")
            image_of_raw_material = resize(image_of_raw_material, width=500)
            cv.imshow("Raw Material", image_of_raw_material)
            cv.waitKey(0)
            cv.destroyAllWindows()
            
            
        def show_product():
            image_of_product = cv.imread("Images/Products/"+main_page.product_var.get()+".png")
            image_of_product = resize(image_of_product, width=500)
            cv.imshow("Product", image_of_product)
            cv.waitKey(0)
            cv.destroyAllWindows()
            
        def show_cam():
            cam = cv.VideoCapture(0)
            while True:
                _, Video_Cam = cam.read()
                cv.imshow("Video_Cam", Video_Cam)
                key = cv.waitKey(1) 
                if key==27: 
                    break
            cam.release()
            cv.destroyAllWindows()
            
        def Raw_Material_Report():
            db = connect('Project_Database.db')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM Raw_Materials')

            col_names = [cn[0] for cn in cursor.description]
            rows = cursor.fetchall()

            x = PrettyTable(col_names)
            x.align[col_names[1]] = "l"
            x.align[col_names[2]] = "r"
            x.padding_width = 1
            for row in rows:
                x.add_row(row)
                
            tabstring = x.get_string()

            output=open("Raw Materials Report.txt","w")
            output.write(tabstring)
            output.close()
            db.close()
            
            messagebox.showinfo("Report", "Raw Material Report Has Generated !")

        def Product_Report():
            db = connect('Project_Database.db')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM Products')

            col_names = [cn[0] for cn in cursor.description]
            rows = cursor.fetchall()

            x = PrettyTable(col_names)
            x.align[col_names[1]] = "l"
            x.align[col_names[2]] = "r"
            x.padding_width = 1
            for row in rows:
                x.add_row(row)
                
            tabstring = x.get_string()

            output=open("Products Report.txt","w")
            output.write(tabstring)
            output.close()
            db.close()
            
            messagebox.showinfo("Report", "Product Report Has Generated !")
            
        # <- Show FUNCS End Point 
        #---------------------------------
        # <- Buttons Start Point
        
        main_page.img_button_Raw = Button(main_page, text= "Image", font=("Arial", 17),  command = show_raw_material)
        main_page.img_button_Raw.place(x = 350, y = 25, height=30)
        
        main_page.img_button_Product = Button(main_page, text= "Image", font=("Arial", 17),  command = show_product)
        main_page.img_button_Product.place(x = 350, y = 75, height=30)
        
        main_page.img_button_Cam = Button(main_page, text= "STRORAGE CAM", font=("Arial", 17),  command = show_cam)
        main_page.img_button_Cam.place(x = 25, y = 125, height=35,width= 450)
        
        main_page.img_button_Raw_Report = Button(main_page, text= "Raw Material Report", font=("Arial", 17),  command = Raw_Material_Report)
        main_page.img_button_Raw_Report.place(x = 25, y = 175, height=35,width= 450)
        
        main_page.img_button_Product_Report = Button(main_page, text= "Product Report", font=("Arial", 17),  command = Product_Report)
        main_page.img_button_Product_Report.place(x = 25, y = 225, height=35,width= 450)
        
        
        # <- Buttons End Point
        #---------------------------------
        