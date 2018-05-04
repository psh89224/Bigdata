# coding: cp949
print("""
0~3세(유아) : 무료
4~13세(어린이) : 2000원
14~18세(청소년) : 3000원
19~65세(성인) : 5000원
66세 이상(노인) : 무료
 """)

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
    break

if charge>0:
    print("귀하는 %s 등급이며, 요금은 %s원 입니다." %(grade, charge))
    money = int(input("요금을 입력하세요."))
    if money<charge:
        print("%d가 모자랍니다. 입력하신 %d를 반환합니다." %((charge-money) ,money))
    elif money==charge:
        print("감사합니다. 티켓을 발행합니다.")
    else :
        print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %(money-charge))

elif charge==0:
    print("귀하는 %s 등급이며, 요금은 무료 입니다." %grade)
    print("감사합니다. 티켓을 발행합니다.")


