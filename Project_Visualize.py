from Project_Classes import *
from tkinter import *
import cv2 as cv
from sqlite3 import *


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
        main_page.geometry("500x200")
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
            image_of_raw_material = cv.imread("Images/"+main_page.raw_material_var.get()+".png")
            cv.imshow("Raw Material", image_of_raw_material)
            cv.waitKey(0)
            cv.destroyAllWindows()
            
            
        def show_product():
            image_of_product = cv.imread("Images/"+main_page.product_var.get()+".png")
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
            
        # <- Show FUNCS End Point 
        #---------------------------------
        # <- Buttons Start Point
        
        main_page.img_button = Button(main_page, text= "Image", font=("Arial", 17), bg = "#e3dac9", command = show_raw_material)
        main_page.img_button.place(x = 350, y = 25, height=30)
        
        main_page.img_button = Button(main_page, text= "Image", font=("Arial", 17), bg = "#e3dac9", command = show_product)
        main_page.img_button.place(x = 350, y = 75, height=30)
        
        main_page.img_button = Button(main_page, text= "STRORAGE CAM", font=("Arial", 17), bg = "#e3dac9", command = show_cam)
        main_page.img_button.place(x = 25, y = 125, height=35,width= 450)
        
        
        # <- Buttons End Point
        #---------------------------------
        