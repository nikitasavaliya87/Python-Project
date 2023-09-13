# number=[1,2,3]
# new_number=[n+1 for n in number]
# print(new_number)

# range(1,5)
# new_number=[n*2 for n in range(1,5)]
# print(new_number)

# names=["Alex","Beth","Caroline","Dave","Eleanor","Freedie"]
# short_name=[name.upper() for name in names if len(name)>5]
# print(short_name)


# number=[1,1,2,3,5,8,13,21,34,55]
# squared_number=[n**2 for n in number]
# print(squared_number)

# number=[1,1,2,3,5,8,13,21,34,55]
# result=[n for n in number if n%2==0]
# print(result)
l1=[]
with open("Angelia\\Day_26_List_Comprehension\\file1.txt") as f1:
    file1_data=f1.readlines()
    
with open("Angelia\\Day_26_List_Comprehension\\file2.txt") as f2:
    file2_data=f2.readlines()   

result=[int(num) for num in file1_data if num in file2_data]
    
print(result)
