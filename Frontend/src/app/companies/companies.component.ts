import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {IOffers, IOffersPurchases} from '../shared/models';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})

export class CompaniesComponent implements OnInit {

  public id_offer: any = '';

  public offers: IOffers[] = [];

  public purchased_offers: IOffersPurchases[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getOffers().then(res => {
      this.offers = res
    })

    // createOfferPurchase() {
    //   if (this.id_offer !== '') {
    //     this.provider.purchaseOffer(this.id_offer).then(res => {
    //       this.purchased_offers.push(res);
    //     });
    //   }
    // }
  }

}
