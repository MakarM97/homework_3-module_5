class Buiding:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __str__(self):
        return str(self.buildingType)

    def __int__(self):
        return int(self.numberOfFloors)

    def __eq__(self, other):
        return self.numberOfFloors == other.buildingType


numberOfFloors = Buiding(10, 'str')
buildingType = Buiding(10, 'str')
res = numberOfFloors == buildingType
print(res)
if Buiding.__eq__(self=numberOfFloors, other=buildingType):
    pass
