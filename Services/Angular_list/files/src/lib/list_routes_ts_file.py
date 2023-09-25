from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class ListRoutesTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase):
        file_content = f'''
        import {{ Route }} from '@angular/router';
        import {{ {lib_name.pascal}Component }} from './{lib_name.kebab}.component';
        
        export const {lib_name.camel}Routes: Route[] = [
          {{ path: '', component: {lib_name.pascal}Component }},
        ];
        '''
        return file_content

