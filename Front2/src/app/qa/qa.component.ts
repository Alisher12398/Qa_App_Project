import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { AuthService } from '../shared/services/auth.service';
import { ProviderService } from '../shared/services/provider.service';
import { ActivatedRoute } from '@angular/router';
import {IGroup, IQa} from '../shared/models';
@Component({
  selector: 'app-qa',
  templateUrl: './qa.component.html',
  styleUrls: ['./qa.component.css']
})
export class QaComponent implements OnInit {

  public id: number = 0;

  public qaList: IQa[] = [];

  constructor(
    private provider: ProviderService,
    private router: ActivatedRoute,
    private location: Location,
    private auth: AuthService) { }
  //
  ngOnInit() {
    if(this.auth.isAuthenticated){
      this.id = parseInt(this.router.snapshot.paramMap.get('id'))

      if(this.id){
        this.provider.getQa(this.id).then(res => {
          this.qaList = res
        })
      }
    }
  }

}
