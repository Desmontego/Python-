# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

X1=int(input("Введите координату X1 :"))
X2=int(input("Введите координату X2 :"))
Y1=int(input("Введите координату Y1 :"))
Y2=int(input("Введите координату Y2 :"))

a= (((Y1-X1)*(Y1-X1))+((Y2-X2)*(Y2-X2)))
sqrt =(a**(0.5))* 100 / 100
print(sqrt)
print("%.4f" % sqrt)