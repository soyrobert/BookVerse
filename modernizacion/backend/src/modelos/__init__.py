from .libro import db, ma, Libro, LibroSerializerSchema

# Define el esquema de creación
create_schema = LibroSerializerSchema()
libro_schema = LibroSerializerSchema()

# Exportar los elementos necesarios
__all__ = ["db", "ma", "Libro", "LibroSerializerSchema", "create_schema", "libro_schema"]
