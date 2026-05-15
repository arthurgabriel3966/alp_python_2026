contador = 3
usuario = input("Digite seu usúario: ")
senha = input("Digite sua senha: ")
while (senha != "12345" or usuario != "aluno") and contador > 1:
    contador -= 1
    print(f"Usúario ou senha invalida! Tente novamente. ({contador} tentativas restantes.)")
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

if senha == "12345" and usuario == "aluno":
    print(f"Bem vindo {usuario}!")
else: print("Conta Bloqueada")
