# coding: cp949
print("""
0~3��(����) : ����
4~13��(���) : 2000��
14~18��(û�ҳ�) : 3000��
19~65��(����) : 5000��
66�� �̻�(����) : ����
 """)

while True:
    age = int(input("���̸� �Է��ϼ��� : "))
    if age <= 3:
        if age<0:
            print("�ٽ��Է��ϼ���")
            continue
        else :
            grade="����"
            charge=0
    elif age <= 13:
        grade="���"
        charge=2000
    elif age <= 18:
        grade="û�ҳ�"
        charge=3000
    elif age <= 65:
        grade="����"
        charge=5000
    else :
        grade="����"
        charge=0
    break

if charge>0:
    print("���ϴ� %s ����̸�, ����� %s�� �Դϴ�." %(grade, charge))
    money = int(input("����� �Է��ϼ���."))
    if money<charge:
        print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�." %((charge-money) ,money))
    elif money==charge:
        print("�����մϴ�. Ƽ���� �����մϴ�.")
    else :
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(money-charge))

elif charge==0:
    print("���ϴ� %s ����̸�, ����� ���� �Դϴ�." %grade)
    print("�����մϴ�. Ƽ���� �����մϴ�.")


