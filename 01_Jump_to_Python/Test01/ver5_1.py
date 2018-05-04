# coding: cp949
print("""
0~3세(유아) : 무료
4~13세(어린이) : 2000원
14~18세(청소년) : 3000원
19~65세(성인) : 5000원
66세 이상(노인) : 무료
 """)
output_msg="나이를 입력하세요."

event_ticket = 3
year_ticket = 5
count = 0

while True:
    print(output_msg,end='')
    age = int(input())

    if 0 <= age <= 3:
        print("귀하는 [유아] 등급이며, 요금은 무료  입니다.")
        print("감사합니다. 티켓을 발행합니다")        

    elif 4 <= age <= 13:
        print("귀하는 [어린이] 등급이며, 요금은 2000원 입니다.")
        pay = int(input("요금유형을 입력하세요.(1:현금, 2:공원 전용 신용카드)"))
        if pay ==1:
            charge = int(input("요금을 입력하세요."))
            if charge == 2000:
                print("감사합니다. 티켓을 발행합니다.")
            elif charge < 2000:
                print("%d가 모자랍니다. 입력하신 %d를 반환합니다." %((2000-charge) ,charge))
            elif charge > 2000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %(charge-2000))
                count = count +1
        elif pay ==2:
            print("%d원 결제되었습니다. 티켓을 발행합니다." %(2000*0.9))
            count = count +1
        
        if count%7==0 and event_ticket!=0:
            event_ticket = event_ticket - 1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료티켓을 발행합니다. 잔여무료티켓 %d장" %event_ticket)
        elif count%4==0 and year_ticket!=0:
            year_ticket = year_ticket -1
            print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여할인티켓 %d장" %year_ticket)
            
    elif 14 <= age <= 18:
        print("귀하는 [청소년] 등급이며, 요금은 3000원 입니다.")
        pay = int(input("요금유형을 입력하세요.(1:현금, 2:공원 전용 신용카드)"))
        if pay == 1:
            charge = int(input("요금을 입력하세요."))
            if charge == 3000:
                print("감사합니다. 티켓을 발행합니다.")
            elif charge < 3000:
                print("%d가 모자랍니다. 입력하신 %d를 반환합니다." %((3000-charge) ,charge))
            elif charge > 3000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %(charge-3000))
            count = count +1
        elif pay ==2:
            print("%d원 결제되었습니다. 티켓을 발행합니다." %(3000*0.9))
            count = count +1

        if count%7==0 and event_ticket!=0:
            event_ticket = event_ticket - 1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료티켓을 발행합니다. 잔여무료티켓 %d장" %event_ticket)
        elif count%4==0 and year_ticket!=0:
            year_ticket = year_ticket -1
            print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여할인티켓 %d장" %year_ticket)

    elif 19 <= age <= 59:
        print("귀하는 [성인] 등급이며, 요금은 5000원 입니다.")
        pay = int(input("요금유형을 입력하세요.(1:현금, 2:공원 전용 신용카드)"))
        if pay ==1:
            charge = int(input("요금을 입력하세요."))
            if charge == 5000:
                print("감사합니다. 티켓을 발행합니다.")
            elif charge < 5000:
                print("%d가 모자랍니다. 입력하신 %d를 반환합니다." %((5000-charge) ,charge))
            elif charge > 5000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %(charge-5000))
            count = count +1
        elif pay ==2:
            print("%d원 결제되었습니다. 티켓을 발행합니다." %(5000*0.9))
            count = count +1

        if count%7==0 and event_ticket!=0:
            event_ticket = event_ticket - 1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료티켓을 발행합니다. 잔여무료티켓 %d장" %event_ticket)
        elif count%4==0 and year_ticket!=0:
            year_ticket = year_ticket -1
            print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여할인티켓 %d장" %year_ticket)

    elif 60 <= age <= 65:
        print("귀하는 [성인] 등급이며, 요금은 5000원 입니다.")
        pay = int(input("요금유형을 입력하세요.(1:현금, 2:공원 전용 신용카드)"))
        if pay ==1:
            charge = int(input("요금을 입력하세요."))
            if charge == 5000:
                print("감사합니다. 티켓을 발행합니다.")
            elif charge < 5000:
                print("%d가 모자랍니다. 입력하신 %d를 반환합니다." %((5000-charge) ,charge))
            elif charge > 5000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %(charge-5000))
            count = count +1
        elif pay ==2:
            print("%d원 결제되었습니다. 티켓을 발행합니다." %((5000*0.9)*0.95))
            count = count +1

        if count%7==0 and event_ticket!=0:
            event_ticket = event_ticket - 1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료티켓을 발행합니다. 잔여무료티켓 %d장" %event_ticket)
        elif count%4==0 and year_ticket!=0:
            year_ticket = year_ticket -1
            print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여할인티켓 %d장" %year_ticket)

    elif age >= 66:
        print("귀하는 [노인] 등급이며, 요금은 무료입니다.")
        print("감사합니다. 티켓을 발행합니다")

    elif age < 0:
        print("다시 입력하세요")
        continue

