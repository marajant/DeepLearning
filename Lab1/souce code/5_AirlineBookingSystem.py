import random
class Person:
    """A simple person class"""
    def __init__(self,personName):
        self.__name = personName
    def returnName(self):
        return self.__name

class Employee(Person):
    """An employee class that inherits from person class, keeps track of salary and
    number of employees"""
    numOfEmployees = 0

    def __init__(self, personName, personSalary):
        Person.__init__(self,personName)
        self.salary = personSalary
        self.numOfEmployees +=1

    def returnSalary(self):
        return self.salary

class fulltimeEmployee(Employee):
    """Fulltime employee class that inherits from employee"""
    def __init__(self,personName, personSalary,hoursWorked):
        Employee.__init__(self,personName,personSalary)
        self.__hoursWorked = hoursWorked

    def isFullTime(self):
        if self.__hoursWorked >= 40: return True

    def addBonus(self):
        if fulltimeEmployee.isFullTime(self):
            self.salary += 10000

class flight():
    """Class that just holds a list that has the type of classes a flight has"""
    seats = ["First Class","Economy","Business"]

    def __init__(self):
        pass


class passenger(Person,flight):
    """Passenger class that inherits from person and flight"""
    def __init__(self,personName):
        Person.__init__(self,personName)
        self.bookingID = None
        self.seat = None

    def book(self):
        """Randomly assigns an int from 1000-10000
        and randomly assigns a seat from the list in flight"""
        self.bookingID = random.randint(1000,10000)
        self.seat = random.choice(flight.seats)

    def getBookingID(self):
        #returns an ID if passenger has booked a flight
        if self.bookingID is None: return None
        return self.bookingID

    def getSeat(self):
        #returns seat if passenger has booked a flight
        if self.seat is None: return None
        return self.seat

Dante = passenger("Dante")
Tutu = fulltimeEmployee("Tutu",98990,40)
Jordan = Employee("Jordan",32000)
Flights = flight()
Dante.book()

print("{0}'s salary is ${1} since he doesn't work full-time \n".format(Jordan.returnName(),Jordan.returnSalary()))

print("{0}'s starting salary is ${1}".format(Tutu.returnName(),Tutu.returnSalary()))


Tutu.addBonus()
print("After working three months the company gave {0} a raise. His new salary is ${1}\n".format(Tutu.returnName(),Tutu.returnSalary()))

print("{0}'s booking ID is #{1}, and his seat is in {2}".format(Dante.returnName(),Dante.getBookingID(),Dante.getSeat()))

