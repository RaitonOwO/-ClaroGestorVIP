import json
from datetime import datetime
from modulo_historiales import registrar_reclamacion_o_sugerencia

def agregar_reclamacion():
    mensaje = input("Por favor, ingresa tu reclamación: ")
    registrar_reclamacion_o_sugerencia(mensaje, "reclamacion")

def agregar_sugerencia():
    mensaje = input("Por favor, ingrese su sugerencia: ")
    registrar_reclamacion_o_sugerencia(mensaje,"sugerencia")