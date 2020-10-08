import { NgModule } from '@angular/core';
import { MatIconModule } from '@angular/material/icon';
import { MatSliderModule } from '@angular/material/slider';

//const matModules = [CdkTableModule,MatAutocompleteModule,MatButtonModule]; 
const matModules = [MatIconModule,MatSliderModule]; 

@NgModule({
  declarations: [],
  imports: [...matModules],
  exports: [...matModules]
})
export class MaterialConfigurationModule { }
