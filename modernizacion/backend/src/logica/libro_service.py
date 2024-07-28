from .deserializers import CreateLibroSchema
from ..modelos import Libro, db, libro_schema
from .errors import DuplicatedBookData
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError


class LibroService():

    def create_libro(self, crear_libro: CreateLibroSchema):
        try:
            nuevo_libro = Libro(**crear_libro)
            db.session.add(nuevo_libro)
            db.session.commit()

        except (IntegrityError, UniqueViolation):
            db.session.rollback()
            raise DuplicatedBookData()
        
    def obtener_libros(self):
       libros = Libro.query.all()

       return [libro_schema.dump(libro) for libro in libros]
    


