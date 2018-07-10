f = open("연습생.txt", 'r', encoding="UTF-8")
list = f.readlines()

def show_candidates(candidate_list):
    for i in candidate_list:
        print(i)

def make_idol(candidate_list):
    for i in candidate_list:
        i = i.replace("\n", "")
        print("신예 아이돌 %s 인기 급상승" %i)

def make_world_star(candidate_list):
    for i in candidate_list:
        i = i.replace("\n", "")
        print("아이돌 %s  월드스타 등극" %i)

show_candidates(list)
make_idol(list)
make_world_star(list)

f.close()