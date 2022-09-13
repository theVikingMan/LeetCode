
class ParkingSystem(object):
    
    def __init__(self, big, medium, small):
        self.parking = {1: big, 2: medium, 3: small}

    def addCar(self, carType):
        if self.parking[carType]: 
            self.parking[carType] -= 1
            return True
        else: return False


'''
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.p=[big,medium,small]

    def addCar(self, carType: int) -> bool:
        self.p[carType-1]-=1
        return self.p[carType-1]>=0
'''