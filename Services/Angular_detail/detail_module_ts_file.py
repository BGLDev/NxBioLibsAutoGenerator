from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class DetailModuleTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase):
        file_content = f'''
        import {{ CommonModule }} from '@angular/common';
        import {{ NgModule }} from '@angular/core';
        import {{ ReactiveFormsModule }} from '@angular/forms';
        import {{ MatAutocompleteModule }} from '@angular/material/autocomplete';
        import {{ MatButtonModule }} from '@angular/material/button';
        import {{ MatCheckboxModule }} from '@angular/material/checkbox';
        import {{ MatFormFieldModule }} from '@angular/material/form-field';
        import {{ MatIconModule }} from '@angular/material/icon';
        import {{ MatInputModule }} from '@angular/material/input';
        import {{ MatSelectModule }} from '@angular/material/select';
        import {{ MatSlideToggleModule }} from '@angular/material/slide-toggle';
        import {{ MatTableModule }} from '@angular/material/table';
        import {{ MatTooltipModule }} from '@angular/material/tooltip';
        import {{ RouterModule }} from '@angular/router';
        import {{ NoRoundDecimalPipeModule }} from '@biolan/shared/pipes/no-round-decimal';
        import {{ ShortDatePipeModule }} from '@biolan/shared/pipes/short-date';
        import {{ ChipModule }} from '@biolan/shared/ui/chip';
        import {{ InputAutocompleteModule }} from '@biolan/shared/ui/input-autocomplete';
        import {{ TranslocoModule }} from '@ngneat/transloco';
        import {{ MatNativeDateModule }} from '@angular/material/core';
        import {{ MatDatepickerModule }} from '@angular/material/datepicker';
        import {{ {lib_name.pascal}Component }} from './{lib_name.kebab}.component';
        import {{ {lib_name.camel}Routes }} from './lib.routes';
        
        @NgModule({{
          imports: [
            CommonModule,
            RouterModule.forChild({lib_name.camel}Routes),
            MatInputModule,
            ReactiveFormsModule,
            MatFormFieldModule,
            MatSelectModule,
            MatButtonModule,
            MatIconModule,
            MatAutocompleteModule,
            TranslocoModule,
            MatCheckboxModule,
            MatSlideToggleModule,
            MatTableModule,
            MatDatepickerModule,
            MatNativeDateModule,
            ShortDatePipeModule,
            ChipModule,
            NoRoundDecimalPipeModule,
            InputAutocompleteModule,
            MatTooltipModule,
          ],
          declarations: [{lib_name.pascal}Component],
          exports: [{lib_name.pascal}Component],
        }})
        export class {lib_name.pascal}Module {{}}
        '''
        return file_content

