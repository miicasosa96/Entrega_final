def validar_numero(valor):
    while not valor.isdigit():
        print("Ingrese un número válido.")
        valor = input("Reingrese: ").strip()
    return int(valor)

def validar_float(valor):
    while True:
        try:
            return float(valor)
        except:
            valor = input("Ingrese un valor numérico válido: ") 

def validar_texto(valor):
    while valor.strip() == "":
        print("No puede ser vacío.")
        valor = input("Reingrese: ").strip()
    return valor

def agregar_producto(conexion):
    print("\n--- ALTA PRODUCTO ---")
    nombre = validar_texto(input("Nombre: "))
    descripcion = input("Descripción: ")
    cantidad = validar_numero(input("Cantidad: "))
    precio = validar_float(input("Precio: "))
    categoria = input("Categoría: ")

    insertar_producto_bd(conexion, nombre, descripcion, cantidad, precio, categoria)    
def listar_productos(conexion):
    productos = obtener_productos_bd(conexion)
    if not productos:
        print("No hay productos cargados.")
        return

    print("\n--- LISTADO ---")
    for p in productos:
        print(f"ID:{p[0]} | {p[1]} | Cant:{p[3]} | ${p[4]} | {p[5]}")   

def buscar_producto(conexion):
    id_buscar = validar_numero(input("ID a buscar: "))
    producto = buscar_producto_id_bd(conexion, id_buscar)

    if producto:
        print(f"✔ Encontrado: {producto}")
    else:
        print("❌ No existe un producto con ese ID.")

def actualizar_stock(conexion):
    id_prod = validar_numero(input("ID a actualizar: "))
    nuevo_stock = validar_numero(input("Nuevo stock: "))
    actualizar_stock_bd(conexion, id_prod, nuevo_stock)

def eliminar_producto(conexion):
    id_prod = validar_numero(input("ID a eliminar: "))
    eliminar_producto_bd(conexion, id_prod)

def reporte_bajo_stock(conexion):
    limite = validar_numero(input("Límite de stock: "))
    productos = obtener_bajo_stock_bd(conexion, limite)

    if not productos:
        print("No hay productos bajo el stock especificado.")
        return

    print("\n--- PRODUCTOS BAJO STOCK ---")
    for p in productos:
        print(f"ID:{p[0]} | {p[1]} | Cant:{p[3]} | ${p[4]} | {p[5]}")



