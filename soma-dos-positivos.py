resultado = 0
num = 1
maior = 0
cont = 0
while num >= 0: 
    num = int(input(f"Dígite seu numero: "))
    if num >= 0:
        resultado += num
        cont += 1
    if num > maior:
        maior = num
print (f"A soma destes números positivos é {resultado}")
print (f"A média aritmética é ({resultado / cont}) ")
print (f"O maior desses numeros é {maior}")
