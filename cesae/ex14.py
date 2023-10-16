#ler 3 numeros
num1=float(input("insira 1 numero"))
num2=float(input("insira 2 numero"))
num3=float(input("insira 3 numero"))

#colocar numeros ordem crescente
if  (num1<num2 and num2<num3):
    print(num1,num2,num3)
elif   (num2<num1 and num1<num3):
    print(num2,num1,num3)
elif (num3<num1 and num1<num2):
    print(num3,num1,num2)
elif ( num3<num2 and num2<num1):
    print(num3,num2,num1)
elif (num1<num3 and num3<num2):
    print(num1,num3,num2)
elif (num2<num3 and num3<num1):
    print(num2,num3,num1)