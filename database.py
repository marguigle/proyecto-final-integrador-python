import sqlite3 as sql


def crear_tabla():
    # Abrir la conexión a la base de datos
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()

    # Crear la tabla si no existe
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

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()


if __name__ == "__main__":
    crear_tabla()
