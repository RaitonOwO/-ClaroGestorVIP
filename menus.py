def menu_usuarios():
    print("***********************")
    print("Bienvenido usuario")
    print("1.Para agregar usuario")
    print("2.Para eliminar usuario")
    print("3.Para editar usuario")
    print("4.Para asignar categoria al usuario")
    print("5.Para mostrar los usuarios")
<<<<<<< HEAD
    print("6.Para salir")
=======
>>>>>>> da771b6b39fe1380b8e3229fb60b5ad72f643db5
   
def menu_planes():
    print("1.Para agregar plan pospago")
    print("2.Para agregar plan prepago")
    print("3.Para agregar plan de fibra optica")
    print("4.Para modificar un plan")
<<<<<<< HEAD
    print("5.Para salir")
=======
>>>>>>> da771b6b39fe1380b8e3229fb60b5ad72f643db5

def menu_historiales():
    print("1.Para mostar el historial de compras")
    print("2.Para mostar el historial de excepciones")
    print("3.Para mostrar el historial de reclamaciones y sugerencias")
<<<<<<< HEAD
    print("4.Para salir")
=======
>>>>>>> da771b6b39fe1380b8e3229fb60b5ad72f643db5

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
<<<<<<< HEAD
    print("4.Para Salir")
=======
>>>>>>> da771b6b39fe1380b8e3229fb60b5ad72f643db5
   