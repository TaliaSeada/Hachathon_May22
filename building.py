import numpy as np
import pandas as pd

# read the data frame
buildings = pd.read_csv(r'building_updated.csv')
buildings.drop("Unnamed: 0", inplace=True, axis=1)
# print(buildings.columns)


# add row function
def addRow(gas=None, livingroom=None, bedroom=None, bathroom=None, city=None, where=None, lang=None, house=None,
           storage=None, furnished=None, AC=None, accesiable=None, elevator=None, parking=None, pets=None, smoking=None,
           price=None, length=None, phone=None, name=None):

    buildings.loc[len(buildings.index)] = [gas, livingroom, bedroom, bathroom, city, where, lang, house, storage,
                                           furnished, AC, accesiable, elevator, parking, pets, smoking, price, length,
                                           phone, name]

# def find_tenants():
#