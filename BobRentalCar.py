class Vichelle:
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.rental_price_per_day=rental_price_per_day

    def displayInfo(self):
        print(f"this car of Brand {self.brand} with model of {self.model} at year {self.year} and of {self.rental_price_per_day}")
    
   
class Car(Vichelle):
    def calculate_rental_cars(self,days):
        return self.rental_price_per_day + days
    def __init__(self, brand, model, year, rental_price_per_day,seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity=seating_capacity
    

