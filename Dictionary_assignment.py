Dic = {}

while True :
    key = int(input("정수 key 값: "))
    value = str(input("문자열 value 값: "))
    if key == 0 :
        print("그만")
        print(Dic)
        break
    elif value == '문자열 종료' :
        print("그만")
        print(Dic)
        break
    else :
        Dic[key] = value

dict_keys = []
dict_values = []
dict_items = []

dict_keys.append(Dic.keys())
print(dict_keys)

dict_values.append(Dic.values())
print(dict_values)

dict_items.append(Dic.items())
print(dict_items)