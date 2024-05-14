import json
from datetime import datetime
from utilidades import *

def comprar_telefono(datos_productos):
    print(datos_productos) 
    referencia = input("Ingrese la referencia del producto que desea comprar: ")
    try:
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
    except ValueError as ve:
        print("Error: Ingrese un número entero válido para la cantidad.")
        guardar_excepcion(ve)
        return datos_productos
    except KeyboardInterrupt:
        print ("Operación interrumpida por el usuario")
        return datos_productos
    historial = f"Se han comprado {cantidad} unidades del producto {referencia}."
    for producto in datos_productos["productos"]:
        if producto["referencia"] == referencia:
            if producto["stock"] >= cantidad:
                producto["stock"] -= cantidad
                print(f"Se han comprado {cantidad} unidades del producto {referencia}.")
                registrar_venta(referencia,cantidad)
            else:
                print("No hay suficiente stock disponible para realizar esta compra.")
            break
    else:
        print("El producto no se encontró en la lista.")
    return datos_productos


def comprar_televisor(datos_productos):
    print(datos_productos) 
    referencia = input("Ingrese la referencia del producto que desea comprar: ")
    try:
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
    except ValueError as ve:
        print("Error: Ingrese un número entero válido para la cantidad.")
        guardar_excepcion(ve)
        return datos_productos
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        return datos_productos
    for producto in datos_productos["productos"]:
        if producto["referencia"] == referencia:
            if producto["stock"] >= cantidad:
                producto["stock"] -= cantidad
                print(f"Se han comprado {cantidad} unidades del producto {referencia}.")
                registrar_venta(referencia, cantidad)
            else:
                print("No hay suficiente stock disponible para realizar esta compra.")
            break
    else:
        print("El producto no se encontró en la lista.")
    return datos_productos

def comprar_audifonos(datos_productos):
    print(datos_productos) 
    referencia = input("Ingrese la referencia del producto que desea comprar: ")
    try:
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
    except ValueError as ve:
        print("Error: Ingrese un número entero válido para la cantidad.")
        guardar_excepcion(ve)
        return datos_productos
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        return datos_productos
    for producto in datos_productos["productos"]:
        if producto["referencia"] == referencia:
            if producto["stock"] >= cantidad:
                producto["stock"] -= cantidad
                print(f"Se han comprado {cantidad} unidades del producto {referencia}.")
                registrar_venta(referencia, cantidad)
            else:
                print("No hay suficiente stock disponible para realizar esta compra.")
            break
    else:
        print("El producto no se encontró en la lista.")
    return datos_productos
