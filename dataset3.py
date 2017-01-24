
#importing necessary packages
import pandas as pd
from itertools import combinations


#reading the input file
dframe_main = pd.read_table('/Users/vigneshsureshbabu/Desktop/maybenew/data/nursery_dataset.csv',sep =',')
dframe = pd.read_table('/Users/vigneshsureshbabu/Desktop/maybenew/data/nursery_dataset.csv',sep =',')

del dframe_main[dframe_main.columns[0]]
##print(dframe_main)
del dframe[dframe.columns[0]]
##print(dframe)

#getting the number of rows and columns of the input data frame.
rows,columns = dframe_main.shape


#fetching user input for minimum support count
print("Enter the minimum Support Count here:")
min_support_count = int(input())


#part of code for calculating f(k-1) * f(k-1)

master_column_list = []



#code for calculating k =1 frequent item sets
def candidate_1(dframe):
    result = []
    pp = []
    not_pp = []

    for cols in combinations(dframe,1):
        #print(cols)

        s = dframe[list(cols)].all(axis=1).sum()
        #print(s)
        #print(list(cols),s)
        if s >= min_support_count:
            pp.append([",".join(cols), s])

        if s < min_support_count:
            not_pp.append([",".join(cols), s])

    sdf = pd.DataFrame(pp, columns=["Pattern", "Support"])
    not_sdf = pd.DataFrame(not_pp, columns=["Pattern", "Support"])
    result.append(sdf)
    result.append(not_sdf)
    return result

df_list_candidate1 = candidate_1(dframe)
df_1st_candidate1 = df_list_candidate1[0]
df_2st_candidate1 = df_list_candidate1[1]

master_column_list.append(list(df_1st_candidate1.Pattern))

print(len(df_1st_candidate1),"is the number of frequent itemsets for k = 1")
print(len(df_2st_candidate1),"is the number of not frequent itemsets for k = 1")

k1_freq = len(df_1st_candidate1)
k1_not_freq = len(df_2st_candidate1)

to_be_deleted = df_2st_candidate1.Pattern[df_2st_candidate1.Support < min_support_count]

for each in to_be_deleted:
    del dframe[each]

list_candidate1 = []
for each in df_1st_candidate1.Pattern:
    list_candidate1.append(each)


#code for calculating k = 2 frequent item sets
def candidate_2(dframe):
    pp = []
    only_column_names = []
    not_pp = []
    result = []
    for cols in combinations(dframe,2):

        s = dframe[list(cols)].all(axis=1).sum()
        if s >= min_support_count:
            pp.append([",".join(cols), s])
            only_column_names.append(cols)
            #print(pp)

            #print(sdf)
        if s < min_support_count:
            not_pp.append([",".join(cols), s])


    sdf = pd.DataFrame(pp, columns=["Pattern", "Support"])
    not_sdf = pd.DataFrame(not_pp, columns=["Pattern", "Support"])
    result.append(sdf)
    result.append(not_sdf)
    result.append(only_column_names)
    return result

df_list_candidate2 = candidate_2(dframe)
#print(df_list_candidate2[2])

df_1st_candidate2 = df_list_candidate2[0]
df_2st_candidate2 = df_list_candidate2[1]
df_only_column_names2 = df_list_candidate2[2]

#print(df_1st_candidate2)

print(len(df_1st_candidate2),"is the number of frequent itemsets for k = 2")
print(len(df_2st_candidate2),"is the number of not frequent itemsets for k = 2")

master_column_list.append(list(df_only_column_names2))

k2_freq = len(df_1st_candidate2)
k2_not_freq = len(df_2st_candidate2)


####bigdata
bigdata1 = pd.concat([df_1st_candidate1,df_1st_candidate2],axis = 0,ignore_index=True)
##print(bigdata1)

not_bigdata1 = pd.concat([df_2st_candidate1,df_2st_candidate2],axis = 0,ignore_index=True)

#code for calculating k =3 frequent item sets:

lk =[]
temp_list_candidate2 = []

for each_element_in_candidate2 in df_only_column_names2:
    for each_element_in_candidate1 in list_candidate1:
        if each_element_in_candidate1 not in each_element_in_candidate2:
            lk = list(each_element_in_candidate2)
            lk.append(each_element_in_candidate1)
            lk.sort()
            temp_list_candidate2.append(lk)

b_set = set(tuple(x) for x in temp_list_candidate2)
all_elements = [ list(x) for x in b_set]

temp_list3 = []
not_temp_list3 = []
only_column_names3 = []
for each in all_elements:
    s = dframe[list(each)].all(axis=1).sum()
    if s >= min_support_count:
        temp_list3.append([",".join(each), s])
        only_column_names3.append(each)
    if s < min_support_count:
            not_temp_list3.append([",".join(each), s])
