import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  Validators,
  FormControl,
} from '@angular/forms';
import { LibrosService } from '../libros.service';
import { Libro} from '../Libro';
@Component({
  selector: 'app-agregar-libros',
  templateUrl: './agregar-libros.component.html',
  styleUrls: ['./agregar-libros.component.css']
})
export class AgregarLibrosComponent implements OnInit {
  libroForm = this.formBuilder.group({
    titulo:['', [Validators.required, Validators.min(1)]],
    fecha_publicacion:['',[
      Validators.required]],
    paginas:[0,[Validators.required]],
    ISBN:['',[Validators.required]],
    autor:['',[Validators.required]],
    editorial:['',[Validators.required]],
  })
  image!: string;
  alert!: boolean;
  constructor(
    private formBuilder: FormBuilder,
    private librosService: LibrosService
  ) { }

  ngOnInit() {
  }

  agregar(
    titulo:string|null,
    fecha:string|null,
    paginas:number|null,
    ISBN:string|null,
    autor:string|null,
    editorial:string|null
  ){
    if(this.image == null){
      this.image = "";
    }
    let lib = {
      titulo: titulo,
      fechaPublicacion: fecha,
      paginas: paginas,
      autor: autor,
      ISBN: ISBN,
      editorial: editorial,
      portada: this.image
    }
    this.librosService.agregarLibros(lib).subscribe(()=>{
      console.log("libro enviado")
    })
  }
  uploadImage(event:any){
    var img = new Image();
    var reader = new FileReader();
    const file = event.target.files[0]
    img.src = URL.createObjectURL(file);
    img.onload = () => {
      if(img.width > 184 || img.height > 273){
        console.log("Error tamaño")
        this.image = "";
      }
      else{
        reader.readAsDataURL(file)
        reader.onload = () => {
          this.image = reader.result as string;
        };
      }
    }
  }
}
