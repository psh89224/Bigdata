# coding: cp949
print("""
0~3�� : ����
4~13�� : 2000��
14~18�� : 3000��
19~65�� : 5000��
66�� �̻� : ����
 """)
output_msg="���̸� �Է��ϼ���."

while True:
    print(output_msg,end='')
    age = int(input())

    if age <= 3:
        print("����� ����  �Դϴ�.")
    elif age <= 13:
        print("����� 2000�� �Դϴ�.")
    elif age <= 18:
        print("����� 3000�� �Դϴ�.")
    elif age <= 65:
        print("����� 5000�� �Դϴ�.")
    elif age >= 66:
        print("����� �����Դϴ�.")

