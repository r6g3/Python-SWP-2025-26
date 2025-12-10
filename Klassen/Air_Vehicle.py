from Vehicle import Vehicle

class Air_Vehicle(Vehicle):
    def __init__(self, weight, power, maxtakeOffWeight):
        super().__init__(weight, power)
        self.maxtakeOffWeight = maxtakeOffWeight
