from classs import Reustarant as R
class IceCreamStand (R):
    def __init__(self, name, type):
        super().__init__(name, type)
    def check_flavours(self):
        flavours=['sandwich','arahis','praline']
        n=0
        while self in flavours:
             n+1
             print(f" {self} Ready")
             break
IceCreamStand.check_flavours('sandwich')
IceCreamStand.check_flavours('praline')