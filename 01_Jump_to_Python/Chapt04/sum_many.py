def math(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    elif choice == "sub":
        result = args[0]
        for i in args[1:]:
            result = result - i
    elif choice == "div":
        result = args[0]
        for i in args[1:]:
            result = result / i
    return result



result=math('sub', 5,4,3,2,1)
print(result)
