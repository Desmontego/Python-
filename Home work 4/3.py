from random import randrange

def list_random(count:int):
    if count < 0:
        print("Введено отрицательное значение")
        return[]

    list_num = []
    for i in range(count):
        list_num.append(randrange(count))

    return list_num

def uniq(list_num: list):
    result = []
    my_dict = {}.fromkeys(list_num, 0)

    for i in list_num:
        my_dict [i] += 1
        
    for k in my_dict:
        if my_dict[k] ==1:    
            result.append(k)
    return result

all_list = list_random(int(input("Число :")))
print(all_list)
print(uniq(all_list))    