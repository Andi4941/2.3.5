# Definir un diccionario de pizzas con los precios
pizzas = {
    "Pepperoni": 8.99,
    "Margarita": 7.99,
    "Hawaiana": 9.99,
    "Vegetariana": 7.99,
    "Mexicana": 9.99
}

def calcular_costo_pedido(pedido):
    neto = sum(pizzas[pizza] for pizza in pedido)
    impuesto = neto * 0.1  # Suponiendo un impuesto del 10%
    total = neto + impuesto
    return neto, impuesto, total

def mostrar_detalle_pedido(pedido, neto, impuesto, total):
    print("Detalle del pedido:")
    for pizza in pedido:
        print(f"{pizza}: ${pizzas[pizza]}")
    print(f"Neto: ${neto:.2f}")
    print(f"Impuesto: ${impuesto:.2f}")
    print(f"Total: ${total:.2f}")

def main():
    # Ejemplo de pedido
    pedido = ["Pepperoni", "Margarita", "Hawaiana"]

    # Calcular costo del pedido
    neto, impuesto, total = calcular_costo_pedido(pedido)

    # Mostrar detalle del pedido
    mostrar_detalle_pedido(pedido, neto, impuesto, total)

if __name__ == "__main__":
    main()