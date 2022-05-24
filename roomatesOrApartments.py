import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import cluster
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")



# TODO look for apartment
# TODO delete function

# read the data frame
data = pd.read_csv(r'data_updated.csv')
data.rename(columns = {'Unnamed: 0' : 'index'}, inplace=True)


u = data['where'].unique()
u_int = {}
for i in range(len(u)):
    u_int[u[i]] = i
w = []
for index, row in data.iterrows():
    row['where'] = u_int.get(row['where'])
    w.append(row['where'])
data['where'] = w
data = data.dropna(axis=0, how='any')
personal_info = data[['index', 'phone number', 'name']]
X =data.copy()
X.drop(['index', 'phone number', 'name'], inplace=True, axis=1)

kmeans_data = KMeans(n_clusters = 100, init = 'k-means++', random_state = 42)
y_kmeans_data = kmeans_data.fit_predict(X)

full_data = data.copy()
full_data['cluster']=y_kmeans_data



def addRow( length=12, rooms=3, price=6000,age=24, gender=0, genderOfRoomMate=0, storage=3,
           balcony=3, AC=3, parking=3, Sk=3, publictraspo=3,
           furnished=3, pets=3, smoke=3, livingroom=3,  accesiable=3,
           where=0,city=1, phonenumber=None, name=None):

    """
    this function adds a new row to the data frame (e.g a new looker)
    :param relevant information
    """

    data.loc[len(data.index)] = [len(data), length, rooms, price, age, gender, genderOfRoomMate, storage, balcony,
                                 AC, parking, Sk, publictraspo, furnished, pets, smoke, livingroom,
                                 accesiable, where,city, phonenumber, name]

def delrow(index):

    data.drop(index, axis=0, inplace=True)


def findmatch(index):

    row = data.iloc[index]
    row = pd.DataFrame([row])
    X=row.copy()
    X.drop(['index', 'phone number', 'name'], inplace=True, axis=1)
    match = full_data.loc[full_data["cluster"] == kmeans_data.predict(X)[0]]
    match_list=[]
    for index, rows in match.iterrows():
        match_list.append(score(row,rows))

    match_list.sort(key=lambda y: y[0])
    match_list.reverse()

    for x in match_list:
        print("feature match score: " ,x[0])
        print(x[1][0])
        print(x[1][1])
        print("the differences are: ")
        for y in range(2,len(x[1])):
            print(x[1][y])
        print()

def score(row1, row2):
    sc=0
    row2=pd.DataFrame([row2])
    f_name=[]
    for column in row1:
        if column in ['storage?', 'balcony/garden', 'AC', 'parking','SK', 'public transpo', 'furnished?', 'pets', 'smoke', 'livingroom', 'accessible?']:
            if np.abs(row1[column].values[0] - row2[column].values[0])<2:
                sc+=1
            if np.abs(row1[column].values[0] - row2[column].values[0])==1:
                f_name.append((column, row1[column].values[0], row2[column].values[0]))
        elif row1[column].values[0] == row2[column].values[0]:
                sc+=1
        elif column== 'age' :
            if np.abs(row1[column].values[0] - row2[column].values[0])<4:
                sc+=1
            if np.abs(row1[column].values[0] - row2[column].values[0])!=0:
                f_name.append((column, row1[column].values[0], row2[column].values[0]))
        else:
            if column not in ['index', 'name', 'phone number']:
                f_name.append((column, row1[column].values[0] ,row2[column].values[0]))
            else:
                if column!= 'index':
                    f_name.insert(0,(column, row2[column].values[0]))
    sc=sc*100/(len(row1.columns)-3)


    return sc, f_name

def main():


    addRow(length=6, rooms=4, price=8000, age=22, gender=1, genderOfRoomMate=1, storage=3, balcony=3,
           AC=4, parking=2, Sk=4, publictraspo=4, furnished=5, pets=1, smoke=1, livingroom=4,
           accesiable=3, where=0, city=3, phonenumber="0500000000", name="abcd")

    findmatch(len(data)-1)
    delrow(len(data)-1)






if __name__ == '__main__':
    main()



