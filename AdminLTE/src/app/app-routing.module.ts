import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {BlankComponent} from './././components/body/blank/blank.component';
import { LoginComponent } from './components/body/login/login.component';
import { RegisterComponent } from './components/body/register/register.component';
import { DashboardComponent } from './components/body/dashboard/dashboard.component';


const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'home', component: BlankComponent },
  {path: 'register', component: RegisterComponent},
  {path: 'index', component: DashboardComponent},
  { path: '**', pathMatch: 'full', redirectTo: 'home' }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
