from random import sample

def listRand(count: int, alp: str = "абв"):
    Wlist=[]
    for i in range(count):
        let = sample(alp, 3)
        Wlist.append("".join(let))
    return " ".join(Wlist)

def sentence(words: str) -> str:
    # return " ".join(i for i in words.split()if i != "абв")
    return " ".join(words.replace("абв", "").split())
all_list = listRand(int(input("Введите значение: ")))
print(all_list)
print(sentence(all_list))