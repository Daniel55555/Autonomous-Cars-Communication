import math

class GetInfoAboutCars():
    def __init__(self, manufacturer = "Unknown", model = "Unknown", id = "Unknown", x2 = 1000, y2 = 1000):
        self.manufacturer = manufacturer
        self.model        = model
        self.id           = id
        self.x2           = x2
        self.y2           = y2



class MyCar():
    def __init__(self, manufacturer = "VW", model = "ID3", id = "123456789123", x1 = 0, y1 = 0):
        self.manufacturer = manufacturer
        self.model        = model
        self.id           = id
        self.x1           = x1
        self.y1           = y1

    def sendInfoAboutCar(self):
        return self.manufacturer, self.model, self.id

    def setSpeed(self, speed):
        return (str(speed) + "km/h")

    def getDistance(self, x1, y1, x2, y2):
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return distance
        
    def closestCar(self, my_position, found_coordinates):
        min = 0
        for i in range (1, len(found_coordinates)):
            previousMinDistance = math.sqrt((my_position[0] - found_coordinates[min][0])** 2 + (my_position[1] - found_coordinates[min][1])** 2)
            currentDistance  = math.sqrt((my_position[0] - found_coordinates[i][0])** 2 + (my_position[1] - found_coordinates[i][1])** 2)
        if currentDistance < previousMinDistance:
            min = i
        return found_coordinates[min]

myCar = MyCar()
car1 = GetInfoAboutCars("Audi", "A4", "15", 15, 20)
car2 = GetInfoAboutCars("Nissan", "Navara", "500",5, 5)
car3 = GetInfoAboutCars("VW", "Passat", "00000", 3, 1)

closest = myCar.closestCar((myCar.x1, myCar.y1), [(car1.x2, car1.y2), (car2.x2, car2.y2), (car3.x2, car3.y2)])

print(closest)
print(myCar.setSpeed(150))
print(myCar.sendInfoAboutCar())



