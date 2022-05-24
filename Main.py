# we will need a class for the buildings and for the people looking for roommates and apartments
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import cluster
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split



import building
import roomatesOrApartments

if __name__ == '_main_':

    print(roomatesOrApartments.data.head())
    roomatesOrApartments.addRow( length=12, rooms=3, price=6000, gender=0, genderOfRoomMate=0, storage=3, balcony=3,
                                 AC=4, parking=2, Sk=4, publictraspo=4, furnished=5, pets=1, smoke=1, livingroom=4,
                                 accesiable=3, where="jerusalem", city=1, phonenumber="0500000000", name="abcd")

    print(roomatesOrApartments.data.head())

    # roomatesOrApartments.find_roommate(555)

    # building.addRow(gas=0, livingroom=0, bedrooms=2, bathrooms=1.5, city=1, where=None, lang=0, house=1,
    #                 storage=0, furnished=1, AC=1, accesiable=1, elevator=1, parking=1, pets=0, smoking=0,
    #                 price=3000, length=12, publictranspo=None, nearconstruction=None, loud=None,phone="0500000000", name="OWNER")