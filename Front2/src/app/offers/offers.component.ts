import { Component, OnInit } from '@angular/core';
import { IOffers } from '../shared/models';
import { AuthService } from '../shared/services/auth.service';
import { ProviderService } from '../shared/services/provider.service';


@Component({
  selector: 'app-offers',
  templateUrl: './offers.component.html',
  styleUrls: ['./offers.component.css']
})
export class OffersComponent implements OnInit {

  public offersList: IOffers[] = [];

  constructor(
    private provider: ProviderService,
    private auth: AuthService
  ) { }

  ngOnInit() {
    if(this.auth.isAuthenticated){
      this.provider.getOffers().then(res => {
        this.offersList = res;
      })
    }
  }

}
