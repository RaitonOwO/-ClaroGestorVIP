#imports
from datos import *
from menus import *
from modulo_usuarios import *

#constantes
RUTA_USUARIOS = "usuarios.json"
RUTA_SERVICIOS = "servicios.json"

datos = cargar_datos(RUTA_USUARIOS)

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
        menu_planes()
        opc = pedir_opcion()
        if opc == 1:
            print("opcion 1")
        elif opc == 2:
            print("opcion 2")
        elif opc == 3:
            print("opcion 3")
        elif opc == 4:
            print("opcion 4")
        elif opc == 5:
            print("Saliendo...")
            break

    elif opc == 4:
        print("Saliendo...")
        break


