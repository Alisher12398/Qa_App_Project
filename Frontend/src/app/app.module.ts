import { BrowserModule } from '@angular/platform-browser';
import { ClassProvider, NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { QuizComponent } from './quiz/quiz.component';
import { ProfileComponent } from './profile/profile.component';
import { BaseComponent } from './base/base.component';
import { MainComponent } from './main/main.component';
import { OffersComponent } from './offers/offers.component';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AuthInterceptor } from './AuthInterceptor';
import { ProviderService } from './shared/services/provider.service';
import { HttpClientModule } from '@angular/common/http';
import { CompaniesComponent } from './companies/companies.component';
import { HeaderComponent } from './header/header.component';
import { JumbotronComponent } from './jumbotron/jumbotron.component';
import { AboutComponent } from './about/about.component';
import { TeamInfoComponent } from './team-info/team-info.component';
import { FooterComponent } from './footer/footer.component';
import { LogformComponent } from './logform/logform.component';
import { RegisterformComponent } from './registerform/registerform.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { AccountComponent } from './account/account.component';
import { QuizformComponent } from './quizform/quizform.component';
import { GroupsComponent } from './groups/groups.component';
import { GroupsformComponent } from './groupsform/groupsform.component';
import { QaComponent } from './qa/qa.component';
import { RegisterComponent } from './auth/register/register.component';

let routes = [
  { path: "", redirectTo: "/login", pathMatch: "full" },
  { path: "login", component: LoginComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    QuizComponent,
    ProfileComponent,
    BaseComponent,
    MainComponent,
    OffersComponent,
    CompaniesComponent,
    HeaderComponent,
    JumbotronComponent,
    AboutComponent,
    TeamInfoComponent,
    FooterComponent,
    LogformComponent,
    RegisterformComponent,
    LoginComponent,
    RegistrationComponent,
    AccountComponent,
    QuizformComponent,
    GroupsComponent,
    GroupsformComponent,
    QaComponent,
    RegisterComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    ProviderService,
    <ClassProvider>{
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
