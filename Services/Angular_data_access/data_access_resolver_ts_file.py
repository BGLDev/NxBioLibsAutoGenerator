from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class DataAccessResolverTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase, module_name: StringCase):
        file_content = f'''
        import {{ Injectable }} from '@angular/core';
        import {{ ActivatedRouteSnapshot, Resolve }} from '@angular/router';
        import {{ {module_name.pascal} }} from '@biolan/biolanglobal/utils/model';
        import {{ Observable }} from 'rxjs';
        import {{ {lib_name.pascal}Service }} from './{lib_name.kebab}.service';
        
        @Injectable({{
          providedIn: 'root',
        }})
        export class {lib_name.pascal}Resolver implements Resolve<{module_name.pascal}> {{
          constructor(private {lib_name.camel}Service: {lib_name.pascal}Service) {{}}
        
          resolve(route: ActivatedRouteSnapshot): Observable<{module_name.pascal}> {{
            return this.{lib_name.camel}Service.getElement(route.params['id']);
          }}
        }}
        '''
        return file_content

