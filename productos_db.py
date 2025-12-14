import sqlite3
def conectar():
    try:
        return sqlite3.connect("inventario.db")
    except:
        return None
def crear_tabla(conexion):      
    cursor = conexion.cursor()
    cursor.execute("""  
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)
    conexion.commit()

def cerrar_conexion(conexion):
    try:
        if conexion:
            conexion.close()
    except sqlite3.Error as e:
        print(f"Error al cerrar la conexión: {e}")

def insertar_producto_bd(conexion, nombre, descripcion, cantidad, precio, categoria):
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))
    conexion.commit()
def obtener_productos_bd(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    return cursor.fetchall()

def buscar_producto_id_bd(conexion, id_prod):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_prod,))
    return cursor.fetchone()

def actualizar_stock_bd(conexion, id_prod, nuevo_stock):
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE productos
        SET cantidad = ?
        WHERE id = ?
    """, (nuevo_stock, id_prod))
    conexion.commit()

def eliminar_producto_bd(conexion, id_prod):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
    conexion.commit()

def obtener_bajo_stock_bd(conexion, limite):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    return cursor.fetchall()