#
# def score1(df, rows, name, score):
#     """
#     this is the first function to update the score for the match
#     for the columns that are non ultimatum
#     :param df: the data frame we work on
#     :param rows: a specific row
#     :param name: name of column
#     :param score: to update
#     :return: the updated score
#     """
#     if df[name] == None or rows[name] == None:
#         score += 1
#     elif np.abs(df[name] - rows[name]) == 0:
#         score += 1
#     elif np.abs(df[name] - rows[name]) == 1:
#         score += 0.75
#     elif np.abs(df[name] - rows[name]) == 2:
#         score += 0.5
#     elif np.abs(df[name] - rows[name]) == 3:
#         score += 0.25
#     return score
#
#
# def score2(df, rows, name, flag, score):
#     """
#     this is the second function to update the score for the match
#     for the columns that are ultimatum
#     :param df: the data frame we work on
#     :param rows: a specific row
#     :param name: name of column
#     :param flag: if totally not a match turn on, will nullify the result
#     :param score: to update
#     :return: the updated score and updated flag
#     """
#     if df[name] == None or rows[name] == None:
#         score += 1
#     elif np.abs(df[name] - rows[name]) == 0:
#         score += 1
#     elif np.abs(df[name] - rows[name]) == 1:
#         score += 0.75
#     elif np.abs(df[name] - rows[name]) == 2:
#         score += 0.5
#     elif np.abs(df[name] - rows[name]) == 3:
#         score += 0.25
#     else:
#         flag = 1
#     return flag, score
#
#
# def score3(df, rows, name, cnt, score):
#     """
#     this is the third function to update the score for the match
#     for the columns that are non ultimatum, but important
#     :param df: the data frame we work on
#     :param rows: a specific row
#     :param name: name of column
#     :param cnt: if not a match increase by one, to normalize the result
#     :param score: to update
#     :return: the updated score and updated flag
#     """
#     if df[name] == None or rows[name] == None:
#         score += 1
#     elif np.abs(df[name] - rows[name]) == 0:
#         score += 1
#     elif np.abs(df[name] - rows[name]) == 1:
#         score += 0.75
#     elif np.abs(df[name] - rows[name]) == 2:
#         score += 0.5
#     elif np.abs(df[name] - rows[name]) == 3:
#         score += 0.25
#     else:
#         cnt += 1
#     return cnt, score
#
#
# def score4(df, rows, name, score, flag, cnt, bu, ba, wh):
#     if bu == 1:
#         if df[name] == None or rows[name] == None:
#             score += 1
#         elif np.abs(df[name] - rows[name]) <= 500:
#             score += 1
#         elif np.abs(df[name] - rows[name]) <= 750:
#             score += 0.5
#         else:
#             cnt += 1
#         return score, cnt
#
#     if ba == 1:
#         if df[name] == None or rows[name] == None:
#             score += 1
#         elif np.abs(df[name] - rows[name]) == 0:
#             score += 1
#         elif np.abs(df[name] - rows[name]) == 0.5:
#             score += 0.75
#         elif np.abs(df[name] - rows[name]) == 1:
#             score += 0.5
#         return score
#
#     if wh == 1:
#         if df[name] == None or rows[name] == None:
#             score += 1
#         elif df[name] == rows[name]:
#             score += 1
#         else:
#             flag = 1
#         return score, flag
#
#
# def sortByScore(score_list):
#     """
#     this function sort the result list and return the data frame
#     :param score_list: list of scores and details
#     :return: the result data frame
#     """
#     score_list.sort(key=lambda y: y[0])
#     score_list.reverse()
#     score_list = pd.DataFrame(score_list, columns=['score', 'name', 'phoneNumber'])
#     score_list = score_list[score_list.score > 50.0]
#     return score_list
#
#
# def find_roommate(rowindex):
#     """
#     this function is the main function to implement the algorithm
#     it uses three different methods:
#     1. score1 - the regular calculation, non ultimatum features
#     2. score2 - ultimatum features
#     3. score3 - non ultimatum features but have more weight
#     :param rowindex: the information of a person looking for a roommate
#     :return: a sorted list of pairs of the score and the relevant information
#     """
#     lookerRow = data.iloc[rowindex]
#     score_list = []
#
#     for indexs, rows in data.iterrows():
#         score = 0
#         flag = 0
#         cnt = 1
#         # reg
#         names1 = ['gas/electric', 'master', 'storage?', 'balcony/garden', 'electric/solar', 'parking', 'public transpo',
#                   'loud neighborhood', 'construction to building', 'furnished?', 'livingroom', 'bedrooms']
#         for i in range(len(names1)):
#             score = score1(lookerRow, rows, names1[i], score)
#
#         # flag
#         names2 = ['pets', 'smoke', 'accessible?']
#         for i in range(len(names2)):
#             flag, score = score2(lookerRow, rows, names2[i], flag, score)
#
#         # count
#         names3 = ['SK', 'AC']
#         for i in range(len(names3)):
#             cnt, score = score3(lookerRow, rows, names3[i], cnt, score)
#
#         names4 = ['price', 'bathrooms', 'where', 'city']
#         score, cnt = score4(lookerRow, rows, names4[0], score, flag, cnt, bu=1, ba=None, wh=None)
#         score = score4(lookerRow, rows, names4[1], score, flag, cnt, bu=None, ba=1, wh=None)
#         score, flag = score4(lookerRow, rows, names4[2], score, flag, cnt, bu=None, ba=None, wh=1)
#         score, flag = score4(lookerRow, rows, names4[3], score, flag, cnt, bu=None, ba=None, wh=1)
#
#
#         if flag == 1:
#             score = 0
#
#         score /= cnt
#         score=(score/21)*100
#         score_list.append((score, rows['name'], rows['phone number']))
#
#     score_list = sortByScore(score_list)
#     score_list = score_list[(score_list.phoneNumber != lookerRow['phone number'])]
#     print(score_list)