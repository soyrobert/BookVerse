import { Routes } from '@angular/router';
import { LibroModule } from './Libro/Libro.module';
import { ListarLibrosComponent } from './Libro/listar-libros/listar-libros.component';
import { AgregarLibrosComponent } from './Libro/agregar-libros/agregar-libros.component';

export const routes: Routes = [
  { path: '', component: ListarLibrosComponent},
  { path: 'agregar', component: AgregarLibrosComponent}
];
