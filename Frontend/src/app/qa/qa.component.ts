import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { IQa } from '../shared/models';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { AuthService } from '../shared/services/auth.service';

@Component({
  selector: 'app-qa',
  templateUrl: './qa.component.html',
  styleUrls: ['./qa.component.css']
})

export class QaComponent implements OnInit {

  public qas : IQa[] = [];

  public id : number;

  public qa_question: string = "";
  public qa_answer_1: string = "";
  public qa_answer_2: string = "";
  public qa_answer_3: string = "";
  public qa_answer_4: string = "";
  public qa_answer_right: number = 0;

  constructor(
    private provider: ProviderService,
    private route: ActivatedRoute,
    private location: Location,
    private auth: AuthService
  ) { }

  ngOnInit() {
  }

}
