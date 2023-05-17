import sqlite3

conn = sqlite3.connect("./bases-datos/alumnos.db")

# Crear el cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla Alumnos
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Alumnos (
                    id INTEGER,
                    nombre TEXT,
                    apellido TEXT
                )"""
)

# Insertar datos en la tabla Alumnos
alumnos = [
    (1, "Juan", "Pérez"),
    (2, "María", "González"),
    (3, "Pedro", "Sánchez"),
    (4, "Ana", "López"),
    (5, "Carlos", "Martínez"),
    (6, "Laura", "Ramírez"),
    (7, "Manuel", "Fernández"),
    (8, "Sofía", "Torres"),
]

cursor.executemany("INSERT INTO Alumnos VALUES (?, ?, ?)", alumnos)

# Realizar una búsqueda de un alumno por nombre
nombre_buscar = "Juan"
cursor.execute(
    "SELECT id, nombre, apellido FROM Alumnos WHERE nombre = ?", (nombre_buscar,)
)
alumno_encontrado = cursor.fetchone()
print(alumno_encontrado)

# Cerrar la conexión a la base de datos
conn.close()
