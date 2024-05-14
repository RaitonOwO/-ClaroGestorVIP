from utilidades import *
import json
from datetime import datetime

def mostar_historial_ventas(historial_ventas):
    for historial in historial_ventas["compras"]:
        print(historial)

def mostar_historial_rs(datos_historiales_reclamaciones):
    for historial in datos_historiales_reclamaciones["registros"]:
        print(historial)


def mostrar_historial_excepciones(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="latin-1") as file:
            historial = file.read()
        print(historial)
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe.")
    except Exception as e:
        print(f"Error al mostrar el historial de excepciones: {str(e)}")


def registrar_reclamacion_o_sugerencia(mensaje, tipo):
    try:
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        reclamacion_o_sugerencia = {
            "fecha": fecha_actual,
            "mensaje": mensaje,
            "tipo": tipo
        }
        
        nombre_archivo = "reclamaciones_sugerencias.json"
        try:
            with open(nombre_archivo, "r") as archivo:
                historial_rs = json.load(archivo)
        except FileNotFoundError:
            historial_rs = {"registros": []}

        historial_rs["registros"].append(reclamacion_o_sugerencia)
   
        with open(nombre_archivo, "w") as archivo:
            json.dump(historial_rs, archivo, indent=4)

        print("La reclamación o sugerencia se ha registrado correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al registrar la reclamación o sugerencia: {str(e)}")







        
