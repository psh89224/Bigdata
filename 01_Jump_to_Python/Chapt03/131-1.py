#coding=cp949
my_data=[1,1,1,1,1,2,2,3,3,4,4,5,5,6,2,5]
print(my_data)
uniqe_data=set(my_data)
print(uniqe_data)

for element in uniqe_data:
    print(element)

t_data=(44,55,66,77,33,44,55)
for element in t_data:
    print(element)

str_data="Hello World"
for element in str_data:
    print(element)

dic_data={"이름":"박석현",
        "나이":30,
        "취미":"몰라"}
for element in dic_data:
    print(element)
for key in dic_data:
    print(key+' '+str(dic_data[key]))

