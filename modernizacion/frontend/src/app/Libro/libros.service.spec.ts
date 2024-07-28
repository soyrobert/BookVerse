/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { LibrosService } from './libros.service';

describe('Service: Libros', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [LibrosService]
    });
  });

  it('should ...', inject([LibrosService], (service: LibrosService) => {
    expect(service).toBeTruthy();
  }));
});
