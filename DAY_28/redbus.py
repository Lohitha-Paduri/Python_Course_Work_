class Redbus:
    bus = {i: "Available" for i in range(1, 11)}
    bookings = {}
    driver_details = {}

    def displayseats(self):
        print("----------xyz bus---------")
        for i in Redbus.bus:
            print(i, Redbus.bus[i])


    def available_seats(self):
        count = 0

        for i in Redbus.bus:
            if Redbus.bus[i] == "Available":
                count += 1

        print("Available seats:", count)

    def booking(self, seatno, user):
        for i in Redbus.bus:
            if i == seatno and Redbus.bus[i] == "Available":
                Redbus.bus[i] = "Booked"
                Redbus.bookings[seatno] = {
                    "name": user.name,
                    "phone": user.phneno
                }

                print(f"Your seat - {seatno} is successfully booked")
                break

        else:
            print(f"Your seat - {seatno} is already booked")


class Users(Redbus):
    def __init__(self, name, email, phneno):
        self.name = name
        self.email = email
        self.phneno = phneno

    def view_driver(self):
        print("----------Driver Details----------")
        print("Driver Name:", Redbus.driver_details["name"])
        print("Driver Phone:", Redbus.driver_details["phone"])


class Drivers(Redbus):
    def __init__(self, name, email, phneno, salary):
        self.name = name
        self.phneno = phneno
        self.email = email
        self.__salary = salary

   
        Redbus.driver_details = {"name": self.name,"phone": self.phneno}

    def view_bookings(self):
        print("----------Passenger Details----------")

        for seat, user in Redbus.bookings.items():
            print("Seat:", seat)
            print("Passenger Name:", user["name"])
            print("Passenger Phone:", user["phone"])



lohitha = Users('Lohitha','padurilohitha@gmail.com',8327452760)
lohitha.available_seats()
lohitha.displayseats()
lohitha.booking(4, lohitha)
lohitha.booking(5, lohitha)
lohitha.available_seats()
lohitha.displayseats()




ram = Drivers('Ram','ram@gmail.com',947898573,50000)
ram.view_bookings()
lohitha.view_driver()  
    
    

  
