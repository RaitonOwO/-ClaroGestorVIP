import json

def cargar_datos(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="latin-1") as file:
            datos = json.load(file)
        return datos
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe.")
        return None
    except Exception as e:
        print(f"Error al cargar datos desde {ruta_archivo}: {str(e)}")
        return None

def guardar_datos(datos, archivo):
    datos = dict(datos)
    
    diccionario=json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()
    

def cargar_datos_txt(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="latin-1") as file:
            datos = file.read()
        return datos
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe.")
        return None
    except Exception as e:
        print(f"Error al cargar datos desde {ruta_archivo}: {str(e)}")
        return None