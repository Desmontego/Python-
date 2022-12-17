def tr_late(num: int):
    list_nums =[]

    while num > 0:
        list_nums.insert(0, num % 2)
        num //= 2
    print(*list_nums, sep="")
    
tr_late(int(input()))
