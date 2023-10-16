#ler valor multiplo de 5
num1=int(input("Insira um valor€"))
valor=num1%5!=0
#calcular menor numero possivel de notas
if (valor):
    print("notas de 200:",num_notas)
else:
    print("valor invalido,deve ser multiplo de 5")
#200
num_notas=int(num1/200)
num1=num1%200
print("Notas 200",num_notas)
#100
num_notas=int(num1/100)
num1=num1%100
print("Notas 100",num_notas)
#50
num_notas=int(num1/50)
num1=num1%50
print("Notas 50",num_notas)
#20
num_notas=int(num1/20)
num1=num1%20
print("Notas 20",num_notas)
#10
num_notas=int(num1/10)
num1=num1%10
print("Notas 10",num_notas)
#5
num_notas=int(num1/5)
num1=num1%5
print("Notas 5",num_notas)