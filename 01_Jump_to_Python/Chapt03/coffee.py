#coding:cp949
coffee = 10

prompt="""
1.Ŀ�Ǳ���
2.Ŀ���ܷ�Ȯ��
3.���α׷�����
�޴��� �����ϼ��� : """

while True:
    print(prompt,end='')
    number = int(input())

    if number==1:
        money = int(input("�ݾ��� �Է��ϼ��� : "))
        if money == 300:
            print("Ŀ�Ǹ� �ݴϴ�.")
            coffee = coffee -1
        elif money > 300:
            print("���� �Ž����� %d �Դϴ�." %(money-300))
            coffee = coffee -1
        else:
            print("�ݾ��� %d ���ڶ��ϴ�." %(300-money))
            print("���� �ٽ� �����ְ� Ŀ�Ǹ� �����ʽ��ϴ�")

    print("���� Ŀ���� ���� %d�� �Դϴ�.\n" %coffee)

    if number==2:
        print("���� Ŀ���� ���� %d�� �Դϴ�.\n" %coffee)

    if number==3:
        print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.\n")
        break

    if not coffee:
        print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.\n")
        break
