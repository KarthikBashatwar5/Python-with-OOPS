class vehicle:
    brand="BMW"
    model="M4"
    def display_details(self):
        print ("best luxury and sports car")
class car (vehicle):
    speed=370 
    mileage=10
class bike(vehicle) :
    brand="Triumph"
    variant="Daytona 625"
v=vehicle
b=bike
c=car
b.display_details(self)
c.display_details(self)
print(b.name)
print(c.name)


