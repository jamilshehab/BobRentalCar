class Vichelle:

    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.__rental_price_per_day=rental_price_per_day #making this variable private 
    
    def get_rental_price_per_day(self):
        return self.__rental_price_per_day

    def set_rental_price_per_day(self,value):
        self.__rental_price_per_day=value

    def displayInfo(self):
        print(f"this car of Brand {self.brand} with model of {self.model} at year {self.year} and a price of {self.get_rental_price_per_day()} ")
    
   
class Car(Vichelle):

    def calculate_rental_cars(self,days):
        return self.rental_price_per_day + days
    
    def __init__(self, brand, model, year, rental_price_per_day):
        super().__init__(brand, model, year, rental_price_per_day)

    def displayInfo(self,seating_capacity):
        print(f"this car of Brand {self.brand} with model of {self.model} at year {self.year} and a price of {self.get_rental_price_per_day()} with a {seating_capacity}") 
    
class Bike(Vichelle):
    def __init__(self,brand,model,year,rental_price_per_day,engine_capacity): 
        super().__init__(brand,model,year,rental_price_per_day)
        self.engine_capacity=engine_capacity
bmw=Car("Toyota","Corolla",2020,50)
bmw.displayInfo(seating_capacity=5);

 