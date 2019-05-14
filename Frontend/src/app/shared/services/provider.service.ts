import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {IUser, IOffers, IOffersPurchases} from '../models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  getProfile() {
    throw new Error("Method not implemented.");
  }

  constructor(http: HttpClient) {
    super(http);
  }

  getOffers(): Promise<IOffers[]> {
    return this.get('http://localhost:8000/api/offers/', {});
  }

  //purchaseOffer(idoffer: IOffersPurchases): Promise<IOffersPurchases> {
  //  return this.post('http://localhost:8000/api/purchases/offers/', {
  //    id_offer: idoffer.id_offer
  //  });
  //}

}
