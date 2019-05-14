import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {IUser, IOffers, IOffersPurchases} from '../shared/models';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {

  public purchased_offers: IOffersPurchases[] = []

  public offers: IOffers[] = []

  public id_offer: any = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getOffers().then(res => {
      this.offers = res;
    });

    //purchaseOffer() {
    //  this.provider.purchaseOffer(this.id_offer).then(res => {
    //    this.purchased_offers.push(res);
    //  });
    //}

  }

}
