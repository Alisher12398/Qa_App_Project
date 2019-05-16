import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RegisterComponent } from './auth/register/register.component';
import { LoginComponent } from './auth/login/login.component';
import {MainPageComponent} from './main-page/main-page.component';
import {ProfileComponent} from './profile/profile.component';
import {GroupsComponent} from './groups/groups.component';
import {QaComponent} from './qa/qa.component';

const routes: Routes = [
  {path: '', component: MainPageComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'login', component: LoginComponent},
  {path: 'profile', component: ProfileComponent},
  {path: 'groups', component: GroupsComponent},
  {path: 'groups/:id', component: QaComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
