"""
Determinar si un número es primo.
"""

# Entradas
numero = int(input("Introduzca un número: "))

# Proceso
if numero == 1:
    primo = "no"
else:
    primo = "sí"
for divisor in range(2, numero):
    if numero % divisor == 0:
        primo = "no"
        break

# Salidas
print(f"El número {numero} {primo} es primo.")