df_1st_candidate3 = pd.DataFrame(temp_list3,columns=["Pattern", "Support"])
df_2st_candidate3 = pd.DataFrame(not_temp_list3,columns=["Pattern", "Support"])
master_column_list.append(list(only_column_names3))

print(len(df_1st_candidate3),"is the number of frequent itemsets for k = 3")
print(len(df_2st_candidate3),"is the number of not frequent itemsets for k = 3")
k3_freq = len(df_1st_candidate3)
k3_not_freq = len(df_1st_candidate3)
bigdata2 = pd.concat([bigdata1,df_1st_candidate3],axis = 0,ignore_index=True)
not_bigdata2 = pd.concat([not_bigdata1,df_2st_candidate3],axis = 0,ignore_index=True)


#code for calculating k > 3 frequent item sets:

test_list = []
candidates_generated_with_support =[]

candidates_generated_not_frequent = []


if len(only_column_names3) > 0:
    k = 3

    n = len(master_column_list)
    #print (master_column_list)
    while (len(master_column_list[n-1]) != 0):

        k = k+1
        main_test_list = []
        for each_element_of_candidates_k in master_column_list[k-2]:
            #print (each_element_of_candidates_k)
            for each_element_of_candidate1 in list_candidate1:
                if each_element_of_candidate1 not in each_element_of_candidates_k:
                    test_list = list(each_element_of_candidates_k)
                    test_list.append(each_element_of_candidate1)
                    test_list.sort()
                    main_test_list.append(test_list)
        k_set = set(tuple(x) for x in main_test_list)
        list_of_elements_of_k = [ list(x) for x in k_set]
        #print(list_of_elements_of_k)
        column_names_of_candidates_generated = []
        for i in list_of_elements_of_k:
            s = dframe[list(i)].all(axis=1).sum()
            if s >= min_support_count:
                candidates_generated_with_support.append([",".join(i), s])
                column_names_of_candidates_generated.append(i)
            else:
                candidates_generated_not_frequent.append([",".join(i), s])
        master_column_list.append(list(column_names_of_candidates_generated))
        n = len(master_column_list)
df_1st_candidatek = pd.DataFrame(candidates_generated_with_support,columns=["Pattern", "Support"])
print(len(candidates_generated_with_support),"is the number of frequent itemsets for k > 3")
df_2st_candidatek = pd.DataFrame(candidates_generated_not_frequent,columns=["Pattern", "Support"])
k_freq = len(candidates_generated_with_support)
k_not_freq = len(df_2st_candidatek)
k4_freq = k3_freq
frequent_item_sets = k1_freq + k2_freq + k3_freq + k_freq

print(frequent_item_sets,"is the total number of frequent itemsets for F1 * F(k-1)")
total_candidates = k1_freq+k1_not_freq+k2_freq+k2_not_freq+k3_freq+k3_not_freq+k_freq+k_not_freq
print(total_candidates,"is the total number of candidates generated using the F1 * F(k-1) method")

##############################################################################

#part of code for calculating f(k-1) * f(k-1)

print("It is the beginning of output for F(k-1) * F(k-1)")

temp_list_candidate_n = []
master_column_list_3aprtb = []
m = len(master_column_list)
for j in range(1,m):
    new_list =[]
    for item_set in master_column_list[j]:
        n = len(item_set)
        #print(n)
        #print(each_element,n)
        #print(each_element[n-1])
        flag =  True
        for every_element in master_column_list[j]:
            if len(every_element) == len(item_set):
                if item_set[n-1] != every_element[n-1]:
                    for i in range(0,n-1):
                        if item_set[i] != every_element[i]:
                            flag = False
                            #print(flag)
                    if flag == True:
                        a = len(every_element)
                        new_list = list(item_set)
                        new_list.append(every_element[a-1])
                        new_list.sort()
                        #print(len(new_list))
                        temp_list_candidate_n.append(new_list)
n_set = set(tuple(x) for x in temp_list_candidate_n)
all_elements_3a_part2 = [ list(x) for x in n_set]
temp_list3a_partb = []
not_temp_list3a_partb = []
candidates = int((total_candidates)/3)
only_column_names3apartb = []

for each in all_elements_3a_part2:
    #print(each)
    s = dframe[list(each)].all(axis=1).sum()
    #print(s)
    if s >= min_support_count:
        temp_list3a_partb.append([",".join(each), s])
        only_column_names3apartb.append(each)
    if s < min_support_count:
            not_temp_list3a_partb.append([",".join(each), s])

df_1st_candidate3apartb = pd.DataFrame(temp_list3a_partb,columns=["Pattern", "Support"])
df_2st_candidate3aprtb = pd.DataFrame(not_temp_list3a_partb,columns=["Pattern", "Support"])
master_column_list_3aprtb.append(list(only_column_names3apartb))

