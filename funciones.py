# def imprimir_mensaje():
#     print ("Mensaje especial: ")
#     print ("¡Estoy aprendiendo a usar funciones!")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# print ("Mensaje especial: ")
# print ("¡Estoy aprendiendo a usar funciones!")
# print ("Mensaje especial: ")
# print ("¡Estoy aprendiendo a usar funciones!")
def conversacion(mensaje):
    print('Hola')
    print("Cómo estás")
    print(mensaje)
    print("Adios")

opcion = int(input("Elige una opción (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opción 1")
elif opcion == 2:
    conversacion("Elegiste la opción 2")
elif opcion == 3:
    conversacion("Elegiste la opción 3")
else:
    print("Escribe la opción correcta")
