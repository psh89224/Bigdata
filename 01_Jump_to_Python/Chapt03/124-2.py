#coding=cp949

prompt="""
1.Add
2.Del
3.List
4.Quit

Enter number:"""

number=0
while True:
    print(prompt,end='')
    number=int(input())

    if number ==4:
        break #while문 종료가 되는 조건이 2개 이상일때
    else: 
        if number ==5:
            break
