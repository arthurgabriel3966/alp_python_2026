num1 = float(input("Dígite seu 1° numero: "))
num2 = float(input("Dígite seu 2° numero: "))
print("Menu")
print("-"*50)
print(""" 1 - Média ponderada com peso 2 e 3
 2 - Quadrado da soma dos dois numeros
 3 - Cubo do menor numero""" )
print("-"*50)
opcao = input("Escolha uma opção: ")
if opcao == "1": 
    resultado = ((num1*2)+(num2*3))/(2+3)
    print(f"A média ponderada destes números é {resultado}")
elif opcao == "2": 
    resultado = (num1+num2)**2
    print(f"O quadrado da soma destes 2 números é: {resultado}")
elif opcao == "3":
    if num1<num2:
        resultado = num1**3 
        print(f"O Cubo do menor numero é {resultado}")
    else: 
        resultado = num2**3
        print(f"O Cubo do menor numero é {resultado}")
else: 
    print("Essa opção não existe")
