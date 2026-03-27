a = int(input(f"Dígite o valor de A: "))
b = int(input(f"Dígite o valor de B: "))
c = int(input(f"Dígite o valor de C: "))
delta = (b**2) - 4*a*c
raiz_delta = delta**0.5
x1 = (-b+raiz_delta)/(2*a)
x2 = (-b-raiz_delta)/(2*a)
print()