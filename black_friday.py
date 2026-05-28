valor = float(input("Dígite o valor total da compra:"))
desconto = 1
while desconto != 0:
    print("Descontos")
    print("""      1 - A vista (15% de desconto)
      2- Cartão de Débito (10% de desconto)
      3- Cartão de Crédito (5% de desconto)
      0- Encerrar o programa.""")
    desconto = int(input("Dígite qual opção deseja: "))
    if desconto == 1: 
        print(f"O valor final a vista foi de {valor-(valor*0.15):.2f}")
        input("Deseja continuar? Aperte Enter.")
    elif desconto == 2: 
        print(f"O valor final no cartão de débito foi de {valor-(valor*0.10):.2f}")
        input("Deseja continuar? Aperte Enter.")
    elif desconto == 3: 
        print(f"O valor final no cartão de crédito foi de {valor-(valor*0.05):.2f}")
        input("Deseja continuar? Aperte Enter.")
    elif desconto == 0: print("Encerrando o programa.")
    else: print("Não temos esta opção de pagamento disponivel")
