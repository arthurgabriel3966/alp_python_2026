usuarios = {}
print("Dígite encerrar no usuario ou na senha para finalizar.")
while True:
    cadastro_usuário = input("Cadastre seu usuário: ")
    if cadastro_usuário.lower() == "encerrar":
        break
    cadastro_senha = input("Cadastre sua senha: ")
    if cadastro_senha.lower() == "encerrar":
        break
    usuarios[cadastro_usuário] = cadastro_senha
    print("Cadastro feito")

login_usuário = input("Dígite seu usuário: ")
login_senha = input("Dígite sua sehna: ")

if login_usuário in usuarios:
    if login_senha == usuarios[login_usuário]:
        print(f"Bem vindo(a) {login_usuário}")
    else:
        print("Senha errada")
else:
    print("Usuário invalido")
