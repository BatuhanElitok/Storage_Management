from prettytable import PrettyTable
from sqlite3 import *

class Raw_Material_Report:
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
    
class Products_Report:
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