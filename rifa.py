import random
print("-"*50)
print("Rifa do Alemão")
print("Dígite encerrar para finalizar a rifa")
print("-"*50)
participantes = []
while True:
    pessoas = str(input("Dígite o nome do comprador: "))
    if pessoas.lower() == "encerrar":
        break
    participantes.append(pessoas)
vencedor = random.choice(participantes)
print("Encerrando a Rifa")
print(f"O vencedor da rifa é {vencedor}")
