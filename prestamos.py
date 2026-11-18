# SISTEMA DE PRESTAMO DE COMPUTADORES

computadores = []
prestamos = []


# 1. Registrar computador
def registrar_computador():
    codigo = input("Codigo del computador: ").strip().upper()

    if not codigo:
        print("El codigo es obligatorio.")
        return

    for equipo in computadores:
        if equipo["codigo"] == codigo:
            print("El computador ya existe.")
            return

    computadores.append({
        "codigo": codigo,
        "estado": "Disponible"
    })

    print("Computador registrado correctamente.")


# 2. Consultar computadores
def consultar_computadores():
    if len(computadores) == 0:
        print("No hay computadores registrados.")
        return

    for equipo in computadores:
        print(equipo["codigo"], "-", equipo["estado"])


# 3. Registrar prestamo
def prestar_computador():
    codigo = input("Codigo del computador: ").strip().upper()

    for equipo in computadores:
        if equipo["codigo"] == codigo:

            if equipo["estado"] == "Prestado":
                print("El computador ya esta prestado.")
                return

            nombre = input("Nombre del aprendiz: ").strip()
            documento = input("Documento: ").strip()
            fecha = input("Fecha de devolucion (AAAA-MM-DD): ").strip()

            if not nombre or not documento or not fecha:
                print("Todos los datos son obligatorios.")
                return

            equipo["estado"] = "Prestado"

            prestamos.append({
                "codigo": codigo,
                "nombre": nombre,
                "documento": documento,
                "fecha": fecha,
                "estado": "Pendiente"
            })

            print("Prestamo registrado correctamente.")
            return

    print("Computador no encontrado.")


# 4. Registrar devolucion
def devolver_computador():
    codigo = input("Codigo del computador: ").strip().upper()

    for equipo in computadores:
        if equipo["codigo"] == codigo:

            if equipo["estado"] == "Disponible":
                print("El computador ya esta disponible.")
                return

            equipo["estado"] = "Disponible"

            for prestamo in prestamos:
                if (prestamo["codigo"] == codigo
                        and prestamo["estado"] == "Pendiente"):
                    prestamo["estado"] = "Devuelto"
                    break

            print("Devolucion registrada correctamente.")
            return

    print("Computador no encontrado.")


# 5. Consultar prestamos pendientes
def consultar_prestamos():
    pendientes = 0

    for prestamo in prestamos:
        if prestamo["estado"] == "Pendiente":
            print("-------------------------")
            print("Computador:", prestamo["codigo"])
            print("Aprendiz:", prestamo["nombre"])
            print("Documento:", prestamo["documento"])
            print("Fecha devolucion:", prestamo["fecha"])
            print("Estado:", prestamo["estado"])
            pendientes += 1

    if pendientes == 0:
        print("No hay prestamos pendientes.")


# 6. Menu principal
while True:
    print("\n===== PRESTAMO DE COMPUTADORES =====")
    print("1. Registrar computador")
    print("2. Consultar computadores")
    print("3. Prestar computador")
    print("4. Devolver computador")
    print("5. Consultar prestamos pendientes")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        registrar_computador()
    elif opcion == "2":
        consultar_computadores()
    elif opcion == "3":
        prestar_computador()
    elif opcion == "4":
        devolver_computador()
    elif opcion == "5":
        consultar_prestamos()
    elif opcion == "6":
        print("Gracias por utilizar el sistema.")
        break
    else:
        print("Opcion incorrecta.")
