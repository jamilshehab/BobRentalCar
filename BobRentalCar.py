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
    
    def __init__(self, brand, model, year, rental_price_per_day,seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity=seating_capacity

    def displayInfo(self):
        print(f"this car of Brand {self.brand} with model of {self.model} at year {self.year} and a price of {self.get_rental_price_per_day()} with a {self.seating_capacity} seat") 
   
    def calculate_rental_cost(self,days):
        # user=int(input("Enter How Many Days : "))
        rental_cost=0
        while days:
           rental_cost+=50
        print(f"Rental cost for {self.brand} {self.model} for {days} days")

class Bike(Vichelle):

    def __init__(self,brand,model,year,rental_price_per_day,engine_capacity): 
        super().__init__(brand,model,year,rental_price_per_day)
        self.engine_capacity=engine_capacity

    def displayInfo(self):
        print(f"this car of Brand {self.brand} with model of {self.model} at year {self.year} and a price of {self.get_rental_price_per_day()} with a {self.engine_capacity} cc") 
    
    def calculate_rental_cost(self,days):
        # user=int(input("Enter How Many Days : "))
        rental_cost=0
        while days:
           rental_cost+=30
        print(f"Rental cost for {self.brand} {self.model} for {days} days")

toyota=Car("Toyota","Corolla",5,2020,50)
yamaha=Bike("Yamaha","R1",2019,30,998)

#creating a function 
def show_vicheles_info(vichelle):
    return vichelle
 
show_vicheles_info(toyota.displayInfo())
show_vicheles_info(yamaha.displayInfo())