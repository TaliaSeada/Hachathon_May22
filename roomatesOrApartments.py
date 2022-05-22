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
    """
    this function adds a new row to the data frame (e.g a new looker)
    :param relevant information
    """
    data.loc[len(data.index)] = [gas, length, rooms, budget, Bathroom, master, storage, balcony, electric,
                                 AC, parking, Sk, publictraspo, loud, construction, furnished, pets, smoke, livingroom,
                                 floor,
                                 floornum, accesiable, where, phonenumber, name]


def score1(df, rows, name, score):
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
    elif np.abs(df[name] - rows[name]) == 0:
        score += 1
    elif np.abs(df[name] - rows[name]) == 1:
        score += 0.75
    elif np.abs(df[name] - rows[name]) == 2:
        score += 0.5
    elif np.abs(df[name] - rows[name]) == 3:
        score += 0.25
    return score


def score2(df, rows, name, flag, score):
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
    elif np.abs(df[name] - rows[name]) == 0:
        score += 1
    elif np.abs(df[name] - rows[name]) == 1:
        score += 0.75
    elif np.abs(df[name] - rows[name]) == 2:
        score += 0.5
    elif np.abs(df[name] - rows[name]) == 3:
        score += 0.25
    else:
        flag = 1
    return flag, score


def score3(df, rows, name, cnt, score):
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
    elif np.abs(df[name] - rows[name]) == 0:
        score += 1
    elif np.abs(df[name] - rows[name]) == 1:
        score += 0.75
    elif np.abs(df[name] - rows[name]) == 2:
        score += 0.5
    elif np.abs(df[name] - rows[name]) == 3:
        score += 0.25
    else:
        cnt += 1
    return cnt, score


def find_roommate(lookerRow):
    """
    this function is the main function to implement the algorithm
    it uses three different methods:
    1. score1 - the regular calculation, non ultimatum features
    2. score2 - ultimatum features
    3. score3 - non ultimatum features but have more weight
    :param lookerRow: the information of a person looking for a roommate
    :return: a sorted list of pairs of the score and the relevant information
    """
    score_list = []
    for indexs, rows in data.iterrows():
        score = 0
        flag = 0
        cnt = 1
        # reg
        names1 = ['gas/electric', 'master', 'storage', 'balcony/garden', 'electric/solar', 'parking', 'public transpo', 'loud neighborhood',
                  'construction to building', 'furnished', 'livingroom' ]

        for i in range(len(names1)):
            score = score1(lookerRow, rows, names1[i], score)

        # flag
        names2 = ['pets', 'smoke', 'accesiable']

        for i in range(len(names2)):
            score = score2(lookerRow, rows, names2[i], flag, score)
        # count
        names3 = ['SK', 'AC']
        for i in range(len(names3)):
            score = score3(lookerRow, rows, names3[i], cnt, score)

        if flag == 1:
            score = 0

        score /= cnt
        score_list.append((score, rows['name'], rows['phone number']))
