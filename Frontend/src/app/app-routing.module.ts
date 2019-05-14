import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BaseComponent } from './base/base.component';
import { ProfileComponent } from './profile/profile.component';
import { MainComponent } from './main/main.component';

const routes: Routes = [
   {path: '', component: BaseComponent},
   {path: 'main', component: MainComponent},
   {path: 'profile', component: ProfileComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
