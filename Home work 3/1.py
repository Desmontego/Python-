from random import sample


def random_list(count: int):
    if count < 0: 
        print("Отрицательно значение")
        return []
    l_numb = sample(range(1, count * 2), count)
    return l_numb
def summ_pos(l_numb: list):
    sum_num= 0
    for k in range(0, len(l_numb), 2):
       sum_num += l_numb[k]
    return sum_num
all_list = random_list(int(input("Введите число-> ")))
print(all_list)
print(summ_pos(all_list))
