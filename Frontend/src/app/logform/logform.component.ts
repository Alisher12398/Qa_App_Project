import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/shared/services/provider.service';
import { AuthService } from 'src/app/shared/services/auth.service';

@Component({
  selector: 'app-logform',
  templateUrl: './logform.component.html',
  styleUrls: ['./logform.component.css']
})
export class LogformComponent implements OnInit {

  public username: any = "";

  public password: any = "";

  constructor(
    private provider: ProviderService,
    private auth: AuthService
  ) { }

  ngOnInit() {
  }

  login() {
      this.auth.login(this.username, this.password);
  }

}
