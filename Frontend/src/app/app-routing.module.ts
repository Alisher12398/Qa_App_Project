import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BaseComponent } from './base/base.component';
import { MainComponent } from './main/main.component';
import { CompaniesComponent } from './companies/companies.component';
import { RegistrationComponent } from './registration/registration.component';
import { LoginComponent } from './login/login.component';
const routes: Routes = [
  { path: '', component: MainComponent },
  { path: 'companies', component: CompaniesComponent },
  { path: 'registration', component: RegistrationComponent},
  { path: 'login', component: LoginComponent},
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
