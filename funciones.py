import sqlite3
from database import *
from tabulate import tabulate
from colorama import init, Fore, Back, Style

init()
init(autoreset=True)


#### menu principal
def menu_principal():
    print(
        Style.BRIGHT
        + Fore.MAGENTA
        + """        #######################################
                GESTION DE STOCK
        #######################################\n"""
    )
    print(Fore.BLUE + "Elija una opcion")
    print(Fore.BLUE + "opcion 1: Agregar un producto")
    print(Fore.BLUE + "opcion 2: Ver lista completa de productos")
    print(Fore.BLUE + "opcion 3: Eliminar un producto de la lista")
    print(Fore.BLUE + "opcion 4: Buscar un producto especifico de la lista")
    print(Fore.BLUE + "opcion 5: Actualizar un producto")
    print(Fore.BLUE + "opcion 6: mostrar stock de un  producto")
    print(Fore.BLUE + "opcion 7: detectar stock bajo (menos de 10 unidades)")
    print(Fore.BLUE + "opcion 8: Salir del menú\n")


####  buscar producto


def buscar_un_producto():
    conn = sqlite3.connect("inventario.db")
    try:
        criterio = (
            input(
                "¿Desea buscar el producto por 'ID' o por 'Nombre'? (Escriba 'ID' o 'Nombre'): "
            )
            .strip()
            .lower()
        )

        if criterio == "nombre":
            nombre_producto = input(
                "Ingrese el nombre del producto que desea buscar: "
            ).lower()

            cursor = conn.cursor()

            cursor.execute(
                """
            SELECT id, nombre, descripcion, precio, cantidad, categoria
            FROM productos
            WHERE LOWER(nombre) LIKE ?
            """,
                (f"%{nombre_producto}%",),
            )

            producto_encontrado = cursor.fetchone()

            if producto_encontrado:
                print(Fore.YELLOW + "\nProducto encontrado:")
                print(f"ID: {producto_encontrado[0]}")
                print(f"Nombre: {producto_encontrado[1]}")
                print(f"Descripción: {producto_encontrado[2]}")
                print(f"Precio: ${producto_encontrado[3]}")
                print(f"Cantidad: {producto_encontrado[4]}")
                print(f"Categoría: {producto_encontrado[5]}\n")
            else:
                print(
                    f"\nNo se encontró ningún producto con el nombre '{nombre_producto}'.\n"
                )

        elif criterio == "id":
            id_producto_input = input(
                "Ingrese la ID del producto que desea buscar: "
            ).strip()
            id_producto = int(id_producto_input)

            cursor = conn.cursor()

            cursor.execute(
                """
            SELECT id, nombre, descripcion, precio, cantidad, categoria
            FROM productos
            WHERE id = ?
            """,
                (id_producto,),  # Pasamos como tupla
            )

            producto_encontrado = cursor.fetchone()

            if producto_encontrado:
                print("\nProducto encontrado:")
                print(f"ID: {producto_encontrado[0]}")
                print(f"Nombre: {producto_encontrado[1]}")
                print(f"Descripción: {producto_encontrado[2]}")
                print(f"Precio: ${producto_encontrado[3]}")
                print(f"Cantidad: {producto_encontrado[4]}")
                print(f"Categoría: {producto_encontrado[5]}\n")
            else:
                print("=" * 60)
                print(f"\nNo se encontró ningún producto con la ID '{id_producto}'.\n")
                print("=" * 60)

            cursor.close()

    except sqlite3.Error as e:
        print(f"Error al buscar el producto: {e}")
    finally:
        conn.close()  # Cerrar la conexión en el bloque finally


#### agregar producto


def insertar_producto():
    conn = sqlite3.connect("inventario.db")  # Conexión a la base de datos
    cursor = conn.cursor()
    try:
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        categoria = input(
            "Ingrese la categoría del producto (ropa de hombre, ropa de mujer, ropa de niño, calzado): "
        )

        cursor.execute(
            """
                    INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria)
                    VALUES (?, ?, ?, ?, ?)
                    """,
            (nombre, descripcion, precio, cantidad, categoria),
        )

        conn.commit()
        print("=" * 60)
        print(f"el producto {nombre} se ha agregado al stock correctamente !!!")
        print("=" * 60)
    except sqlite3.Error as e:
        print(f"Error al insertar el producto: {e}")
    except ValueError as ve:
        print(f"Error en los datos ingresados: {ve}")


