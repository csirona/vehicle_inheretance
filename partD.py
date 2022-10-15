import vehicle 

def increaseSpeed(vehicle):
    if str(type(vehicle)) == "<class 'vehicle.Car'>":
        vehicle.setMax_speed(int(vehicle.getMax_speed())+50)
        print('Increased speed of car is '+str(vehicle.getMax_speed()))
    elif str(type(vehicle)) == "<class 'vehicle.Aeroplane'>":
        vehicle.setMax_speed(int(vehicle.getMax_speed())+ 100)
        print('Increased speed of aeroplane is '+str(vehicle.getMax_speed()))
    else:
        print('Invalid Vehicle')

def partD():
    # Ask car name and speed
    carName = input("What is your car name?")
    carSpeed = input("What is its max speed?")
    numCylinders = input("What is its number of  cyliners?")
    # Ask aeroplane and speed
    aeroName = input("What is your aeroplane name?")
    aeroSpeed = input("What is its max speed?")
    numEngines = input("What is its number of engines?")
    #Instances for car and aeroplane
    myCar = vehicle.Car(carName,carSpeed,numCylinders)
    myAeroplane = vehicle.Aeroplane(aeroName, aeroSpeed, numEngines)

    print(myCar.getName()+' ' + myCar.getMax_speed() +' '+myCar.getNumber_of_cylinders()+' '+myAeroplane.getName() + ' ' +myAeroplane.getMax_speed() +' '+myAeroplane.getNumber_of_engines())

    # Encrease speed
    increaseSpeed(myCar)
    increaseSpeed(myAeroplane)
    # Know which is faster with if conditional
    print('The faster is ')
    if int(myCar.getMax_speed()) >int(myAeroplane.getMax_speed()):
        print(myCar.getName())
        return myCar
    elif int(myCar.getMax_speed()) == int(myAeroplane.getMax_speed()):
        print('Both have same speed')
        return None
    else:
        print(myAeroplane.getName())
        return myAeroplane
    
partD()