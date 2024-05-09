def registrar_usuario(datos):
    datos = dict(datos)
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el documento: ")
    usuario["cliente"]=input("Ingrese el tipo de cliente: ")
    try:
        usuario["edad"] = int(input("Ingrese la edad: "))
    except Exception:
        usuario["edad"] = 0
    datos["usuarios"].append(usuario)
    print("Usuario registrado con éxito!")
    return datos
