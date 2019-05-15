import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/shared/services/provider.service';
import { AuthService } from 'src/app/shared/services/auth.service';

@Component({
  selector: 'app-registerform',
  templateUrl: './registerform.component.html',
  styleUrls: ['./registerform.component.css']
})
export class RegisterformComponent implements OnInit {

  public username: any = "";

  public password: any = "";

  constructor(
    private provider: ProviderService,
    private auth: AuthService
  ) { }

  ngOnInit() {
  }

  register() {
    console.log("asdfasdfasdf")
    if (this.username !== '' && this.password !== '') {
      this.auth.register(this.username, this.password);
    }
  }

}
