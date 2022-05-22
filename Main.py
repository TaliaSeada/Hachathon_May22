# we will need a class for the buildings and for the people looking for roommates and apartments

import building
import roomatesOrApartments

if __name__ == '__main__':
    # print(building.buildings.tail())
    #
    # building.addRow(gas=0, livingroom=0, bedroom=2, bathroom=1.5, city=1, where=None, lang=0, house=1,
    #                 storage=0, furnished=1, AC=1, accesiable=1, elevator=1, parking=1, pets=0, smoking=0,
    #                 price=3000, length=12, phone="0500000000", name="OWNER")
    #
    # print(building.buildings.tail())

    # print(roomatesOrApartments.data.tail())
    # roomatesOrApartments.addRow(gas=None, length=None, rooms=None, budget=None, Bathroom=None, master=None,
    #                             storage=None,
    #                             balcony=None, electric=None, AC=None, parking=None, Sk=None, publictraspo=None,
    #                             loud=None, construction=None,
    #                             furnished=None, pets=None, smoke=None, livingroom=None, floor=None, floornum=None,
    #                             accesiable=None, where=None,
    #                             phonenumber=None, name=None)
    #
    # print(roomatesOrApartments.data.tail())

    print(roomatesOrApartments.data.head())

    roomatesOrApartments.find_roommate(1)



