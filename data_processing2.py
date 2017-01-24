import numpy as np
import pandas as pd


dframe_main_dataset2 = pd.read_csv('/Users/vigneshsureshbabu/Desktop/maybenew/data/mushroom.txt',header = None,sep =',')

headers = ['capshape','capsurface','capcolor','bruises','odor','gillattachment','gillspacing','gillsize','gillcolor','stalkshape','stalkroot','stalksurfaceabovering','stalksurfacebelowring','stalkcolorabovering','stalkcolorbelowring','veiltype','veilcolor','ringnumber','ringtype','sporeprintcolor','population','habitat','class_value']


#code for data processing
temp_list = []
original_column_names = []
n = len(dframe_main_dataset2.columns)
for i in dframe_main_dataset2:
    temp_list = list(set(dframe_main_dataset2.ix[:,i]))
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

rows = len(dframe_main_dataset2)
columns = len(new_column_names)

temp_new_data = np.zeros(shape=(rows,columns))
#print(temp_new_data)
#print(temp_new_data.shape)

my_frame_dataset2 = pd.DataFrame(temp_new_data,columns=new_column_names,dtype=int)
#print(new_data_frame)



n = len(dframe_main_dataset2)
for row_index in range(0,n):
    every_row = dframe_main_dataset2.ix[row_index]
    for column_index in range(0,len(dframe_main_dataset2.columns)):
        new_column = headers[column_index]+"_"+every_row[column_index]
        my_frame_dataset2[new_column][row_index] = 1

print(my_frame_dataset2)


#this path should be the same in dataset2.py
my_frame_dataset2.to_csv("/Users/vigneshsureshbabu/Desktop/maybenew/data/mushroom_dataset.csv", sep=',')

