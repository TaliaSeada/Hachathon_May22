import numpy as np
import pandas as pd

# read the data frame
import roomatesOrApartments

# TODO look for tenants
# TODO delete function

buildings = pd.read_csv(r'building_updated.csv')
buildings.drop("Unnamed: 0", inplace=True, axis=1)


# add row function
def addRow(gas=None, livingroom=None, bedroom=None, bathroom=None, city=None, where=None, lang=None, house=None,
           storage=None, furnished=None, AC=None, accesiable=None, elevator=None, parking=None, pets=None, smoking=None,
           price=None, length=None, phone=None, name=None):

    buildings.loc[len(buildings.index)] = [gas, livingroom, bedroom, bathroom, city, where, lang, house, storage,
                                           furnished, AC, accesiable, elevator, parking, pets, smoking, price, length,
                                           phone, name]


def find_tenants(rowindex):
    apartment_row = buildings.iloc[rowindex]
    for index, rows in roomatesOrApartments.data.iterrow():
        print()

        #bool values
        # electric/gas
        # acsesiable
        #loud
        #construction
        #elevator
        #storage
        #livingroom
        #balcony/garden
        #smoke
        #pets
        #city
        #house/building
        #furnished
        #



