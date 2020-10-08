import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home.component';
//import { MaterialConfigurationModule } from '../material-configuration-module/material-configuration-module.module';
import { MatIconModule } from '@angular/material/icon';
import { MatSliderModule } from '@angular/material/slider';

@NgModule({
  declarations: [HomeComponent],
  imports: [
    CommonModule, MatIconModule,MatSliderModule
  ]
})
export class HomeModule { }
