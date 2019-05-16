import { Component, OnInit } from '@angular/core';
import {IGroup} from '../shared/models';
import { Location } from '@angular/common';
import { AuthService } from '../shared/services/auth.service';
import { ProviderService } from '../shared/services/provider.service';

@Component({
  selector: 'app-groups',
  templateUrl: './groups.component.html',
  styleUrls: ['./groups.component.css']
})
export class GroupsComponent implements OnInit {

  public groupList: IGroup[] = [];

  public GroupTitle: string = ""

  constructor(
    private provider: ProviderService,
    private location: Location,
    private auth: AuthService
  ) { }

  ngOnInit() {
    if(this.auth.isAuthenticated){
      this.provider.getGroups().then(res => {
        this.groupList = res;
      })
    }
  }

}
