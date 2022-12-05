user=input("Введите число :")
sum = 0

a =len(user) -2 
user=float(user)
user*=int(10** a)

while user:
    sum +=int(user%10)
    user//=10

print(int(sum))    