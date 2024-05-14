from modulo_historiales import guardar_excepcion

def validar_documento(documento):
    if len(documento) > 10:
        print("Error: El documento no puede tener más de 10 dígitos.")
        return False
    elif not documento.isdigit():
        print("Error: El documento debe contener solo números.")
        return False
    return True

def registrar_usuario(datos):
    datos = dict(datos)
    usuario = {}
    usuario["nombre"] = input("Ingrese el nombre: ")
    
    while True:
        documento = input("Ingrese el documento: ")
        if validar_documento(documento):
            usuario["documento"] = documento
            break
    
    usuario["cliente"] = input("Ingrese el tipo de cliente: ")
    usuario["telefono"] = input("Ingrese el numero de telefono: ")
    usuario["direccion"] = input("Ingrese la direccion: ")
    usuario["servicio_contratado"] = ""
    
    try:
        usuario["edad"] = int(input("Ingrese la edad: "))
    except ValueError as ve:
        print("Error: Ingrese una edad válida.")
        guardar_excepcion(ve)
        usuario["edad"] = 0
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        return datos
    
    for documento_en_uso in datos["usuarios"]:
        if documento_en_uso["documento"] == usuario["documento"]:
            print("Error: El documento ya está en uso.")
            return datos
    
    datos["usuarios"].append(usuario)
    print("Usuario registrado con éxito!")
    return datos





def eliminar_participante(datos):
    datos = dict(datos)
    try:
        documento = input("Ingrese el documento del usuario: ")
        if not validar_documento(documento):
            return datos
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        guardar_excepcion("Operación interrumpida por el usuario")
        return datos
    
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"].pop(i)
            print("Usuario eliminado!")
            return datos
    
    print("Participante no existe")
    return datos


def editar_usuario(datos):
    datos = dict(datos)
    buscar_usuario = input("Ingrese el documento del usuario: ")

    try:
        for usuario in datos["usuarios"]:
            if usuario["documento"] == buscar_usuario:
                print("Usuario encontrado!")
                nuevo_nombre = input("Nuevo nombre (Enter para dejar sin cambios): ")
                nuevo_documento = input("Nuevo documento (Enter para dejar sin cambios): ")
                nuevo_cliente = input("Nuevo tipo de cliente (Enter para dejar sin cambios): ")
                nuevo_edad = input("Nueva edad (Enter para dejar sin cambios): ")

                if nuevo_documento and validar_documento(nuevo_documento):
                    usuario["documento"] = nuevo_documento
                if nuevo_nombre:
                    usuario["nombre"] = nuevo_nombre
                if nuevo_cliente:
                    usuario["cliente"] = nuevo_cliente
                if nuevo_edad:
                    try:
                        usuario["edad"] = int(nuevo_edad)
                    except ValueError:
                        print("Error: La edad debe ser un número entero.")
                print("Usuario editado con éxito!")
                break
        else:
            print("Usuario no encontrado!")
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        guardar_excepcion("Operación interrumpida por el usuario")
        return datos
    
    return datos
    
def asignar_categoria_usuario(datos):
    datos = dict(datos)
    try:
        buscar_usuario = input("Ingrese el documento del usuario: ")
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        guardar_excepcion("Operación interrumpida por el usuario")
        return datos

    for usuario in datos["usuarios"]:
        if usuario["documento"] == buscar_usuario:
            print("Usuario encontrado!")
            nueva_categoria = input("Ingrese el tipo de cliente: ")
            if nueva_categoria:
                usuario["cliente"] = nueva_categoria
                print("Categoría actualizada!")
            else:
                print("No se ha asignado ninguna categoría.")
            break
    else:
        print("Usuario no encontrado!")
        return datos

    if not validar_documento(buscar_usuario):
        return datos
    
    return datos
def mostar_usuarios(datos):
    datos = dict(datos)
    for i in datos["usuarios"]:
        print (i)
