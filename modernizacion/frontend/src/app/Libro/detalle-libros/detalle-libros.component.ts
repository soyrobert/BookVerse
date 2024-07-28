import { Component, Inject, OnInit } from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { DialogData} from '../listar-libros/listar-libros.component'
@Component({
  selector: 'app-detalle-libros',
  templateUrl: './detalle-libros.component.html',
  styleUrls: ['./detalle-libros.component.css']
})
export class DetalleLibrosComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<DetalleLibrosComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData
  ) { }

  cerrar(): void {
    this.dialogRef.close();
  }

  ngOnInit() {
  }

}
