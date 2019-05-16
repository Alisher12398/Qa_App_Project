// import { Component, OnInit } from '@angular/core';
// import { IContact, IContactNew } from '../shared/models';
// import { ProviderService } from '../shared/services/provider.service';
// import { Location } from '@angular/common';
// import { identifierModuleUrl } from '@angular/compiler';
// import { ActivatedRoute } from '@angular/router';
// import { empty } from 'rxjs';
// import { AuthService } from '../shared/services/auth.service';
//
// @Component({
//   selector: 'app-task-list-detail',
//   templateUrl: './contact-detail.component.html',
//   styleUrls: ['./contact-detail.component.css']
// })
// export class ContactDetailComponent implements OnInit {
//
//   public id: number = 0;
//
//   public taskList: any = {}
//
//   constructor(
//     private provider: ProviderService,
//     private router: ActivatedRoute,
//     private location: Location,
//     private auth: AuthService
//   ) { }
//
//   ngOnInit() {
//
//     // this.provider.sendMessage.subscribe(res => {
//     //   this.id = parseInt(res)
//     // })
//     if(this.auth.isAuthenticated){
//       this.id = parseInt(this.router.snapshot.paramMap.get('id'))
//
//       if(this.id){
//         this.provider.getTaskListDetail(this.id).then(res => {
//           this.taskList = res
//         })
//       }
//     }
//   }
//
//
//   updateTaskList(){
//     this.provider.updateContact(this.taskList).then(res => {
//       this.taskList = res
//     })
//   }
//
//   deleteTaskList(){
//     this.provider.deleteContact(this.taskList.id).then(() => {
//     })
//   }
//
// }
