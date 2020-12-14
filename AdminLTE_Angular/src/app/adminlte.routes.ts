import { RouterModule, Routes } from '@angular/router';
import {BlankComponent} from './././components/body/blank/blank.component';

const app_routes: Routes = [
  { path: 'home', component: BlankComponent },
  { path: '**', pathMatch: 'full', redirectTo: 'home' }
];

export const app_routing = RouterModule.forRoot(app_routes);
