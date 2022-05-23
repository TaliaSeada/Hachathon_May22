import numpy as np
import pandas as pd

# read the data frame
import roomatesOrApartments

# TODO look for tenants
# TODO delete function

buildings = pd.read_csv(r'building_updated.csv')
buildings.drop("Unnamed: 0", inplace=True, axis=1)
print(buildings.columns)


# add row function
def addRow(gas=None, livingroom=None, bedrooms=None, bathrooms=None, city=None, where=None, lang=None, house=None,
           storage=None, furnished=None, AC=None, accesiable=None, elevator=None, parking=None, pets=None, smoking=None,
           price=None, length=None, publictranspo=None, nearconstruction=None, loud=None, phone=None, name=None):

    buildings.loc[len(buildings.index)] = [gas, livingroom, bedrooms, bathrooms, city, where, lang, house, storage,
                                           furnished, AC, accesiable, elevator, parking, pets, smoking, price, length,
                                           publictranspo, nearconstruction,loud, phone, name]



def score1(df, rows, name, score,cnt):
    """
    this is the first function to update the score for the match
    for the columns that are non ultimatum
    :param df: the data frame we work on
    :param rows: a specific row
    :param name: name of column
    :param score: to update
    :return: the updated score
    """
    if df[name] == None or rows[name] == None:
        score += 1
    elif df[name] ==0 and  rows[name] <=3:
        score += 1
    elif df[name] ==1 and rows[name] >= 3:
        score += 1
    else:
        cnt+=1
    return score, cnt


def score2(df, rows, name, score, flag):
    """
    this is the second function to update the score for the match
    for the columns that are ultimatum
    :param df: the data frame we work on
    :param rows: a specific row
    :param name: name of column
    :param flag: if totally not a match turn on, will nullify the result
    :param score: to update
    :return: the updated score and updated flag
    """
    if df[name] == None or rows[name] == None:
        score += 1
    elif df[name] == 0 and rows[name] <= 3:
         score += 1
    elif df[name] == 1 and rows[name] >= 3:
        score += 1
    else:
        flag = 1
    return score, flag


def score3(df, rows, name, score, cnt):
    """
    this is the third function to update the score for the match
    for the columns that are non ultimatum, but important
    :param df: the data frame we work on
    :param rows: a specific row
    :param name: name of column
    :param cnt: if not a match increase by one, to normalize the result
    :param score: to update
    :return: the updated score and updated flag
    """
    if df[name] == None or rows[name] == None:
        score += 1
    elif df[name]==rows[name]:
        score+=1
    else:
        cnt+=1
    return score, cnt


def score4(df, rows, name, score, cnt, bu, ba):
    if bu == 1:
        if df[name] == None or rows[name] == None:
            score += 1
        elif np.abs(df[name] - rows[name]) <= 500:
            score += 1
        elif np.abs(df[name] - rows[name]) <= 750:
            score += 0.5
        else:
            cnt += 1
        return score, cnt

    if ba == 1:
        if df[name] == None or rows[name] == None:
            score += 1
        elif np.abs(df[name] - rows[name]) == 0:
            score += 1
        elif np.abs(df[name] - rows[name]) == 0.5:
            score += 0.75
        elif np.abs(df[name] - rows[name]) == 1:
            score += 0.5
        return score


def sortByScore(score_list):
    """
    this function sort the result list and return the data frame
    :param score_list: list of scores and details
    :return: the result data frame
    """
    score_list.sort(key=lambda y: y[0])
    score_list.reverse()
    score_list = pd.DataFrame(score_list, columns=['score', 'name', 'phoneNumber'])
    score_list = score_list[score_list.score != 0]
    return score_list


def find_tenants(rowindex):

    score_list=[]
    apartment_row = buildings.iloc[rowindex]
    print(buildings.columns)
    for index, rows in roomatesOrApartments.data.iterrows():
        score = 0
        flag = 0
        cnt = 1

        names1 = ['gas/electric','livingroom','city', 'storage?','furnished?', 'AC' ,'Elevator','parking','bedrooms', 'near construction', 'loud neighborhood']
        for i in range(len(names1)):
            score, cnt = score1(apartment_row, rows, names1[i], score, cnt)

        names2=['accessible?', 'pets','smoke' ]
        for i in range(len(names2)):
            score, flag = score2(apartment_row, rows, names2[i], score, flag)


        names3=['city','where','rent length']
        for i in range(len(names3)):
            score, cnt = score3(apartment_row, rows, names3[i], score, cnt)

        names4=['bathrooms','price']
        score = score4(apartment_row, rows, names4[0], score, cnt, bu=None, ba=1)
        score, cnt = score4(apartment_row, rows, names4[1], score, cnt, bu=1, ba=None)

        if flag == 1:
            score = 0

        score /= cnt
        score_list.append((score, rows['name'], rows['phone number']))

    score_list = sortByScore(score_list)
    print(score_list)
