#coding:cp949
# �Է� : ����(Argument, Paramater)
# ��� : return (print�� �ǹ��ϴ� ���� �ƴ�)

def my_sum1(num1,num2): #�Է�, ����� ��� �����ϴ� ���̽�
    result = num1+num2
    return result #����, ����Ͻ� �������� ����

def my_sum2(num1,num2): #�Է¸� �ִ� ���̽�
    result = num1+num2
    print("%d+%d=%d" %(num1,num2,result)) #����� �ʿ���ų� ��� ó���ϰ��� �Ҷ�

def my_sum3(num1,num2): #���(return)�� �����ϴ� ���̽�
    #�Է��� �Լ����� ó��
    num1 = int(input("ù��° ���� �Է��ϼ���"))
    num2 = int(input("�ι�° ���� �Է��ϼ���"))
    result = num1+num2
    return result

def my_sum4(num1,num2): #�Է�/���(return)�� ���� ���̽�
    #�Լ��ȿ��� ��� ���� ó��
    num1 = int(input("ù��° ���� �Է��ϼ���"))
    num2 = int(input("�ι�° ���� �Է��ϼ���"))
    result = num1+num2
    print("%d+%d=%d" %(num1,num2,result))

num1 = int(input("ù��° ���� �Է��ϼ���"))
num2 = int(input("�ι�° ���� �Է��ϼ���"))
result = my_sum1(num1,num2)
print("%d+%d=%d" %(num1,num2,result))

num1 = input("ù��° ���� �Է��ϼ���")
num2 = input("�ι�° ���� �Է��ϼ���")
my_sum2(num1,num2)
result = my_sum3()
print("%d+%d=%d"%(num1,num2,result))
my_sum4()
