import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GroupsformComponent } from './groupsform.component';

describe('GroupsformComponent', () => {
  let component: GroupsformComponent;
  let fixture: ComponentFixture<GroupsformComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GroupsformComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GroupsformComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
