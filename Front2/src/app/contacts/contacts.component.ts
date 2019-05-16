// import { Component, OnInit } from '@angular/core';
// import { ProviderService } from '../shared/services/provider.service';
// import { IContact } from '../shared/models';
// import { Location } from '@angular/common';
// import { AuthService } from '../shared/services/auth.service';
//
// @Component({
//   selector: 'app-task-lists',
//   templateUrl: './contacts.component.html',
//   styleUrls: ['./contacts.component.css']
// })
// export class ContactsComponent implements OnInit {
//
//   public contacts: IContact[] = [];
//
//   public contactName: string = ""
//   public contactPhone: string = ""
//
//   constructor(
//     private provider: ProviderService,
//     private location: Location,
//     private auth: AuthService
//   ) { }
//
//   ngOnInit() {
//     if(this.auth.isAuthenticated){
//       this.provider.getTaskLists().then(res => {
//         this.contacts = res;
//       })
//     }
//   }
//
//   navigateBack(){
//     this.location.back()
//   }
//
//   createContact(){
//     if(this.contactName != ''){
//       this.provider.createContact(this.contactName, this.contactPhone).then(res => {
//         this.contacts.push(res)
//       })
//     }
//   }
//
//   // sendId(id: number){
//   //   this.provider.sendMessage.emit(id+"")
//   // }
//
// }
