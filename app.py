# from database import *
# from tabulate import tabulate
from funciones import *

# #### menu principal
# def menu_principal():
#     print(
#         """        #######################################
#                 GESTION DE STOCK
#         #######################################\n"""
#     )
#     print("Elija una opcion")
#     print("opcion 1: Agregar un producto")
#     print("opcion 2: Ver lista completa de productos")
#     print("opcion 3: Eliminar un producto de la lista")
#     print("opcion 4: Buscar un producto especifico de la lista")
#     print("opcion 5: Actualizar un producto")
#     print("opcion 6: mostrar stock de un  producto")
#     print("opcion 7: detectar stock bajo (menos de 10 unidades)")
#     print("opcion 8: Salir del menú\n")


# ####  buscar producto
# def buscar_un_producto():
#     try:
#         criterio = (
#             input(
#                 "¿Desea buscar el producto por 'ID' o por 'Nombre'? (Escriba 'ID' o 'Nombre'): "
#             )
#             .strip()
#             .lower()
#         )

#         if criterio == "nombre":
#             # Pedir el nombre del producto al usuario
#             nombre_producto = input(
#                 "Ingrese el nombre del producto que desea buscar: "
#             ).lower()

#             # Crear cursor
#             cursor = conn.cursor()

#             # Consulta parametrizada para evitar inyección SQL
#             cursor.execute(
#                 """
#             SELECT id, nombre, descripcion, precio, cantidad, categoria
#             FROM productos
#             WHERE LOWER(nombre) LIKE ?
#             """,
#                 (f"%{nombre_producto}%",),
#             )

#             # Obtener el producto encontrado
#             producto_encontrado = (
#                 cursor.fetchone()
#             )  # fetchone() para un único resultado

#             if producto_encontrado:
#                 print("\nProducto encontrado:")
#                 print(f"ID: {producto_encontrado[0]}")
#                 print(f"Nombre: {producto_encontrado[1]}")
#                 print(f"Descripción: {producto_encontrado[2]}")
#                 print(f"Precio: ${producto_encontrado[3]}")
#                 print(f"Cantidad: {producto_encontrado[4]}")
#                 print(f"Categoría: {producto_encontrado[5]}\n")
#             else:
#                 print(
#                     f"\nNo se encontró ningún producto con el nombre '{nombre_producto}'.\n"
#                 )

#         elif criterio == "id":
#             id_producto = (
#                 input("Ingrese la ID del producto que desea buscar: ").lower().strip()
#             )

#             # Crear cursor
#             cursor = conn.cursor()

#             # Consulta parametrizada para evitar inyección SQL
#             cursor.execute(
#                 """
#             SELECT id, nombre, descripcion, precio, cantidad, categoria
#             FROM productos
#             WHERE LOWER(id) LIKE ?
#             """,
#                 (id_producto),
#             )

#             # Obtener el producto encontrado
#             producto_encontrado = (
#                 cursor.fetchone()
#             )  # fetchone() para un único resultado

#             if producto_encontrado:
#                 print("\nProducto encontrado:")
#                 print(f"ID: {producto_encontrado[0]}")
#                 print(f"Nombre: {producto_encontrado[1]}")
#                 print(f"Descripción: {producto_encontrado[2]}")
#                 print(f"Precio: ${producto_encontrado[3]}")
#                 print(f"Cantidad: {producto_encontrado[4]}")
#                 print(f"Categoría: {producto_encontrado[5]}\n")
#             else:
#                 print(f"\nNo se encontró ningún producto con la ID '{id_producto}'.\n")
#             cursor.close()
#     except sqlite3.Error as e:
#         print(f"Error al buscar el producto: {e}")


# #### agregar producto


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
#                     INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria)
#                     VALUES (?, ?, ?, ?, ?)
#                     """,
#             (nombre, descripcion, precio, cantidad, categoria),
#         )

