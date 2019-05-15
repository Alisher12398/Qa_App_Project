import { Component, OnInit } from '@angular/core';
// import {AuthService} from '../../shared/service/auth.service';

@Component({
  selector: 'app-logform',
  templateUrl: './logform.component.html',
  styleUrls: ['./logform.component.css']
})
export class LogformComponent implements OnInit {
  // authenticated = false;
  // username = '';
  // password = '';
  // errors: string = null;

  constructor(
    // private auth: AuthService,
    // private route: ActivatedRoute,
    // private router: Router
  ) {
  }

  ngOnInit() {
  }

  // authenticate(username: string, password: string) {
  //   this.auth.authenticate(username, password).then(res => {
  //     this.authenticated = true;
  //     this.router.navigateByUrl('/');
  //   }).catch(err => {
  //     this.errors = err;
  //   });
  // }

}
