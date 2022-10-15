# Part A: Create a class vehicle 

class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name= name
    
    def getMax_speed(self):
        return self.max_speed
    def setMax_speed(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
            return 'Name of Vehicle is: '+ str(self.name) +' and its max_speed is: '+str(self.max_speed)


# Tests for part A

# print('------ Part A ------')
# v = Vehicle('car1',200)

# print(v.__str__())
# print(v.getName())
# print(v.getMax_speed())
# v.setName('carModified')
# v.setMax_speed(150)
# print("**************")
# print(v.__str__())
# print(v.getName())
# print(v.getMax_speed())
# print("**************")
# print('------ End Part A ------')


# Part B: Inheritance to Car and Aeroplane

class Car(Vehicle):
    
    def __init__(self,name,max_speed, number_of_cylinders):
        super().__init__(name,max_speed)
        self.number_of_cylinders = number_of_cylinders

    def getNumber_of_cylinders(self):
        return self.number_of_cylinders

    def setNumber_of_cylinders(self,newNumber_of_cylinders):
        self.number_of_cylinders = newNumber_of_cylinders

    def __str__(self):
        return 'Name of Vehicle is: '+ str(self.name) +',its max_speed is: '+str(self.max_speed) + 'And its Number of Cylinders is: ' + str(self.number_of_cylinders)


# Tests for part B

# print('------ Part B ------')

# car =  Car(1,2,3)
# print(car.__str__())
# print(car.getNumber_of_cylinders())
# print('****************')
# car.setNumber_of_cylinders(80)
# print(car.getNumber_of_cylinders())
# car.setName('newname')
# car.setMax_speed(90000)
# print(car.getName())
# print(car.__str__())
# print('------ End Part B ------')


# Part C the aeroplane

class Aeroplane(Vehicle):
    def __init__(self, name, max_speed,number_of_engines):
        super().__init__(name, max_speed)
        self.number_of_engines =number_of_engines
    
    def getNumber_of_engines(self):
        return self.number_of_engines

    def setNumber_of_engines(self,newNumber_of_engines):
        self.number_of_engines = newNumber_of_engines

    def __str__(self):
        return 'Name of Vehicle is: '+ str(self.name) +' ,its max_speed is: '+str(self.max_speed) + ' And its Number of Engines is: ' + str(self.number_of_engines)


# Tests for part C

# print('------ Part C ------')

# aeroplane =  Aeroplane('fly',800,3)
# print(aeroplane.__str__())
# print(aeroplane.getNumber_of_engines())
# print('****************')
# aeroplane.setNumber_of_engines(80)
# print(aeroplane.getNumber_of_engines())
# aeroplane.setName('newname')
# aeroplane.setMax_speed(90000)
# print(aeroplane.getName())
# print(aeroplane.__str__())
# print('------ End Part C ------')


