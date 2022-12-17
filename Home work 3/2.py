from random import sample


def random_list(count: int):
    if count < 0: 
        print("Отрицательно значение")
        return []
    l_numb = sample(range(1, count * 2), count)
    return l_numb
def summ_pos(l_numb: list):
    sum_num= []
    len_list= len(l_numb)

    for k in range(len_list // 2 ):
        sum_num.append(l_numb[k] * l_numb[len_list-k-1])

    if len_list % 2:
        sum_num.append(l_numb[len_list // 2])
    return sum_num
all_list = random_list(int(input("Введите число-> ")))
print(all_list)
print(summ_pos(all_list))

