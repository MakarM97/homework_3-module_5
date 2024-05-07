class Buiding:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)
        # print(type(self.numberOfFloors))
        # print(type(self.buildingType))

    def __eq__(self, other):
        return self.numberOfFloors == other.buildingType


my_building1 = Buiding(2, 'str')
my_building2 = Buiding(4, 'string')
print(my_building1)
print(my_building2)
if my_building1 == my_building2:# В коде ошибки нет но почему, если мы сравниваем инт и стр? Или я вообще неверно код написал?
    print('Ок')# Не пойму почему этот принт не выводит???




