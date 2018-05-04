# coding: cp949
print("""
0~3세(유아) : 무료
4~13세(어린이) : 2000원
14~18세(청소년) : 3000원
19~65세(성인) : 5000원
66세 이상(노인) : 무료
 """)

event_ticket = 3
year_ticket = 5
count = 1

while True:
    age = int(input("나이를 입력하세요 : "))
    if age <= 3:
        if age<0:
            print("다시입력하세요")
            continue
        else :
            grade="유아"
            charge=0
    elif age <= 13:
        grade="어린이"
        charge=2000
    elif age <= 18:
        grade="청소년"
        charge=3000
    elif age <= 65:
        grade="성인"
        charge=5000
    else :
        grade="노인"
        charge=0

    if charge>0:
        print("귀하는 %s 등급이며, 요금은 %s원 입니다." %(grade, charge))
        pay = int(input("요금유형을 입력하세요.(1:현금, 2:공원 전용 신용카드) "))
        if pay ==1:
            money = int(input("요금을 입력하세요."))
            if money<charge:
                print("%d가 모자랍니다. 입력하신 %d를 반환합니다." %((charge-money) ,money))
                continue
            elif money==charge:
                print("감사합니다. 티켓을 발행합니다.")
            else :
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %(money-charge))

        elif pay ==2:
            if 60 <= age <= 65:
                print("%d원 결제되었습니다. 티켓을 발행합니다." %((charge*0.9)*0.95))
            else :
                print("%d원 결제되었습니다. 티켓을 발행합니다."%(charge*0.9))

        if count%7==0 and event_ticket!=0:
            event_ticket -= 1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료티켓을 발행합니다. 잔여무료티켓 %d장" %event_ticket)
        elif count%4==0 and year_ticket!=0:
            year_ticket -= 1
            print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여할인티켓 %d장" %year_ticket)
        count += 1

    elif charge==0:
        print("귀하는 %s 등급이며, 요금은 무료 입니다." %grade)
        print("감사합니다. 티켓을 발행합니다.")

