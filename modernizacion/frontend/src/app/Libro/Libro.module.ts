import { NgModule} from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatGridListModule } from '@angular/material/grid-list';
import { ListarLibrosComponent } from './listar-libros/listar-libros.component';
import { DetalleLibrosComponent } from './detalle-libros/detalle-libros.component';
import { AgregarLibrosComponent } from './agregar-libros/agregar-libros.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  imports: [
    MatGridListModule,
    CommonModule,
    ReactiveFormsModule,
    FormsModule,
  ],
  declarations: [ListarLibrosComponent,DetalleLibrosComponent, AgregarLibrosComponent],
  exports: [ListarLibrosComponent,DetalleLibrosComponent, AgregarLibrosComponent]
})
export class LibroModule { }
