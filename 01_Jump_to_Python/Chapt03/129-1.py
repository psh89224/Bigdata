#coding:cp949
index = 0 
big_data = [1,2,3,4,5,6,7,8,9,10]

while True:
    index += 1
    print("index : %d" %index)
    big_data = big_data*1000000
    print(big_data)
#    print("Ctrl + C를 눌러야 종료가 됩니다")
