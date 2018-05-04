# coding: cp949
print("""
0~3세 : 무료
4~13세 : 2000원
14~18세 : 3000원
19~65세 : 5000원
66세 이상 : 무료
 """)
output_msg="나이를 입력하세요."

while True:
    print(output_msg,end='')
    age = int(input())

    if age <= 3:
        print("요금은 무료  입니다.")
    elif age <= 13:
        print("요금은 2000원 입니다.")
    elif age <= 18:
        print("요금은 3000원 입니다.")
    elif age <= 65:
        print("요금은 5000원 입니다.")
    elif age >= 66:
        print("요금은 무료입니다.")