print(frequent_item_sets,"is the total number of frequent itemsets generated using F(k-1) * F(k-1) method")
print(candidates,"is the total number of candidates for f(k-1) * f(k-1)")

###############################################################################################################

print("calculating the count of maximal and closed frequent item set")


master_big_data = pd.concat([bigdata2,df_1st_candidatek],axis = 0,ignore_index=True)
frequent_item_sets_list = master_big_data.Pattern.str.split(',').tolist()
not_master_big_data = pd.concat([not_bigdata2,df_2st_candidatek],axis = 0,ignore_index=True)
not_frequent_itemset = not_master_big_data.Pattern.str.split(',').tolist()
x = list(master_big_data.set_index('Pattern').to_dict().values()).pop()
dictlist = []
for key, value in x.items():
    temp = [key,value]
    dictlist.append(temp)

master =[]
for i in dictlist:
    item = []
    if "," in i[0]:

        first = i[0].split(',')
        item.append(first)
        item.append(i[1])
    else:
        temp2 = []
        temp2.append(i[0])
        item.append(temp2)
        item.append(i[1])
    master.append(item)

master_length = []
for each in master:
    master_length.append(each[0])

maxlength = max(len(s) for s in master_length)
closed_freq_set_list = []
for length in range(1,maxlength+1):
    for k in master:
        temp_list = []
        flag = True

        if len(k[0]) == length:
            for l1 in master:
                if len(l1[0]) == length + 1:
                    y = l1[0]
                    if k[0][0] in l1[0]:
                        if k[1] == l1[1]:
                            flag = False
                            break
            if flag == True:
                temp_list = k[0]
                closed_freq_set_list.append(temp_list)

print(len(closed_freq_set_list),"is the number of closed frequent itemsets ")

maximal_freq_set_list = []

for length in range(1,maxlength+1):
    for k in master:
        temp_list = []
        flag = True

        if len(k[0]) == length:
            for l1 in master:
                if len(l1[0]) == length + 1:
                    y = l1[0]
                    if k[0][0] in l1[0]:
                        if l1[0] in frequent_item_sets_list:
                            flag = False
                            break
            if flag == True:
                temp_list = k[0]
                maximal_freq_set_list.append(temp_list)

print(len(maximal_freq_set_list),"is the number of maximal frequent itemsets ")



##########################################################################################################
#rule generation for part (e)
#brute force method of rule generation.

print("Enter the minimum confidence level:")
min_confidence_level = int(input())
master_rules_list = []
min_confidence_level2 = min_confidence_level + 30
master_pruned_list = []


computation_counter = 0
for each in master:
    if len(each[0]) >= 2:
        for r_value in range(1,len(each[0])):
            for subsets in combinations(each[0],r_value):
                list_subset = []
                list_parent = []
                main_list = []


                if len(list(subsets)) == 1:
                    for key,value in x.items():


                        if list(subsets)[0] == key:
                            computation_counter = computation_counter+ 1
                            confidence = (each[1]/value)*100
                            if confidence > min_confidence_level:
                                z = list(each[0])


                                for subset_length_1 in subsets:
                                    c = subset_length_1
                                    if subset_length_1 in z:
                                        z.remove(subset_length_1)
                                        list_subset = list(subsets)
                                        list_parent = z
                                        main_list.append(list_subset)
                                        main_list.append(list_parent)
                                        main_list.append(confidence)
                                        master_rules_list.append(main_list)
                            break
                else:
                    flag = True
                    temp_subset = list(subsets)
                    merged_subset = ','.join(temp_subset)
                    for key,value in x.items():


                        if merged_subset == key:
                            computation_counter = computation_counter + 1
                            confidence = (each[1]/value)*100
                            if confidence > min_confidence_level:
                                split = list(each[0])
                                for every_element in subsets:
                                    c = every_element
                                    if every_element in split:
                                        split.remove(every_element)
                                        flag = True
                                if flag == True:
                                    list_subset = list(subsets)
                                    list_parent = split
                                    main_list.append(list_subset)
                                    main_list.append(list_parent)
                                    main_list.append(confidence)
                                    master_rules_list.append(main_list)
                                    if confidence > min_confidence_level2:
                                        master_pruned_list.append(master_rules_list)


