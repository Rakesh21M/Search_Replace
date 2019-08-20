import re
import pandas as pd
import os

current_dir = os.getcwd()

print(current_dir+"/data/names.xlsx")
data = pd.read_excel(current_dir+"/data/names.xlsx")
#print(data.head())
f = open(current_dir+"/data/Test.txt", "r")
string = f.read()
s_list = string.split('\n')
pattern = str(input("Enter the pattern starting : "))
star1 = int(input("Enter the 1st star to skip : "))
star2 = int(input("Enter the 2nd star to skip : "))
n = len(s_list)-1
print("Number of pattern line got ", n)
s_original = list()
i = 0

# s_list contain actual list
for sslist in s_list:
    j = 0
    s_sample = sslist
    if re.search("\A"+pattern, s_sample):
        
        # s_list1 contain * splited items
        s_list1 = sslist.split('*')
        s_list1[star1] = data.iloc[i,j]
        j = j + 1
        s_list1[star2] = data.iloc[i,j]
        s_join = "*".join(s_list1)
        s_original.append(s_join)
        i = i + 1
    else:
        s_original.append(s_sample)
        
#print(s_original)

s_save = "\n".join(s_original)
f1 = open(current_dir+"/output/final_sheet.txt", "w")
f1.write(s_save)
 
f.close()
f1.close()
