def input_ingredient():
    ingredient_list=[]

    while True:
        list = input("안녕하세요. 원하시는 재료를 입력하세요 : ")
        if list=='종료':
            return ingredient_list
        ingredient_list.append(list)

def make_sandwiches(ingredient_list):
    print("샌드위치를 만들겠습니다.")
    for i in ingredient_list:
        print("%s 추가합니다." %i)

prompt="""
안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.
1. 주문
2. 종료
입력 : """

while True:
    print(prompt,end=' ')
    number = int(input())

    if number == 1:
        make_sandwiches(input_ingredient())
        print("주문하신 샌드위치입니다. 맛있게 드세요")

    elif number == 2:
        print("종료합니다")
        break




