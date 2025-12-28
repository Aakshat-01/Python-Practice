class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model

    def get_brand(self):
        return self.__brand
    def fullname(self):
        return f"{self.brand} {self.model}"
    
