# coding: cp949
print("""
0~3��(����) : ����
4~13��(���) : 2000��
14~18��(û�ҳ�) : 3000��
19~65��(����) : 5000��
66�� �̻�(����) : ����
 """)

event_ticket = 3
year_ticket = 5
count = 1

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

    if charge>0:
        print("���ϴ� %s ����̸�, ����� %s�� �Դϴ�." %(grade, charge))
        pay = int(input("��������� �Է��ϼ���.(1:����, 2:���� ���� �ſ�ī��) "))
        if pay ==1:
            money = int(input("����� �Է��ϼ���."))
            if money<charge:
                print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�." %((charge-money) ,money))
                continue
            elif money==charge:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            else :
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(money-charge))

        elif pay ==2:
            if 60 <= age <= 65:
                print("%d�� �����Ǿ����ϴ�. Ƽ���� �����մϴ�." %((charge*0.9)*0.95))
            else :
                print("%d�� �����Ǿ����ϴ�. Ƽ���� �����մϴ�."%(charge*0.9))

        if count%7==0 and event_ticket!=0:
            event_ticket -= 1
            print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ�����Ƽ�� %d��" %event_ticket)
        elif count%4==0 and year_ticket!=0:
            year_ticket -= 1
            print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ�����Ƽ�� %d��" %year_ticket)
        count += 1

    elif charge==0:
        print("���ϴ� %s ����̸�, ����� ���� �Դϴ�." %grade)
        print("�����մϴ�. Ƽ���� �����մϴ�.")

