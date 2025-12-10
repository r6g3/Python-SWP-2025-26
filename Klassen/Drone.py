from Air_Vehicle import Air_Vehicle

class Drone(Air_Vehicle):

    def __init__(self, weight, power, maxtakeOffWeight, uav, fpv):
        super().__init__(weight, power, maxtakeOffWeight)
        self.uav = uav
        self.fpv = fpv

    def __prep__(self):
        return super().__str__()