class Vichelle:
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.rental_price_per_day=rental_price_per_day

 
   
class Car(Vichelle):
    def calculate_rental_cars(self,days):
        return self.rental_price_per_day + days


