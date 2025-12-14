from productos import *
from productos_db import *
from colorama import Fore, Style, init



init(autoreset=True)
def menu():
    print(Fore.CYAN + "="*60)
    print("          🛒 GESTIÓN DE PRODUCTOS - SOLUCIÓN FINAL     ")
    print("="*60)

    print(Fore.GREEN + "[1] ➕ Agregar Producto")
    print("[2] 📋 Listar Productos")
    print("[3] 🔍 Buscar Producto")
    print("[4] ✏ Actualizar Stock")
    print("[5] ❌ Eliminar Producto")
    print("[6] ⚠ Reporte Bajo Stock\n")

    print(Fore.YELLOW + "[7] 🔚 Salir")
    
def main():
    conexion = conectar()
    crear_tabla(conexion)

    while True:
        menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            agregar_producto(conexion)
        elif opcion == "2":
            listar_productos(conexion)
        elif opcion == "3":
            buscar_producto(conexion)
        elif opcion == "4":
            actualizar_stock(conexion)
        elif opcion == "5":
            eliminar_producto(conexion)
        elif opcion == "6":
            reporte_bajo_stock(conexion)
        elif opcion == "7":
            print("Fin del programa. 👋")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