#         # Confirmar cambios
#         conn.commit()
#         print("=" * 60)
#         print(f"el producto {nombre} se ha agregado al stock correctamente !!!")
#         print("=" * 60)
#     except sqlite3.Error as e:
#         print(f"Error al insertar el producto: {e}")
#     except ValueError as ve:
#         print(f"Error en los datos ingresados: {ve}")


# ### ver lista completa  de productos
# def ver_lista_completa_productos():

#     try:
#         # Conexión y ejecución de la consulta
#         cursor = conn.cursor()
#         cursor.execute(
#             """
#             SELECT *
#             FROM productos
#             """
#         )
#         productos_encontrados = cursor.fetchall()

#         # Encabezados de la tabla
#         encabezados = ["ID", "Nombre", "Descripción", "Precio", "Cantidad", "Categoría"]

#         # Verificar si hay productos y formatear la salida
#         if productos_encontrados:
#             # Usar tabulate para mostrar los productos como tabla
#             print(tabulate(productos_encontrados, headers=encabezados, tablefmt="grid"))
#         else:
#             print("\nNo se encontró ningún producto en la base de datos.\n")

#     except sqlite3.Error as e:
#         print(f"Error al buscar el producto: {e}")


# ### eliminar un producto seleccionado por su id o por su nombre
# def eliminar_producto():
#     try:
#         criterio = (
#             input(
#                 "¿Desea eliminar el producto por 'ID' o por 'Nombre'? (Escriba 'ID' o 'Nombre'): "
#             )
#             .strip()
#             .lower()
#         )

#         if criterio == "id":
#             id_producto = input(
#                 "Ingrese el ID del producto que desea eliminar: "
#             ).strip()
#             if not id_producto.isdigit():
#                 print("El ID debe ser un número válido.")
#                 return

#             cursor = conn.cursor()
#             cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
#             conn.commit()

#             if cursor.rowcount > 0:
#                 print(f"Producto con ID {id_producto} eliminado correctamente.")
#             else:
#                 print(f"No se encontró un producto con ID {id_producto}.")

#         elif criterio == "nombre":
#             nombre_producto = input(
#                 "Ingrese el Nombre del producto que desea eliminar: "
#             ).strip()
#             if not nombre_producto:
#                 print("Debe ingresar un nombre válido.")
#                 return

#             cursor = conn.cursor()
#             cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre_producto,))
#             conn.commit()

#             if cursor.rowcount > 0:
#                 print(
#                     f"Producto con Nombre '{nombre_producto}' eliminado correctamente."
#                 )
#             else:
#                 print(f"No se encontró un producto con el Nombre '{nombre_producto}'.")
#         else:
#             print("Opción inválida. Por favor, elija 'ID' o 'Nombre'.")

#     except sqlite3.Error as e:
#         print(f"Error al eliminar el producto: {e}")


# ######  actualizar producto  ######


# def actualizar_producto():
#     try:

#         criterio = (
#             input(
#                 "¿Desea actualizar el producto por 'ID' o por 'Nombre'? (Escriba 'ID' o 'Nombre'): "
#             )
#             .strip()
#             .lower()
#         )

#         if criterio not in ["id", "nombre"]:
#             print("Criterio inválido. Por favor, elija 'ID' o 'Nombre'.")
#             return

#         if criterio == "id":
#             identificador = input(
#                 "Ingrese la ID del producto que desea actualizar: "
#             ).strip()
#             columna_criterio = "id"
#         else:
#             identificador = (
#                 input("Ingrese el nombre del producto que desea actualizar: ")
#                 .strip()
#                 .lower()
#             )
#             columna_criterio = "LOWER(nombre)"

#         nuevo_nombre = input(
#             "Ingrese el nuevo nombre del producto (o presione Enter para no cambiar): "
#         ).strip()
#         nueva_descripcion = input(
#             "Ingrese la nueva descripción del producto (o presione Enter para no cambiar): "
#         ).strip()
#         nuevo_precio = input(
#             "Ingrese el nuevo precio del producto (o presione Enter para no cambiar): "
#         ).strip()
#         nueva_cantidad = input(
#             "Ingrese la nueva cantidad del producto (o presione Enter para no cambiar): "
#         ).strip()
#         nueva_categoria = input(
#             "Ingrese la nueva categoría del producto (o presione Enter para no cambiar): "
#         ).strip()