### ver lista completa  de productos


def ver_lista_completa_productos():

    try:
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM productos
            """
        )
        productos_encontrados = cursor.fetchall()

        encabezados = ["ID", "Nombre", "Descripción", "Precio", "Cantidad", "Categoría"]

        if productos_encontrados:

            print(tabulate(productos_encontrados, headers=encabezados, tablefmt="grid"))
        else:
            print("\nNo se encontró ningún producto en la base de datos.\n")

    except sqlite3.Error as e:
        print(f"Error al buscar el producto: {e}")


### eliminar un producto seleccionado por su id o por su nombre
def eliminar_producto():
    try:
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()

        criterio = (
            input(
                "¿Desea eliminar el producto por 'ID' o por 'Nombre'? (Escriba 'ID' o 'Nombre'): "
            )
            .strip()
            .lower()
        )

        if criterio == "id":
            id_producto = input(
                "Ingrese el ID del producto que desea eliminar: "
            ).strip()
            if not id_producto.isdigit():
                print("El ID debe ser un número válido.")
                return

            cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
            conn.commit()

            if cursor.rowcount > 0:
                print("=" * 60)
                print(f"Producto con ID {id_producto} eliminado correctamente.")
                print("=" * 60)
            else:
                print("=" * 60)
                print(f"No se encontró un producto con ID {id_producto}.")
                print("=" * 60)

        elif criterio == "nombre":
            nombre_producto = input(
                "Ingrese el Nombre del producto que desea eliminar: "
            ).strip()
            if not nombre_producto:
                print("Debe ingresar un nombre válido.")
                return

            cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre_producto,))
            conn.commit()

            if cursor.rowcount > 0:
                print("=" * 60)
                print(
                    f"Producto con Nombre '{nombre_producto}' eliminado correctamente."
                )
                print("=" * 60)
            else:
                print("=" * 60)
                print(f"No se encontró un producto con el Nombre '{nombre_producto}'.")
                print("=" * 60)

        else:
            print("=" * 60)
            print("Opción inválida. Por favor, elija 'ID' o 'Nombre'.")
            print("=" * 60)

    except sqlite3.Error as e:
        print(f"Error al eliminar el producto: {e}")
    finally:
        if conn:
            conn.close()  # Cerrar la conexión


######  actualizar producto  ######


def actualizar_producto():
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()

        # Selección del criterio de búsqueda
        criterio = (
            input(
                "¿Desea actualizar el producto por 'ID' o por 'Nombre'? (Escriba 'ID' o 'Nombre'): "
            )
            .strip()
            .lower()
        )

        if criterio not in ["id", "nombre"]:
            print("Criterio inválido. Por favor, elija 'ID' o 'Nombre'.")
            return

        # Definir criterio de búsqueda y columna
        if criterio == "id":
            identificador = input(
                "Ingrese la ID del producto que desea actualizar: "
            ).strip()
            if not identificador.isdigit():
                print("La ID debe ser un número válido.")
                return
            columna_criterio = "id"
        else:
            identificador = input(
                "Ingrese el nombre del producto que desea actualizar: "
            ).strip()
            if not identificador:
                print("Debe ingresar un nombre válido.")
                return
            columna_criterio = "nombre"

        # Nuevos valores para actualizar
        nuevo_nombre = input(
            "Ingrese el nuevo nombre del producto (o presione Enter para no cambiar): "
        ).strip()
        nueva_descripcion = input(
            "Ingrese la nueva descripción del producto (o presione Enter para no cambiar): "
        ).strip()
        nuevo_precio = input(
            "Ingrese el nuevo precio del producto (o presione Enter para no cambiar): "
        ).strip()
        nueva_cantidad = input(
            "Ingrese la nueva cantidad del producto (o presione Enter para no cambiar): "
        ).strip()
        nueva_categoria = input(
            "Ingrese la nueva categoría del producto (o presione Enter para no cambiar): "
        ).strip()

        # Preparar campos para actualizar
        campos_a_actualizar = []
        valores = []

        if nuevo_nombre:
            campos_a_actualizar.append("nombre = ?")
            valores.append(nuevo_nombre)
        if nueva_descripcion:
            campos_a_actualizar.append("descripcion = ?")
            valores.append(nueva_descripcion)
        if nuevo_precio:
            try:
                valores.append(float(nuevo_precio))
                campos_a_actualizar.append("precio = ?")
            except ValueError:
                print("El precio debe ser un número válido.")
                return
        if nueva_cantidad:
            try:
                valores.append(int(nueva_cantidad))
                campos_a_actualizar.append("cantidad = ?")
            except ValueError:
                print("La cantidad debe ser un número entero.")
                return
        if nueva_categoria:
            campos_a_actualizar.append("categoria = ?")
            valores.append(nueva_categoria)

        # Verificar si hay algo que actualizar
        if not campos_a_actualizar:
            print("No se proporcionaron nuevos valores. Nada que actualizar.")
            return

        # Construir y ejecutar la consulta de actualización
        consulta = f"""
            UPDATE productos
            SET {', '.join(campos_a_actualizar)}
            WHERE {columna_criterio} = ?
        """
        valores.append(identificador)

        cursor.execute(consulta, valores)
        conn.commit()

        # Verificar si se actualizó algún registro
        if cursor.rowcount > 0:
            print("\nProducto actualizado exitosamente.\n")
        else:
            print(
                "\nNo se encontró ningún producto que coincida con el criterio especificado.\n"
            )

    except sqlite3.Error as e:
        print(f"Error al actualizar el producto: {e}")
    except ValueError as e:
        print(f"Error en los valores ingresados: {e}")
    finally:
        if conn:
            conn.close()  # Cerrar la conexión para evitar fugas de recursos


#### mostrar stock ####


def mostrar_stock():
    try:
        # Crear conexión a la base de datos
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()

        # Solicitar el nombre del producto
        nombre_producto = (
            input("Ingrese el nombre del producto que desea ver el stock: ")
            .strip()
            .lower()
        )

        # Ejecutar la consulta
        cursor.execute(
            """
            SELECT cantidad
            FROM productos
            WHERE LOWER(nombre) LIKE ?
            """,
            (f"%{nombre_producto}%",),
        )

        # Recuperar el resultado
        producto_encontrado = cursor.fetchone()

        if producto_encontrado:
            print("=" * 60)
            print(
                f"El stock del producto '{nombre_producto}' es de {producto_encontrado[0]} unidades."
            )
            print("=" * 60)
        else:
            print("=" * 60)
            print(f"No se encontró ningún producto con el nombre '{nombre_producto}'.")
            print("=" * 60)

    except sqlite3.Error as e:
        print(f"Error al consultar el stock: {e}")

    finally:
        # Cerrar la conexión
        if conn:
            conn.close()


####### detectar stock bajo #####
def detectar_stock_bajo():
    try:
        # Crear conexión a la base de datos
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()

        # Ejecutar la consulta para obtener productos con stock bajo
        cursor.execute(
            """SELECT id, nombre, cantidad FROM productos WHERE cantidad < 10;"""
        )
        cantidades = cursor.fetchall()

        # Verificar si hay productos con stock bajo
        if cantidades:
            print("=" * 40)
            print("Productos con bajo stock:")
            print("=" * 40)
            print("")

            # Mostrar los productos con stock bajo
            for cantidad in cantidades:
                print(
                    f"ID: {cantidad[0]} - Producto: {cantidad[1]} - Cantidad: {cantidad[2]}"
                )
                print("-" * 40)
        else:
            print("=" * 40)
            print("No hay productos con stock bajo.")
            print("=" * 40)

    except sqlite3.Error as e:
        print(f"Error al detectar el stock bajo: {e}")

    finally:
        # Cerrar la conexión
        if conn:
            conn.close()
