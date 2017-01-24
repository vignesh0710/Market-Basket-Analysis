

import numpy as np
import pandas as pd

from itertools import combinations
import itertools

dframe_main_dataset3 = pd.read_csv('/Users/vigneshsureshbabu/Desktop/maybenew/data/nursery_data.txt',header = None,sep =',')

headers = ['parents','has_nurs','form','children','housing','finance','social','health','class_value']



temp_list = []
original_column_names = []
n = len(dframe_main_dataset3.columns)
for i in dframe_main_dataset3:
    temp_list = list(set(dframe_main_dataset3.ix[:,i]))
    original_column_names.append(temp_list)

#print(original_column_names[0])



#print(new_column_names)
#print(each[0]+each[1][n])

list = []
new_column_names = []
z = zip(headers,original_column_names)
for each in z:
    #print(each)
    #print(each[0]+each[1][1])
    for x in each[1]:
        z = each[0]+'_'+x
        list = z
        new_column_names.append(list)

##print(new_column_names)

rows = len(dframe_main_dataset3)
columns = len(new_column_names)

temp_new_data = np.zeros(shape=(rows,columns))
#print(temp_new_data)
#print(temp_new_data.shape)

my_frame_dataset3 = pd.DataFrame(temp_new_data,columns=new_column_names,dtype=int)
#print(new_data_frame)



n = len(dframe_main_dataset3)
for row_index in range(0,n):
    every_row = dframe_main_dataset3.ix[row_index]
    for column_index in range(0,len(dframe_main_dataset3.columns)):
        new_column = headers[column_index]+"_"+every_row[column_index]
        my_frame_dataset3[new_column][row_index] = 1

print(my_frame_dataset3)



my_frame_dataset3.to_csv("/Users/vigneshsureshbabu/Desktop/maybenew/data/nursery_dataset.csv", sep=',')

