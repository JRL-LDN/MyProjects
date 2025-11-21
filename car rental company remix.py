class Car():
    def __init__(self, numberPlate, make, model, availablbility):
        self.numberPlate = numberPlate
        self.make = make
        self.model = model
        self.availablbility = availablbility

    def hireThisCar(self):
        self.availablbility = False
        print(self.numberPlate + " Car has been rented out. It is not available")

    def returnThisCar(self):
        self.availablbility = True
        print("Car has been returned and is now available")

    def isAvailable(self):
        return self.availablbility

    def getCarNumber(self):
        return self.numberPlate

    def __str__(self):
        return str(self.numberPlate) + " " + str(self.make) + " " + str(self.model) + " " + str(self.availablbility)

class Customer():
    def __init__(self, name, licenseNumber, phoneNumber):
        self.name = name
        self.licenseNumber = licenseNumber
        self.phoneNumber = phoneNumber

    def __str__(self):
        return str(self.name) + " " + str(self.licenseNumber)

class CarRentalCompany():
    def __init__(self, companyName):
        self.companyName = companyName
        self.carList = []
        self.customerList = []
        self.CarCustomerMap = {}

    def addCar(self, car):
        self.carList.append(car)

    def addCustomer(self, customer):
        self.customerList.append(customer)

    def initializeCars(self):
        self.carList= [
        Car("AB123", "BMW", "5series", True),
        Car("CD123", "BMW", "3series", True),
        Car("BCD123", "BMW", "7series", True),
        Car("D123", "BMW", "1series", True),
        Car("MNP123", "BMW", "X5", True),
        Car("BC123", "BMW", "X3", True),
        Car("123ABC", "Mercedes", "Cclass", True),
        Car("987ABC", "Mercedes", "EClass", True),
        Car("PQR123", "Mercedes", "SClass", True),
        Car("123PQR", "Mercedes", "GLE", True)
        ]

    def initializeCustomers(self):
        self.customerList= [
        Customer("Alice", "123456PQR", 98765),
        Customer("JIb", "6786545ABC", 987546465),
        Customer("Samuel", "123ABC456", 12398765),
        Customer("Alex", "123PQR456", 987634455),
        Customer("Bob", "123XYX456", 98765123)
        ]

    def printAllAvailableCars(self):
        print(self.companyName, "STATUS REPORT")

        print("Cars:")
        for car in self.carList:
            if(car.isAvailable()):
                print(car)

        '''
        print("Customers:")
        for customer in self.customerList:
            print(customer)
            '''
        '''I added input validation to the function because if the wrong car number is used,
     which may not exist, it gets added to the dictionary and assigns that carNumber to the customerLicense.
      Due to the loop the availability of the car doesn't change as hireThisCar() never runs.
      This means the system incorrectly thinks a non-existent car has been hired.'''

    def RentACar(self, carNumber, customerLicense):
        foundCar = None
        for car in self.carList:
            if car.getCarNumber() == carNumber:
                foundCar = car
                break

        if foundCar is None:
            print("Car does not exist")
            return

        if carNumber in  self.CarCustomerMap.keys():
            print("Car is already hired")
            return

        self.CarCustomerMap[carNumber] = customerLicense
        foundCar.hireThisCar()

        '''for car in self.carList:
                if(car.getCarNumber() == carNumber ):
                    car.hireThisCar()'''

    def printRentedCarDetails(self):
        for car in self.CarCustomerMap:
            print(car, self.CarCustomerMap[car])

def main():
    companyName = "ABCDCarRental"
    companyName = companyName.capitalize()

    crc = CarRentalCompany(companyName)
    crc.initializeCars()
    crc.initializeCustomers()

    crc.printAllAvailableCars()

    print("----------------------")
    print("now renting...:")
    print("----------------------")

    crc.RentACar("CD123", "123PQR456")
    crc.RentACar("D123", "123ABC456")

    print("----------------------")
    print("Already rented cars:")
    print("----------------------")

    crc.printRentedCarDetails()

    print("----------------------")
    print("hiring another car to another customer:")
    print("----------------------")

    crc.RentACar("AB123", "6786545ABC")

    print("----------------------")
    print("Already rented cars:")
    print("----------------------")

    crc.printRentedCarDetails()

    print("----------------------")
    print("updated available cars:")
    print("----------------------")

    crc.printAllAvailableCars()

if __name__ == "__main__":
    main()
