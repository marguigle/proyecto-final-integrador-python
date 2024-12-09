import sqlite3 as sql

conn = sql.connect("inventario")
conn.commit()
conn.close()


def crear_tabla():
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        precio REAL NOT NULL,
        cantidad INTEGER NOT NULL,
        categoria TEXT
    )
    """
    )
    conn.commit()
    conn.close()


import sqlite3

# Conexión a la base de datos (debería estar fuera de la función si se usa en varias funciones)
conn = sqlite3.connect("inventario")


import sqlite3

# Conexión global a la base de datos
conn = sqlite3.connect("inventario")


# def insertar_producto():
#     try:
#         nombre = input("Ingrese el nombre del producto: ")
#         descripcion = input("Ingrese la descripción del producto: ")
#         precio = float(input("Ingrese el precio del producto: "))
#         cantidad = int(input("Ingrese la cantidad del producto: "))
#         categoria = input(
#             "Ingrese la categoría del producto (ropa de hombre, ropa de mujer, ropa de niño, calzado): "
#         )

#         # Crear cursor
#         cursor = conn.cursor()

#         # Consulta parametrizada para evitar inyección SQL
#         cursor.execute(
#             """
#             INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria)
#             VALUES (?, ?, ?, ?, ?)
#             """,
#             (nombre, descripcion, precio, cantidad, categoria),
#         )

#         # Confirmar cambios
#         conn.commit()
#         print(f"el producto {nombre} se ha agregado al stock correctamente !!!")
#     except sqlite3.Error as e:
#         print(f"Error al insertar el producto: {e}")
#     except ValueError as ve:
#         print(f"Error en los datos ingresados: {ve}")


# # Llamar a la función
# # ñ
# insertar_producto()

# # Cerrar la conexión solo al final del programa
# conn.close()


if __name__ == "__main__":
    pass
