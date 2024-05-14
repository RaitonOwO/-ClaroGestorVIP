#imports
from datos import *
from menus import *
from modulo_usuarios import *
from modulo_servicios import *
from modulo_ventas import *
from modulo_historiales import *
from modulo_reclamaciones_sugerencias import *
from utilidades import *
#constantes
RUTA_USUARIOS = "usuarios.json"
RUTA_SERVICIOS = "servicios.json"
RUTA_PRODUCTOS = "productos_tienda.json"
RUTA_HISTORIALES = "historial_ventas.json"
RUTA_HISTORIALES_RECLAMACIONES = "reclamaciones_sugerencias.json"
RUTA_HISTORIAL_EXCEPCIONES = "excepciones.txt"
#cargar datos
datos = cargar_datos(RUTA_USUARIOS)
datos_productos = cargar_datos(RUTA_PRODUCTOS)
datos_historiales = cargar_datos(RUTA_HISTORIALES)
datos_historiales_reclamaciones = cargar_datos(RUTA_HISTORIALES_RECLAMACIONES)
mostrar_historial_excepciones(RUTA_HISTORIAL_EXCEPCIONES)
opc = 0

while True:
    menu_principal()
    opc = pedir_opcion()
    if opc == 1:
        menu_usuarios()
        opc = pedir_opcion()
        if opc == 1:
            datos = registrar_usuario(datos)
        elif opc == 2:
            datos = eliminar_participante(datos)
        elif opc == 3:
            datos = editar_usuario(datos)
        elif opc == 4:
            datos = asignar_categoria_usuario(datos)
        elif opc == 5:
            mostar_usuarios(datos)
        elif opc == 6:
            print("Saliendo...")
            break
        guardar_datos(datos,RUTA_USUARIOS)
    elif opc == 2:
        menu_servicios()
        opc = pedir_opcion()
        if opc == 1:
            datos = agregar_plan_pospago(datos)
        elif opc == 2:
            datos = agregar_plan_prepago(datos)
        elif opc == 3:
            datos = agregar_plan_fribra_optica(datos)
        elif opc == 4:
            datos = modificar_servicio(datos)
        elif opc == 5:
            datos = eliminar_servicio(datos)
        elif opc == 6:
            print("Saliendo...")
            break
        guardar_datos(datos,RUTA_SERVICIOS)
    elif opc == 3:
        menu_ventas()
        opc = pedir_opcion()
        if opc == 1:
            comprar_telefono(datos_productos)
        elif opc == 2:
            comprar_televisor(datos_productos)
        elif opc == 3:
            comprar_audifonos(datos_productos)
        elif opc == 4:
            print("Saliendo...")
            break
        guardar_datos(datos_productos,RUTA_PRODUCTOS)
    elif opc == 4:
        menu_historiales()
        opc = pedir_opcion()
        if opc == 1:
            mostar_historial_ventas(datos_historiales)
        elif opc == 2:
            mostrar_historial_excepciones(RUTA_HISTORIAL_EXCEPCIONES)  # Utilizamos la función aquí
        elif opc == 3:
            mostar_historial_rs(datos_historiales_reclamaciones)
        elif opc == 4:
            print("Saliendo...")
            break
        guardar_datos(datos_historiales,RUTA_HISTORIALES)
    elif opc == 5:
        agregar_reclamacion()
    elif opc == 6:
        agregar_sugerencia()
    elif opc == 7:
        print("Saliendo...")
        break
        
        


