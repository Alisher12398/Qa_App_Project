import { Component, OnInit } from '@angular/core';
import { AuthService } from '../shared/services/auth.service';
import { ProviderService } from '../shared/services/provider.service';
import {Location} from '@angular/common';
import {IUser} from '../shared/models';
import {forEach} from '@angular/router/src/utils/collection';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  public id_user: number = 0;
  public users: IUser[] = [];
  public id = localStorage.key(this.id_user)

  constructor(
    private provider: ProviderService,
    private auth: AuthService
  ) { }

  ngOnInit() {
    if(this.auth.isAuthenticated){
      this.provider.getUser().then(res => {
        this.users = res;
      })
    }
  }

}
