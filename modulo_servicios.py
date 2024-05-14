from modulo_usuarios import validar_documento
from modulo_historiales import guardar_excepcion

def agregar_plan_pospago(datos):
    datos = dict(datos)
    try:
        buscar_usuario = input("Ingrese el documento del usuario: ")
        if not validar_documento(buscar_usuario):
            return datos
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        guardar_excepcion("Operación interrumpida por el usuario")
        return datos
    
    usuario_encontrado = False  

    for usuario in datos["usuarios"]:
        if usuario["documento"] == buscar_usuario:
            print("Usuario encontrado!")
            servicio = input("Ingrese el servicio que quieres contratar: ")
            if servicio:
                usuario["servicio_contratado"] = servicio
                print("Su servicio ha sido contratado con éxito!")
                usuario_encontrado = True  
            break  
    
    if not usuario_encontrado:
        print("Usuario no encontrado")
    
    return datos

def agregar_plan_prepago(datos):
    datos = dict(datos)
    try:
        buscar_usuario = input("Ingrese el documento del usuario: ")
        if not validar_documento(buscar_usuario):
            return datos
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        guardar_excepcion("Operación interrumpida por el usuario")
        return datos
    
    usuario_encontrado = False  

    for usuario in datos["usuarios"]:
        if usuario["documento"] == buscar_usuario:
            print("Usuario encontrado!")
            servicio = input("Ingrese el servicio que quieres contratar: ")
            if servicio:
                usuario["servicio_contratado"] = servicio
                print("Su servicio ha sido contratado con éxito!")
                usuario_encontrado = True  
            break  
    
    if not usuario_encontrado:
        print("Usuario no encontrado")

    return datos

def agregar_plan_fribra_optica(datos):
    datos = dict(datos)
    try:
        buscar_usuario = input("Ingrese el documento del usuario: ")
        if not validar_documento(buscar_usuario):
            return datos
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        guardar_excepcion("Operación interrumpida por el usuario")
        return datos
    
    usuario_encontrado = False  

    for usuario in datos["usuarios"]:
        if usuario["documento"] == buscar_usuario:
            print("Usuario encontrado!")
            servicio = input("Ingrese el servicio que quieres contratar: ")
            if servicio:
                usuario["servicio_contratado"] = servicio
                print("Su servicio ha sido contratado con éxito!")
                usuario_encontrado = True  
            break  
    
    if not usuario_encontrado:
        print("Usuario no encontrado")
    
    return datos

def modificar_servicio(datos):
    datos = dict(datos)
    try:
        buscar_usuario = input("Ingrese el documento del usuario: ")
        if not validar_documento(buscar_usuario):
            return datos
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        guardar_excepcion("Operación interrumpida por el usuario")
        return datos
    
    usuario_encontrado = False  

    for usuario in datos["usuarios"]:
        if usuario["documento"] == buscar_usuario:
            print("Usuario encontrado!")
            servicio = input("Ingrese el nuevo servicio que quieres contratar: ")
            if servicio:
                usuario["servicio_contratado"] = servicio
                print("Su servicio ha sido modificado con éxito!")
                usuario_encontrado = True  
            break  
    
    if not usuario_encontrado:
        print("Usuario no encontrado")
    
    return datos


def eliminar_servicio(datos):
    datos = dict(datos)
    try:
        buscar_usuario = input("Ingrese el documento del usuario: ")
        if not validar_documento(buscar_usuario):
            return datos
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        guardar_excepcion("Operación interrumpida por el usuario")
        return datos

    for usuario in datos["usuarios"]:
        if usuario["documento"] == buscar_usuario:
            print("Usuario encontrado!")
            if "servicio_contratado" in usuario:
                del usuario["servicio_contratado"]
                print("Servicio eliminado con éxito!")
            else:
                print("El usuario no tiene ningún servicio contratado.")
            break
    else:
        print("Usuario no encontrado")
    
    return datos



                
        
        
