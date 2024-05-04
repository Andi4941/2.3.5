def realizar_compra():
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    while True:
        producto = input("Nombre del producto: ")
        cantidad = input("Cantidad: ")
        if producto.strip() and cantidad.strip():
            break
        else:
            print("Por favor, ingrese el nombre del producto y la cantidad.")
    confirmacion = input("¿Estás seguro que deseas pagar? (\"s\" o \"n\"): ")
    if nombre.strip() and telefono.strip() and confirmacion.lower() == "s":
        print("Compra realizada con éxito.")
    else:
        print("Faltan datos por ingresar. Por favor, vuelva a comenzar.")
        realizar_compra()

realizar_compra()