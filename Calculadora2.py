num1 = int(input("Escolha o 1° Numero: "))
num2 = int(input("Escolha o 2° Numero: "))
menu = 1
while menu != 0:
    print("Menu")
    print("-"*30)
    print("""1 - Soma
2 - Subtração
3 - Divisão
4 - Multiplicação
0 - Encerra o programa""")
    print("-"*30)
    menu = int(input("Escolha um opção: "))
    if menu == 1:
        resultado = num1+num2
        print(f"A soma destes numeros é {resultado} ")
        input("Deseja continuar? Aperte Enter.")
    elif menu == 2:
        resultado = num1-num2
        print(f"A subtração destes numeros é {resultado}")
        input("Deseja continuar? Aperte Enter.")
    elif menu == 3:
        resultado = num1/num2
        print(f"A divisão destes numeros é {resultado}")
        input("Deseja continuar? Aperte Enter.")
    elif menu == 4:
        resultado = num1*num2
        print(f"A multiplicação destes numeros é {resultado}")
        input("Deseja continuar? Aperte Enter.")
    elif menu == 0:
        print("Programa encerrado.")
    else: print("Opção invalida")
