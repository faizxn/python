
class Employee:

    name = "Osama Bin Laden"
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    def hasAchivedTarget(self):

        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved !!!")

        else:
            print("Target has not been achieved !!!")

emplyoee = Employee()
emplyoee.hasAchivedTarget()


----------------- Class and Instance Attributes ----------------------------------------------------


class Employee:
    numberOfWorkingHour = 40                ##Class Attributes##

employeeOne = Employee()
employeeTwo = Employee()

print(employeeOne.numberOfWorkingHour)
print(employeeTwo.numberOfWorkingHour)

Employee.numberOfWorkingHour = 50           ##Class Attributes##

print(employeeOne.numberOfWorkingHour)
print(employeeTwo.numberOfWorkingHour)

employeeOne.name = "Nushrat Ritu "          ##Instance Attributes##
employeeOne.study = "Bangladesh University "

print(employeeOne.name)
print(employeeOne.study)


------------------ Static and Instance Method ------------------------------------------------------


class Employee:

    def employeeDetails(self):
        self.name = "Nushrat Ritu"
        print(self.name)

    @staticmethod
    def welcomMessage():
        print("Welcome to our Organization !!")

employee = Employee()
employee.employeeDetails()
employee.welcomMessage()


------------------ Self Parameter ------------------------------------------------------


class Employee:

    def employeeDetails(self):
        self.name= "Nurhrat Ritu"
        print("Name : ", self.name)
        self.age = 22
        print("Age :", self.age)


    def printEmplyoeeDetails(self):
        print("Printing another method !!")
        print("Name : ", self.name)
        print("Age : ", self.age)

emplyoee = Employee()
emplyoee.employeeDetails()
emplyoee.printEmplyoeeDetails()


------------------ Init Method ---------------------------------------------------



class Employee:

    def employeeDetails(self):
        self.name = "Faiz"
        print(self.name)

    def displayEmployee(self):
        print(self.name)

employee = Employee()
employee.employeeDetails()        ##AttributeError wil appear if this method is not called##
employee.displayEmployee()


                    =>>>


class Employee:

    def __init__(self):
        self.name = "Nushrat Ritu "

    def displayEmployee(self):
        print(self.name)

employee = Employee()
employee.displayEmployee()



                    =>>>



class Employee:

    def __init__(self, name):
        self.name = name

    def displayEmployee(self):
        print(self.name)

employeeOne = Employee("Nushrat Ritu ")
employeeTwo = Employee("Muhammad Faizullah ")

employeeOne.displayEmployee()
employeeTwo.displayEmployee()

