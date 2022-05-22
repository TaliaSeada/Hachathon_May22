import numpy as np
import pandas as pd

# read the data frame
data = pd.read_csv(r'data_updated.csv')
data.drop("Unnamed: 0", inplace=True, axis=1)
print(data.columns)


def addRow(gas=None, length=None, rooms=None, budget=None, Bathroom=None, master=None, storage=None,
           balcony=None, electric=None, AC=None, parking=None, Sk=None, publictraspo=None, loud=None, construction=None,
           furnished=None, pets=None, smoke=None, livingroom=None, floor=None, floornum=None, accesiable=None,
           where=None,
           phonenumber=None, name=None):
    data.loc[len(data.index)] = [gas, length, rooms, budget, Bathroom, master, storage, balcony, electric,
                                 AC, parking, Sk, publictraspo, loud, construction, furnished, pets, smoke, livingroom,
                                 floor,
                                 floornum, accesiable, where, phonenumber, name]


def find_roommate(lookerrow):
    for indexs, rows in data.iterrows():
        score = 0
        flag = 1
        # gas
        if np.abs(lookerrow['gas/electric'] - rows['gas/electric']) == 0:
            score += 1
        elif np.abs(lookerrow['gas/electric'] - rows['gas/electric']) == 1:
            score += 0.75
        elif np.abs(lookerrow['gas/electric'] - rows['gas/electric']) == 2:
            score += 0.5
        elif np.abs(lookerrow['gas/electric'] - rows['gas/electric']) == 3:
            score += 0.25

        #master
        if np.abs(lookerrow['master'] - rows['master']) == 0:
            score += 1
        elif np.abs(lookerrow['master'] - rows['master']) == 1:
            score += 0.75
        elif np.abs(lookerrow['master'] - rows['master']) == 2:
            score += 0.5
        elif np.abs(lookerrow['master'] - rows['master']) == 3:
            score += 0.25

        #storage
        if np.abs(lookerrow['storage'] - rows['storage']) == 0:
            score += 1
        elif np.abs(lookerrow['storage'] - rows['storage']) == 1:
            score += 0.75
        elif np.abs(lookerrow['storage'] - rows['storage']) == 2:
            score += 0.5
        elif np.abs(lookerrow['storage'] - rows['storage']) == 3:
            score += 0.25

        #balcony/garden
        if np.abs(lookerrow['balcony/garden'] - rows['balcony/garden']) == 0:
            score += 1
        elif np.abs(lookerrow['balcony/garden'] - rows['balcony/garden']) == 1:
            score += 0.75
        elif np.abs(lookerrow['balcony/garden'] - rows['balcony/garden']) == 2:
            score += 0.5
        elif np.abs(lookerrow['balcony/garden'] - rows['balcony/garden']) == 3:
            score += 0.25


        #accesible
        if np.abs(lookerrow['accesiable'] - rows['accesiable']) == 0:
            score += 1
        elif np.abs(lookerrow['accesiable'] - rows['accesiable']) == 1:
            score += 0.75
        elif np.abs(lookerrow['accesiable'] - rows['accesiable']) == 2:
            score += 0.5
        elif np.abs(lookerrow['accesiable'] - rows['accesiable']) == 3:
            score += 0.25

        #electric/solar
        if np.abs(lookerrow['accesiable'] - rows['accesiable']) == 0:
            score += 1
        elif np.abs(lookerrow['accesiable'] - rows['accesiable']) == 1:
            score += 0.75
        elif np.abs(lookerrow['accesiable'] - rows['accesiable']) == 2:
            score += 0.5
        elif np.abs(lookerrow['accesiable'] - rows['accesiable']) == 3:
            score += 0.25