#         campos_a_actualizar = []
#         valores = []

#         if nuevo_nombre:
#             campos_a_actualizar.append("nombre = ?")
#             valores.append(nuevo_nombre)
#         if nueva_descripcion:
#             campos_a_actualizar.append("descripcion = ?")
#             valores.append(nueva_descripcion)
#         if nuevo_precio:
#             campos_a_actualizar.append("precio = ?")
#             valores.append(float(nuevo_precio))
#         if nueva_cantidad:
#             campos_a_actualizar.append("cantidad = ?")
#             valores.append(int(nueva_cantidad))
#         if nueva_categoria:
#             campos_a_actualizar.append("categoria = ?")
#             valores.append(nueva_categoria)

#         if not campos_a_actualizar:
#             print("No se proporcionaron nuevos valores. Nada que actualizar.")
#             return

#         cursor = conn.cursor()

#         consulta = f"""
#             UPDATE productos
#             SET {', '.join(campos_a_actualizar)}
#             WHERE {columna_criterio} = ?
#         """
#         valores.append(identificador)

#         cursor.execute(consulta, valores)
#         conn.commit()

#         print("\nProducto actualizado exitosamente.\n")

#         cursor.close()

#     except sqlite3.Error as e:
#         print(f"Error al actualizar el producto: {e}")
#     except ValueError as e:
#         print(f"Error en los valores ingresados: {e}")


# #### mostrar stock ####


# def mostrar_stock():

#     try:
#         nombre_producto = (
#             input("Ingrese el nombre del producto que desea ver el stock: ")
#             .strip()
#             .lower()
#         )

#         cursor = conn.cursor()

#         cursor.execute(
#             """
#                 SELECT cantidad
#                 FROM productos
#                 WHERE LOWER(nombre) LIKE ?
#                 """,
#             (f"%{nombre_producto}%",),
#         )

#         producto_encontrado = cursor.fetchone()

#         if producto_encontrado:
#             print("=" * 60)
#             print(
#                 f"El stock del producto '{nombre_producto}' es de {producto_encontrado[0]} unidades."
#             )
#             print("=" * 60)
#         else:
#             print("=" * 60)
#             print(f"No se encontró ningún producto con el nombre '{nombre_producto}'.")
#             print("=" * 60)
#     except sqlite3.Error as e:
#         print(f"Error al consultar el stock: {e}")


# ####### detectar stock bajo #####
# def detectar_stock_bajo():
#     cursor = conn.cursor()
#     cursor.execute("""SELECT id,nombre, cantidad FROM productos WHERE CANTIDAD < 10;""")
#     cantidades = cursor.fetchall()
#     print("=" * 40)
#     print("productos con bajo stock :")
#     print("=" * 40)
#     print("")
#     for cantidad in cantidades:

#         print(f"id:{cantidad[0]} - producto: {cantidad[1]} - contidad: {cantidad[2]}")
#         print("-" * 40)

#         # Mostrar solo el valor de la cantid


# ############  APP PRINCIPAL  #############


def main():
    while True:
        menu_principal()  # Mostrar el menú al inicio del bucle
        opcion_elegida = input("Elija una opción: ")
        if opcion_elegida == "1":
            insertar_producto()
        elif opcion_elegida == "2":
            ver_lista_completa_productos()
        elif opcion_elegida == "3":
            eliminar_producto()
        elif opcion_elegida == "4":
            buscar_un_producto()
        elif opcion_elegida == "5":
            actualizar_producto()
        elif opcion_elegida == "6":
            mostrar_stock()
        elif opcion_elegida == "7":
            detectar_stock_bajo()
        elif opcion_elegida == "8":
            print("\nHASTA PRONTO !!!")
            break  # Salir del bucle
        else:
            print("Elija una opción válida. Debe ser un número del 1 al 8.")


main()
