import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { Libro } from './Libro';

@Injectable({
  providedIn: 'root',
})
export class LibrosService {
  private url = environment.API;
  constructor(private http:HttpClient) { }

  obtenerLibros():Observable<Array<Libro>>{
    return this.http.get<Array<Libro>>(`${this.url}/queries`);
  }

  agregarLibros(request: any):Observable<string>{
    return this.http.post<string>(`${this.url}/commands`, request);
  }
}

