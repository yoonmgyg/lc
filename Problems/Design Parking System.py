# Designs parking system by adding slots for sizes of cars and subtracting according to added car type
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.vehicle = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if carType == 1 :
            if self.vehicle[0] > 0:
                self.vehicle[0] -= 1
                return True
        elif carType == 2:
            if self.vehicle[1] > 0:
                self.vehicle[1] -= 1
                return True
        elif carType == 3:
            if self.vehicle[2] > 0:
                self.vehicle[2] -= 1
                return True
        return False
