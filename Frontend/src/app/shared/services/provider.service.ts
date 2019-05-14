import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProviderService {
  getProfile() {
    throw new Error("Method not implemented.");
  }

  constructor() { }
}
