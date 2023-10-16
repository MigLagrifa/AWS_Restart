#pedir 3 numeros
num1=float(input("Coloque numero 1"))
num2=float(input("Coloque numero 2"))
num3=float(input("Coloque numero 3"))
ordem=input("Selecione se deseja por ordem crescente ou decrescente")
#pedir ordem crescente ou decrescente

#colocar por ordem crescente ou decrescente
if (ordem=="decrescente" and num1>num2 and num2>num3):
    print(num1,num2,num3)
elif (ordem=="decrescente" and num2>num1 and num1>num3):
    print(num2,num1,num3)
elif (ordem=="decrescente" and num3>num1 and num1>num2):
    print(num3,num1,num2)
elif (ordem=="decrescente" and num3>num2 and num2>num1):
    print(num3,num2,num1)
elif (ordem=="decrescente" and num1>num3 and num3>num2):
    print(num1,num3,num2)
elif (ordem=="decrescente" and num2>num3 and num3>num1):
    print(num2,num3,num1)

elif (ordem=="crescente" and num1<num2 and num2<num3):
    print(num1,num2,num3)
elif (ordem=="crescente" and num2<num1 and num1<num3):
    print(num2,num1,num3)
elif (ordem=="crescente" and num3<num1 and num1<num2):
    print(num3,num1,num2)
elif (ordem=="crescente" and num3<num2 and num2<num1):
    print(num3,num2,num1)
elif (ordem=="crescente" and num1<num3 and num3<num2):
    print(num1,num3,num2)
elif (ordem=="crescente" and num2<num3 and num3<num1):
    print(num2,num3,num1)