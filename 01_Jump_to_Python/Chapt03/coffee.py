#coding:cp949
coffee = 10

prompt="""
1.커피구매
2.커피잔량확인
3.프로그램종료
메뉴를 선택하세요 : """

while True:
    print(prompt,end='')
    number = int(input())

    if number==1:
        money = int(input("금액을 입력하세요 : "))
        if money == 300:
            print("커피를 줍니다.")
            coffee = coffee -1
        elif money > 300:
            print("여기 거스름돈 %d 입니다." %(money-300))
            coffee = coffee -1
        else:
            print("금액이 %d 모자랍니다." %(300-money))
            print("돈을 다시 돌려주고 커피를 주지않습니다")

    print("남은 커피의 양은 %d개 입니다.\n" %coffee)

    if number==2:
        print("남은 커피의 양은 %d개 입니다.\n" %coffee)

    if number==3:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.\n")
        break

    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.\n")
        break
