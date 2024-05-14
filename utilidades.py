import json
from datetime import datetime

def guardar_excepcion(excepcion):
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("excepciones.txt", "a") as file:
        file.write(f"[{fecha_actual}] {str(excepcion)}\n")


def registrar_venta(referencia_producto, cantidad):
    try:
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        venta = {
            "fecha": fecha_actual,
            "historial": f"Se han comprado {cantidad} unidades del producto {referencia_producto}."
        }
        nombre_archivo = "historial_ventas.json"
        try:
            with open(nombre_archivo, "r") as archivo:
                historial_ventas = json.load(archivo)
        except FileNotFoundError:
            historial_ventas = {"compras": []}
        
        historial_ventas["compras"].append(venta)
        
        with open(nombre_archivo, "w") as archivo:
            json.dump(historial_ventas, archivo, indent=4)

        print("La venta se ha registrado correctamente en el historial de ventas.")
    except Exception as e:
        print(f"Ocurrió un error al registrar la venta: {str(e)}")
