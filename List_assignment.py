List = []

for x in range(0,15,1) :
    n = int(input("정수 입력: "))
    for y in range(0,1,1) :
        List.append(n)
    if x>=14 :
        print(List)
    else :
        pass

for a in range(1,16,1) :
    if a%2 == 0 :
        List.remove(a)
    else :
        pass
print(List)

for b in range(1,16,1) :
    if b%3 == 0 :
        if b%2 != 0 :
            List.remove(b)
        else :
            pass
    else :
        pass
print(List)

pop = List.pop(0)
print(pop)
List.insert(0,2)
List.insert(1,3)
print(List)