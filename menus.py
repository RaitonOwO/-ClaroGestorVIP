def menu_usuarios():
    print("╔══════════════════════════════════════════╗")
    print("║           MENU DE USUARIOS               ║")
    print("╠══════════════════════════════════════════╣")
    print("║ Bienvenido usuario                       ║")
    print("║ 1. Agregar usuario                       ║")
    print("║ 2. Eliminar usuario                      ║")
    print("║ 3. Editar usuario                        ║")
    print("║ 4. Asignar categoría al usuario          ║")
    print("║ 5. Mostrar los usuarios                  ║")
    print("║ 6. Salir                                 ║")
    print("╚══════════════════════════════════════════╝")


   
def menu_servicios():
    print("╔══════════════════════════════════════════╗")
    print("║           MENU DE SERVICIOS              ║")
    print("╠══════════════════════════════════════════╣")
    print("║ 1. Agregar plan pospago                  ║")
    print("║ 2. Agregar plan prepago                  ║")
    print("║ 3. Agregar plan de fibra óptica          ║")
    print("║ 4. Modificar un plan                     ║")
    print("║ 5. Eliminar servicio                     ║")
    print("║ 6. Salir                                 ║")
    print("╚══════════════════════════════════════════╝")


def menu_historiales():
    print("╔══════════════════════════════════════════╗")
    print("║          MENU DE HISTORIALES             ║")
    print("╠══════════════════════════════════════════╣")
    print("║ 1. Mostrar el historial de compras       ║")
    print("║ 2. Mostrar el historial de excepciones   ║")
    print("║ 3. Mostrar el historial de reclamaciones ║")
    print("║    y sugerencias                         ║")
    print("║ 4. Salir                                 ║")
    print("╚══════════════════════════════════════════╝")


def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("╭───────────────────────────────────────╮")
        print("│                                       │")
        print("│            ¡Opción ingresada!         │")
        print("│                                       │")
        print("╰───────────────────────────────────────╯")
        return opc
    except ValueError:
        print("╭───────────────────────────────────────╮")
        print("│                                       │")
        print("│      Error: ¡Ingrese un número!       │")
        print("│                                       │")
        print("╰───────────────────────────────────────╯")
        return -1

    
def menu_principal():
    print("╔══════════════════════════════════════════╗")
    print("║             MENU PRINCIPAL               ║")
    print("╠══════════════════════════════════════════╣")
    print("║ 1. Mostrar menú de usuarios              ║")
    print("║ 2. Mostrar menú de servicios             ║")
    print("║ 3. Mostrar menú de ventas                ║")
    print("║ 4. Mostrar menú de historiales           ║")
    print("║ 5. Agregar reclamo                       ║")
    print("║ 6. Agregar sugerencia                    ║")
    print("║ 7. Salir                                 ║")
    print("╚══════════════════════════════════════════╝")

def mensaje_claro():
    print("╔══════════════════════════════════════════════╗")
    print("║            ¡Bienvenido a Claro!              ║")
    print("╚══════════════════════════════════════════════╝")

    


def menu_ventas():
    print("╔════════════════════════════════════════╗")
    print("║             MENU DE VENTAS             ║")
    print("╠════════════════════════════════════════╣")
    print("║ 1. Comprar SmartPhone                  ║")
    print("║ 2. Comprar Televisor                   ║")
    print("║ 3. Comprar Audífonos                   ║")
    print("║ 4. Salir                               ║")
    print("╚════════════════════════════════════════╝")

   
   