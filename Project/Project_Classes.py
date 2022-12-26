from abc import ABC, abstractmethod


class RawMaterials(ABC):
    def __init__(self, Name, Date_of_purchase, Name_of_Supplier, Storage_expiration_date, Storage_code, Description):
        self.Name = Name
        self.Date_of_purchase = Date_of_purchase
        self.Name_of_Supplier = Name_of_Supplier
        self.Storage_expiration_date = Storage_expiration_date
        self.Storage_code = Storage_code
        self.Description = Description

    #   Setters
    @abstractmethod
    def set_Name(self, Name):
        self.Name = Name

    def set_Date_of_purchase(self, Date_of_purchase):
        self.Date_of_purchase = Date_of_purchase

    def set_Name_of_Supplier(self, Name_of_Supplier):
        self.Name_of_Supplier = Name_of_Supplier

    def set_Storage_expiration_date(self, Storage_expiration_date):
        self.Storage_expiration_date = Storage_expiration_date
        
    @abstractmethod
    def set_Storage_code(self, Storage_code):
        self.Storage_code = Storage_code
        
    @abstractmethod
    def set_Description(self, Description):
        self.Description = Description

    #   Getters
    @abstractmethod
    def get_Name(self):
        return self.Name

    def get_Date_of_purchase(self):
        return self.Date_of_purchase

    def get_Name_of_Supplier(self):
        return self.Name_of_Supplier

    def get_Storage_expiration_date(self):
        return self.Storage_expiration_date
    
    @abstractmethod
    def get_Storage_code(self):
        return self.Storage_code
    
    @abstractmethod
    def get_Description(self):
        return self.Description


class Products(RawMaterials):
    def __init__(self, Name, Date_of_Production, Name_of_Customer, Product_expiration_date, Storage_code, list_of_raw_used, Description):
        self.Name = Name
        self.Date_of_Production = Date_of_Production
        self.Name_of_Customer = Name_of_Customer
        self.Product_expiration_date = Product_expiration_date
        self.Storage_code = Storage_code
        self.list_of_raw_used = list_of_raw_used
        self.Description = Description

    #   Setters

    def set_Name(self, Name):
        self.Name = Name

    def set_Date_of_Production(self, Date_of_Production):
        self.Date_of_Production = Date_of_Production

    def set_Name_of_Customer(self, Name_of_Customer):
        self.Name_of_Customer = Name_of_Customer

    def set_Product_expiration_date(self, Product_expiration_date):
        self.Product_expiration_date = Product_expiration_date

    def set_Storage_code(self, Storage_code):
        self.Storage_code = Storage_code

    def set_list_of_raw_used(self, list_of_raw_used):
        self.list_of_raw_used = list_of_raw_used

    def set_Description(self, Description):
        self.Description = Description

    #   Getters

    def get_Name(self):
        return self.Name

    def get_Date_of_Production(self):
        return self.Date_of_Production

    def get_Name_of_Customer(self):
        return self.Name_of_Customer

    def get_Product_expiration_date(self):
        return self.Product_expiration_date

    def get_Storage_code(self):
        return self.Storage_code

    def get_list_of_raw_used(self):
        return self.list_of_raw_used

    def get_Description(self):
        return self.Description
