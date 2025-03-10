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

    def __init__(self, brand, model, year, rental_price_per_day,seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity=seating_capacity

     
    def displayInfo(self):
        print(f"this car of Brand {self.brand} with model of {self.model} at year {self.year} and a price of {self.get_rental_price_per_day()} $ /day with a {self.seating_capacity} seat") 
   
    def calculate_rental_cost(self,days):
        i=0
        rental_cost=0
        while i<days:
           rental_cost+=50
           i+=1
        print(f"Rental cost for {self.brand} {self.model} for {days} days : {rental_cost} $")

class Bike(Vichelle):

    def __init__(self,brand,model,year,rental_price_per_day,engine_capacity): 
        super().__init__(brand,model,year,rental_price_per_day)
        self.engine_capacity=engine_capacity

    def displayInfo(self):
        print(f"this car of Brand {self.brand} with model of {self.model} at year {self.year} and a price of {self.get_rental_price_per_day()} $ /day and a  {self.engine_capacity} cc of Engine Capacity") 
    
    def calculate_rental_cost(self,days):
        i=0
        rental_cost=0
        while i<days:
           rental_cost+=30
           i+=1
        print(f"Rental cost for {self.brand} {self.model} for {days} days : {rental_cost} $")

toyota=Car("Toyota","Corolla",2020,50,5)
yamaha=Bike("Yamaha","R1",2019,30,998)

#creating a function 
def show_vicheles_info(vichelle):
    return vichelle
 
show_vicheles_info(toyota.displayInfo())
show_vicheles_info(yamaha.displayInfo())
show_vicheles_info(toyota.calculate_rental_cost(3))
show_vicheles_info(yamaha.calculate_rental_cost(5))
#updating rental price using setter method
show_vicheles_info(toyota.set_rental_price_per_day(55))
result=f"The Updated Rental Price of {toyota.brand} is {show_vicheles_info(toyota.get_rental_price_per_day())}$/day "

print(result)