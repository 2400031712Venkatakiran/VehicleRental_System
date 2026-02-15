from abc import ABC, abstractmethod
class Vehicle:
    def __init__(self,vehicle_id,brand):
        self.vehicle_id=vehicle_id
        self.brand=brand
    def display(self):
        print(f"Vehicle id is {self.vehicle_id} and brand is {self.brand}")
class Car(Vehicle):
    def __init__(self,vehicle_id,brand,rate_per_day=0):
        super().__init__(vehicle_id,brand)
        self.rate_per_day=900
    def rent_per_day(self,days):
        return self.rate_per_day*days
class Bike(Vehicle):
    def __init__(self,vehicle_id,brand,rate_per_day=500):
        super().__init__(vehicle_id,brand)
        self.rate_per_day=500
    def rent_per_day(self,days):

        return self.rate_per_day*days
class RentalRecord:
    def __init__(self,Vehicle,days):
        self.Vehicle=Vehicle
        self.days=days
    def calculate_rent(self):
        return self.Vehicle.rent_per_day(self.days)
class RentalManager:
    def __init__(self):
        self.rental_records={}
        self.vehicles={}
    def add_vehicle(self,vehicle):
        self.vehicles[vehicle.vehicle_id]=vehicle
        return f"Vehicle added"
    def rent_vehicle(self,vehicle_id,days):
        if vehicle_id in self.vehicles:
            self.rental_records[vehicle_id]=RentalRecord(self.vehicles[vehicle_id],days)
            return f"Vehicle rented"
        else:
            return f"please enter a valid vehicle id"
    def return_vehicle(self,vehicle_id):
        if vehicle_id in self.rental_records:
            del self.rental_records[vehicle_id]
            return f"Vehicle was returned"
        else:
            return f"please enter a valid vehicle id"
    def show_rentals(self):
        for i in self.rental_records:
            print(self.vehicles[rental_records[i]].display())
            print(self.rental_records[i].days)
            print(self.rental_records[i].calculate_rent())
def main():
    manager=RentalManager()
    while(1):
        print("1. Add Car\n2. Add Bike\n3. Rent Vehicle\n4. Return Vehicle\n5. Show Rentals\n6. Exit")
        choice=int(input("Enter the valid choice:"))
        if choice == 1:
            vehicle_id=int(input("enter vehicle id"))
            brand=input("enter the brand")
            print(manager.add_vehicle(Car(vehicle_id,brand)))
        elif choice == 2:
            vehicle_id=int(input("enter the vehicle id"))
            brand=input("enter the brand ")
            print(manager.add_vehicle(Bike(vehicle_id,brand)))
        elif choice == 3:
            vehicle_id=int(input("enter the vehicle id:"))
            days=int(input("enter the days of rent"))
            print(manager.rent_vehicle(vehicle_id,days))
        elif choice == 4:
            vehicle_id=int(input("enter the vehicle id: "))
            print(manager.return_vehicle(vehicle_id))
        elif choice==5:
            manager.show_rentals()
        elif choice==6:
            break
        else:
            print("enter the valid choice")
if __name__ == '__main__':
    main()