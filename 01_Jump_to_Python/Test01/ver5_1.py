# coding: cp949
print("""
0~3��(����) : ����
4~13��(���) : 2000��
14~18��(û�ҳ�) : 3000��
19~65��(����) : 5000��
66�� �̻�(����) : ����
 """)
output_msg="���̸� �Է��ϼ���."

event_ticket = 3
year_ticket = 5
count = 0

while True:
    print(output_msg,end='')
    age = int(input())

    if 0 <= age <= 3:
        print("���ϴ� [����] ����̸�, ����� ����  �Դϴ�.")
        print("�����մϴ�. Ƽ���� �����մϴ�")        

    elif 4 <= age <= 13:
        print("���ϴ� [���] ����̸�, ����� 2000�� �Դϴ�.")
        pay = int(input("��������� �Է��ϼ���.(1:����, 2:���� ���� �ſ�ī��)"))
        if pay ==1:
            charge = int(input("����� �Է��ϼ���."))
            if charge == 2000:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            elif charge < 2000:
                print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�." %((2000-charge) ,charge))
            elif charge > 2000:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(charge-2000))
                count = count +1
        elif pay ==2:
            print("%d�� �����Ǿ����ϴ�. Ƽ���� �����մϴ�." %(2000*0.9))
            count = count +1
        
        if count%7==0 and event_ticket!=0:
            event_ticket = event_ticket - 1
            print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ�����Ƽ�� %d��" %event_ticket)
        elif count%4==0 and year_ticket!=0:
            year_ticket = year_ticket -1
            print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ�����Ƽ�� %d��" %year_ticket)
            
    elif 14 <= age <= 18:
        print("���ϴ� [û�ҳ�] ����̸�, ����� 3000�� �Դϴ�.")
        pay = int(input("��������� �Է��ϼ���.(1:����, 2:���� ���� �ſ�ī��)"))
        if pay == 1:
            charge = int(input("����� �Է��ϼ���."))
            if charge == 3000:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            elif charge < 3000:
                print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�." %((3000-charge) ,charge))
            elif charge > 3000:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(charge-3000))
            count = count +1
        elif pay ==2:
            print("%d�� �����Ǿ����ϴ�. Ƽ���� �����մϴ�." %(3000*0.9))
            count = count +1

        if count%7==0 and event_ticket!=0:
            event_ticket = event_ticket - 1
            print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ�����Ƽ�� %d��" %event_ticket)
        elif count%4==0 and year_ticket!=0:
            year_ticket = year_ticket -1
            print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ�����Ƽ�� %d��" %year_ticket)

    elif 19 <= age <= 59:
        print("���ϴ� [����] ����̸�, ����� 5000�� �Դϴ�.")
        pay = int(input("��������� �Է��ϼ���.(1:����, 2:���� ���� �ſ�ī��)"))
        if pay ==1:
            charge = int(input("����� �Է��ϼ���."))
            if charge == 5000:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            elif charge < 5000:
                print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�." %((5000-charge) ,charge))
            elif charge > 5000:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(charge-5000))
            count = count +1
        elif pay ==2:
            print("%d�� �����Ǿ����ϴ�. Ƽ���� �����մϴ�." %(5000*0.9))
            count = count +1

        if count%7==0 and event_ticket!=0:
            event_ticket = event_ticket - 1
            print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ�����Ƽ�� %d��" %event_ticket)
        elif count%4==0 and year_ticket!=0:
            year_ticket = year_ticket -1
            print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ�����Ƽ�� %d��" %year_ticket)

    elif 60 <= age <= 65:
        print("���ϴ� [����] ����̸�, ����� 5000�� �Դϴ�.")
        pay = int(input("��������� �Է��ϼ���.(1:����, 2:���� ���� �ſ�ī��)"))
        if pay ==1:
            charge = int(input("����� �Է��ϼ���."))
            if charge == 5000:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            elif charge < 5000:
                print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�." %((5000-charge) ,charge))
            elif charge > 5000:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %(charge-5000))
            count = count +1
        elif pay ==2:
            print("%d�� �����Ǿ����ϴ�. Ƽ���� �����մϴ�." %((5000*0.9)*0.95))
            count = count +1

        if count%7==0 and event_ticket!=0:
            event_ticket = event_ticket - 1
            print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ�����Ƽ�� %d��" %event_ticket)
        elif count%4==0 and year_ticket!=0:
            year_ticket = year_ticket -1
            print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ�����Ƽ�� %d��" %year_ticket)

    elif age >= 66:
        print("���ϴ� [����] ����̸�, ����� �����Դϴ�.")
        print("�����մϴ�. Ƽ���� �����մϴ�")

    elif age < 0:
        print("�ٽ� �Է��ϼ���")
        continue

