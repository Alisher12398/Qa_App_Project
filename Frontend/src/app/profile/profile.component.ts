import { Component, OnInit } from '@angular/core';
import { AuthService } from '../shared/services/auth.service';
import { ProviderService } from '../shared/services/provider.service';
import { IProfile } from '../shared/models';
import { Location } from '@angular/common';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  public profile: IProfile[] = [];

  // public ProfileName: string = ""

  constructor(
    private provider: ProviderService,
    private location: Location,
    private auth: AuthService
  ) { }

  ngOnInit(){

  }

  // ngOnInit() {
  //   if(this.auth.isAuthenticated){
  //     this.provider.getProfile().then(res => {
  //       this.profile = res;
  //     })
  // }

  // navigateBack(){
  //   this.location.back()
  // }

  // createProfile(){
  //   if(this.profile != ''){
  //   this.provider.createProfile(this.profile).then(res => {
  //     this.profile.push(res)
  //   })
  // }

}
