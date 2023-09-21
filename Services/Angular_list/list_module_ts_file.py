from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class ListModuleTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase):
        file_content = f'''
        import {{ CommonModule }} from '@angular/common';
        import {{ NgModule }} from '@angular/core';
        import {{ MatCheckboxModule }} from '@angular/material/checkbox';
        import {{ MatIconModule }} from '@angular/material/icon';
        import {{ MatPaginatorModule }} from '@angular/material/paginator';
        import {{ MatSortModule }} from '@angular/material/sort';
        import {{ MatTableModule }} from '@angular/material/table';
        import {{ MatTooltipModule }} from '@angular/material/tooltip';
        import {{ RouterModule }} from '@angular/router';
        import {{ ShortDatePipeModule }} from '@biolan/shared/pipes/short-date';
        import {{ ChipModule }} from '@biolan/shared/ui/chip';
        import {{ TranslocoModule }} from '@ngneat/transloco';
        import {{ {lib_name.pascal}Component }} from './{lib_name.kebab}.component';
        import {{ {lib_name.camel}Routes }} from './lib.routes';
        
        @NgModule({{
          imports: [
            CommonModule,
            RouterModule.forChild({lib_name.camel}Routes),
            MatPaginatorModule,
            MatTableModule,
            MatCheckboxModule,
            MatSortModule,
            ShortDatePipeModule,
            MatIconModule,
            ChipModule,
            TranslocoModule,
            MatTooltipModule,
          ],
          declarations: [{lib_name.pascal}Component],
          exports: [{lib_name.pascal}Component],
        }})
        export class {lib_name.pascal}Module {{}}
        '''
        return file_content

