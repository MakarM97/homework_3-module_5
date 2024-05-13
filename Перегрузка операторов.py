class Buiding:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors and
                self.buildingType == other.buildingType)


numberOfFloors = Buiding(10, '10')
buildingType = Buiding(10, '10')
res = numberOfFloors == buildingType
print(res)
