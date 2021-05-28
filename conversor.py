pesos = input("¿Cuántos pesos chilenos tienes?: ")
pesos = float(pesos)
valor_dolar = 733
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")