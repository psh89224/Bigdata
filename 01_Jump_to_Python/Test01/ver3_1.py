# coding: cp949
print("""
0~3��(����) : ����
4~13��(���) : 2000��
14~18��(û�ҳ�) : 3000��
19~65��(����) : 5000��
66�� �̻�(����) : ����
 """)
output_msg="���̸� �Է��ϼ���."

while True:
    print(output_msg,end='')
    age = int(input())

    if 0 <= age <= 3:
        print("���ϴ� [����] ����̸�, ����� ����  �Դϴ�.")
        print("�����մϴ�. Ƽ���� �����մϴ�")

    elif 4 <= age <= 13:
        print("���ϴ� [���] ����̸�, ����� 2000�� �Դϴ�.")
        charge = int(input("����� �Է��ϼ���."))
        if charge == 2000:
            print("�����մϴ�. Ƽ���� �����մϴ�.")
        elif charge < 2000:
            print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�." %((2000-charge) ,charge))
        elif charge > 2000:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(charge-2000))

    elif 14 <= age <= 18:
        print("���ϴ� [û�ҳ�] ����̸�, ����� 3000�� �Դϴ�.")
        charge = int(input("����� �Է��ϼ���."))
        if charge == 3000:
            print("�����մϴ�. Ƽ���� �����մϴ�.")
        elif charge < 3000:
            print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�." %((3000-charge) ,charge))
        elif charge > 3000:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(charge-3000))

    elif 19 <= age <= 65:
        print("���ϴ� [����] ����̸�, ����� 5000�� �Դϴ�.")
        charge = int(input("����� �Է��ϼ���."))
        if charge == 5000:
            print("�����մϴ�. Ƽ���� �����մϴ�.")
        elif charge < 5000:
            print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�." %((5000-charge), charge))
        elif charge > 5000:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(charge-5000))

    elif age >= 66:
        print("���ϴ� [����] ����̸�, ����� �����Դϴ�.")
        print("�����մϴ�. Ƽ���� �����մϴ�")

    elif age < 0:
        print("�ٽ� �Է��ϼ���")
        continue
