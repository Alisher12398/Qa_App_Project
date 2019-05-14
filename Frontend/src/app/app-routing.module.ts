import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainComponent } from './main/main.component';
import { RegistrationComponent } from './registration/registration.component';
import { LoginComponent } from './login/login.component';
import { ProfileComponent } from './profile/profile.component';
import { QuizComponent } from './quiz/quiz.component';
import { OffersComponent } from './offers/offers.component';
import { GroupsComponent } from './groups/groups.component';
const routes: Routes = [
  { path: '', component: MainComponent },
  { path: 'companies', component: OffersComponent },
  { path: 'registration', component: RegistrationComponent},
  { path: 'login', component: LoginComponent},
  { path: 'profile', component: ProfileComponent},
  { path: 'quiz', component: GroupsComponent},
  { path: 'test', component: QuizComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }