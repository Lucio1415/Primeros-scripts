import json
import os

# Nombre del archivo donde se guardarán los datos
ARCHIVO_DATOS = "base_datos.json"

def cargar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r") as f:
            return json.load(f)
    return {}

def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w") as f:
        json.dump(datos, f, indent=4)

def menu():
    inventario = cargar_datos()
    
    while True:
        print("\n--- SISTEMA DE GESTIÓN PROFESIONAL ---")
        print("1. Ver Inventario")
        print("2. Agregar/Actualizar Producto")
        print("3. Registrar Venta")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\nID | Producto | Stock | Precio")
            for id, info in inventario.items():
                print(f"{id} | {info['nombre']} | {info['stock']} | {info['precio']} DH")
        
        elif opcion == "2":
            id = input("ID o Código de barras: ")
            nombre = input("Nombre del producto: ")
            stock = int(input("Cantidad inicial: "))
            precio = float(input("Precio de venta (DH): "))
            inventario[id] = {"nombre": nombre, "stock": stock, "precio": precio}
            guardar_datos(inventario)
            print("¡Producto guardado!")

        elif opcion == "3":
            id = input("Ingrese ID del producto vendido: ")
            if id in inventario:
                cant = int(input(f"Cantidad vendida (Disponible: {inventario[id]['stock']}): "))
                if cant <= inventario[id]['stock']:
                    inventario[id]['stock'] -= cant
                    guardar_datos(inventario)
                    total = cant * inventario[id]['precio']
                    print(f"Venta registrada. Total: {total} DH")
                else:
                    print("Error: Stock insuficiente.")
            else:
                print("Error: Producto no encontrado.")
        
        elif opcion == "4":
            print("Cerrando sistema...")
            break

if __name__ == "__main__":
    menu()
