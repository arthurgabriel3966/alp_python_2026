num1 = float(input("Dígite seu 1° numero: "))
num2 = float(input("Dígite seu 2° numero: "))
print("Menu")
print("""      1 - Média ponderada, com pesos 2 e 3
      2 - Quadrado da soma dos 2 números
      3 - Cubo do menor número""")
opcao = input("Escolha uma opção: ")
if opcao == "1": print(f"A média ponderada destes números é {((num1*2)+(num2*3))/(2+3)}")
elif opcao == "2": print(f"O quadrado da soma destes 2 números é: {(num1+num2)**2}")
elif opcao == "3":
    if num1<num2: print(f"O Cubo do menor numero é {num1**3}")
    else: print(f"O Cubo do menor numero é {num2**3}")
else: print("Essa opção não existe")
