def registrar_usuario(datos):
    datos = dict(datos)
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el documento: ")
    usuario["cliente"]=input("Ingrese el tipo de cliente: ")
    usuario["telefono"]=input("Ingrese el numero de telefono: ")
    usuario["direccion"]=input("Ingrese la direccion: ")

    try:
        usuario["edad"] = int(input("Ingrese la edad: "))
    except Exception:
        usuario["edad"] = 0
    datos["usuarios"].append(usuario)
    print("Usuario registrado con éxito!")
    return datos


def eliminar_participante(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"].pop(i)
            print("usuario eliminado!")
            return datos
    print("Participante no existe")
    return datos


def editar_usuario(datos):
    datos = dict(datos)
    buscar_usuario = input("ingrese el documento del usuario: ")


    for usuarios in datos["usuarios"]:
        if usuarios["documento"] == buscar_usuario:
            print("Usuario encontrado!")
            nuevo_nombre = input("Nuevo nombre (Enter para dejar sin cambios): ")
            nuevo_documento = input("Nuevo documento (Enter para dejar sin cambios): ")
            nuevo_cliente = input("Nuevo tipo de cliente (Enter para dejar sin cambios): ")
            nuevo_edad = (input("Nueva edad (Enter para dejar sin cambios): "))
            if nuevo_nombre:
                usuarios["nombre"] = nuevo_nombre
            if nuevo_documento:
                usuarios["documento"] = nuevo_documento
            if nuevo_cliente:
                usuarios["cliente"] = nuevo_cliente
            if nuevo_edad:
                try:
                    usuarios["edad"] = int(nuevo_edad)
                except Exception:
                    print("La edad debe ser un numero entero.")
                print("Usuario editado con exito!")
                break
        else:
            print("Usuario no encontrado!")
    return datos
    
def categoria_usuario(datos):
    

            




