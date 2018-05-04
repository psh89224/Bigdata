#coding:cp949
# 입력 : 인자(Argument, Paramater)
# 출력 : return (print를 의미하는 것이 아님)

def my_sum1(num1,num2): #입력, 출력을 모두 지정하는 케이스
    result = num1+num2
    return result #연산, 비즈니스 로직에만 집중

def my_sum2(num1,num2): #입력만 있는 케이스
    result = num1+num2
    print("%d+%d=%d" %(num1,num2,result)) #출력이 필요없거나 모두 처리하고자 할때

def my_sum3(num1,num2): #출력(return)만 지정하는 케이스
    #입력을 함수에서 처리
    num1 = int(input("첫번째 수를 입력하세요"))
    num2 = int(input("두번째 수를 입력하세요"))
    result = num1+num2
    return result

def my_sum4(num1,num2): #입력/출력(return)이 없는 케이스
    #함수안에서 모든 것을 처리
    num1 = int(input("첫번째 수를 입력하세요"))
    num2 = int(input("두번째 수를 입력하세요"))
    result = num1+num2
    print("%d+%d=%d" %(num1,num2,result))

num1 = int(input("첫번째 수를 입력하세요"))
num2 = int(input("두번째 수를 입력하세요"))
result = my_sum1(num1,num2)
print("%d+%d=%d" %(num1,num2,result))

num1 = input("첫번째 수를 입력하세요")
num2 = input("두번째 수를 입력하세요")
my_sum2(num1,num2)
result = my_sum3()
print("%d+%d=%d"%(num1,num2,result))
my_sum4()
