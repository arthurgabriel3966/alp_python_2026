#valor = float(input(f"Dígite quantos reais gostaria de converter: "))
#real = valor*1
#dolar = real/5.24
#print(f"A conversão de {real} reais é igual a: {dolar} dolares")
valor = int(input("Escolha quantos reais você quer converter: "))
real = valor/1
dolar = valor/5.24
euro = valor/6.05
opção = int(input("Digite oq quer converter 1-euro 2-dolar: "))
if opção==1:
    print(f"{real} reais é igual a {euro:.2f} euros")
elif opção==2:
    print(f"{real} reais é igual a {dolar:.2f} dolares")
else:
    print("Esse valor não existe.")


