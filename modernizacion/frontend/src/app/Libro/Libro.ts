export class Libro {
  titulo: string | null;
  fecha_publicacion: string | null;
  paginas: number | null;
  ISBN: string | null;
  autor: string | null;
  editorial: string | null;
  portada: string | null;
  constructor(
    titulo: string | null,
    fecha_publicacion: string | null,
    paginas: number | null,
    ISBN: string | null,
    autor: string | null,
    editorial: string | null,
    portada: string | null
  ){
    this.titulo = titulo;
    this.fecha_publicacion = fecha_publicacion;
    this.paginas = paginas;
    this.ISBN = ISBN;
    this.autor = autor;
    this.editorial = editorial;
    this.portada = portada;
  }

}
