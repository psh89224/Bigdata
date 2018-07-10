import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

m = p.search("python")
print(m)

result = p.findall("life is too short")
print(result)