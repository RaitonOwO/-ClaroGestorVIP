def menu_usuarios():
    print("***********************")
    print("Bienvenido usuario")
    print("1.Para agregar usuario")
    print("2.Para eliminar usuario")
    print("3.Para editar usuario")
    print("4.Para asignar categoria al usuario")
    print("5.Para mostrar los usuarios")
    print("6.Para salir")

   
def menu_planes():
    print("1.Para agregar plan pospago")
    print("2.Para agregar plan prepago")
    print("3.Para agregar plan de fibra optica")
    print("4.Para modificar un plan")
    print("5.eliminar servicio")
    print("6.Para salir")

def menu_historiales():
    print("1.Para mostar el historial de compras")
    print("2.Para mostar el historial de excepciones")
    print("3.Para mostrar el historial de reclamaciones y sugerencias")
    print("4.Para salir")

def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("***************************************")
        return opc
    except Exception:
        print("Valor inválido")
        print("***************************************")
        return -1
    
def menu_principal():
    print("1.Para mostrar menu de usuarios")
    print("2.Para mostar menu de ventas")
    print("3.Para mostrar menu de historiales")
    print("4.Para Salir")
   