def rules_confidence_pruning(each_itemset, list_of_rules_generated, x,min_confidence_level):
    association_rules_dict = {}
    rules_less_than_confidence = []
    confidence_pruning_operations_count = 0
    rule_generator_count = 0


    if len(each_itemset) != 1:
        itemset = list(each_itemset)

        child_item_sets = []
        if len(itemset) == 1:
            child_item_sets.append(itemset[0])
            return child_item_sets
        else:
            individual_combinations = combinations(itemset, len(itemset) - 1)
            for i in individual_combinations:
                func_variable = list(i)
                if not func_variable or len(func_variable) == len(itemset):
                    continue
                else:
                    child_item_sets.append(func_variable)
        for item in child_item_sets:
            copy_of_main_list = list(list_of_rules_generated)

            rules_generator = []
            for each_item in item:
                #print(each_item,"eachitem")
                if each_item in copy_of_main_list:
                    copy_of_main_list.remove(each_item)
            rules_generator.append(tuple(item))
            copy_of_main_list.sort()
            rules_generator.append(tuple(copy_of_main_list))
            if (rules_generator not in list(association_rules_dict.keys())) and (rules_generator not in rules_less_than_confidence):
                confidence_pruning_operations_count = confidence_pruning_operations_count + 1
                if len(item) == 1:
                    m2 = ''.join(item)
                else:
                    temp_variable = list(item)
                    m2 =  ','.join(temp_variable)
                    #print(temp2,"temp2")

                temp_subset_1 = list(each_itemset)
                merged_subset_1 = ','.join(temp_subset_1)
                found = False
                val_k = 0
                val_n = 0
                for key_k, values_k in x.items():
                    if found:
                        break
                    else:

                        if key_k == merged_subset_1:
                            for key_n,values_n in x.items():
                                if key_n == m2:
                                    found = True
                                    val_k = values_k
                                    val_n = values_n
                                    break

                if val_k == 0 or val_n == 0:
                    continue
                else:
                    confidence_level_pruning = float(val_k / val_n) * 100
                    if confidence_level_pruning < 60:
                        rules_less_than_confidence.append(rules_generator)
                    else:
                        association_rules_dict[tuple(rules_generator)] = confidence_level_pruning
                        rule_generator_count = rule_generator_count + 1
                        rules_confidence_pruning(tuple(item), list_of_rules_generated, x, min_confidence_level)
        #print ("func...", confidence_pruning_operations_count)
        output = [confidence_pruning_operations_count, association_rules_dict, rules_less_than_confidence, rule_generator_count]
        #print(output)
        return (output)
#print(master_rules_list)

print (len(master_rules_list),"is the number of rules generated with brute force")
print(len(master_pruned_list),"is the number of rules generated with confidence pruning")
sorted_rule_list = sorted(master_rules_list,reverse = True, key = lambda x: int(x[2]))
##print(sorted_rule_list)
print("this is the solution for part (e)")
print("The top 10 rules are:")
for j in range(0,11):
    print(sorted_rule_list[j])


################################################################### lift as interestingness measure ###############################

#rules using lift as a interestingness measure
master_lift_list = []
for each in master:
    if len(each[0]) >= 2:
        for r_value in range(1,len(each[0])):
            for subsets in combinations(each[0],r_value):
                list_subset = []
                list_parent = []
                main_list_lift = []
                if len(list(subsets)) == 1:
                    for key,value in x.items():
                        if list(subsets)[0] == key:

                            confidence = (each[1]/value)
                            if confidence > 0:
                                z = list(each[0])
                                for subset_length_1 in subsets:
                                    c = subset_length_1
                                    if subset_length_1 in z:
                                        z.remove(subset_length_1)
                                        list_subset = list(subsets)
                                        list_parent = z
                                        for key_m,values_m in x.items():
                                            if list_parent[0] == key_m:
                                                lift_measure = (confidence/values_m)*rows
                                                main_list_lift.append(list_subset)
                                                main_list_lift.append(list_parent)
                                                main_list_lift.append(lift_measure)
                                                master_lift_list.append(main_list_lift)
                            break
                else:
                    flag = True
                    temp_subset = list(subsets)
                    merged_subset = ','.join(temp_subset)
                    for key,value in x.items():
                        if merged_subset == key:

                            confidence = (each[1]/value)
                            if confidence > 0:
                                split = list(each[0])
                                for every_element in subsets:
                                    c = every_element
                                    if every_element in split:
                                        split.remove(every_element)
                                        flag = True
                                if flag == True:
                                    list_subset = list(subsets)
                                    list_parent = split
                                    for key_p,values_p in x.items():
                                        temp_parent = ','.join(list_parent)
                                        if temp_parent == key_p:
                                            lift_measure = (confidence/values_p)*rows
                                            main_list_lift.append(list_subset)
                                            main_list_lift.append(list_parent)
                                            main_list_lift.append(lift_measure)
                                            master_lift_list.append(main_list_lift)


##print(master_lift_list)
sorted_lift_list = sorted(master_lift_list,reverse = True, key = lambda x: int(x[2]))
print("The top 10 rules with lift as measure are:")
for j in range(0,11):
    print(sorted_lift_list[j])

