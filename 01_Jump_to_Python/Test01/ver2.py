# coding: cp949
print("""
0~3세(유아) : 무료
4~13세(어린이) : 2000원
14~18세(청소년) : 3000원
19~65세(성인) : 5000원
66세 이상(노인) : 무료
 """)
output_msg="나이를 입력하세요."
while True:
    print(output_msg,end='')
    age = int(input())
    if 0 <= age <= 3:
        print("귀하는 [유아] 등급이며, 요금은 무료  입니다.")
    elif 4 <= age <= 13:
        print("귀하는 [어린이] 등급이며, 요금은 2000원 입니다.")
    elif 14 <= age <= 18:
        print("귀하는 [청소년] 등급이며, 요금은 3000원 입니다.")
    elif 19 <= age <= 65:
        print("귀하는 [성인] 등급이며, 요금은 5000원 입니다.")
    elif age >= 66:
        print("귀하는 [노인] 등급이며, 요금은 무료입니다.")

    elif age < 0:
        print("다시 입력하세요")
        continue

