from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatMaterail = []

    def __init__(self, license, driver, typeCarAccepted, seatMaterail):
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatMaterail = seatMaterail