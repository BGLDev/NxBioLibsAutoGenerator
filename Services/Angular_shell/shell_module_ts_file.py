from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class ShellModuleTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase):
        file_content = f'''
        import {{ CommonModule }} from '@angular/common';
        import {{ NgModule }} from '@angular/core';
        import {{ RouterModule }} from '@angular/router';
        import {{ {lib_name.camel}Routes }} from './lib.routes';
        
        @NgModule({{
          imports: [
            CommonModule,
            RouterModule.forChild({lib_name.camel}Routes),
          ],
        }})
        export class {lib_name.pascal}Module {{}}
        '''
        return file_content

