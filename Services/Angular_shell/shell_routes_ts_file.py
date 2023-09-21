from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class ShellRoutesTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase, module_name: StringCase, lib_user_type: StringCase, scope_name: StringCase):
        file_content = f'''
        import {{ Data, Route }} from '@angular/router';
        import {{ {module_name.pascal}{lib_user_type.pascal}Resolver }} from '@biolan/{scope_name.kebab}/{module_name.kebab}/data-access';
        import {{ AuthGuard }} from '@biolan/biolanglobal/utils/guard';

        export const {lib_name.camel}Routes: Route[] = [
          {{
            path: '',
            canActivate: [AuthGuard],
            loadChildren: () =>
              import(
                '@biolan/{scope_name.kebab}/{module_name.kebab}/feature/{lib_user_type.kebab}/{module_name.kebab}-list-{lib_user_type.kebab}'
              ).then((m) => m.{module_name.pascal}List{lib_user_type.pascal}Module),
            data: {{
              breadcrumb: {{
                alias: '{module_name.snake.upper()}',
                translatable: true,
              }},
            }},
          }},
          {{
            path: 'new',
            canActivate: [AuthGuard],
            loadChildren: () =>
              import(
                '@biolan/{scope_name.kebab}/{module_name.kebab}/feature/{lib_user_type.kebab}/{module_name.kebab}-detail-{lib_user_type.kebab}'
              ).then((m) => m.{module_name.pascal}Detail{lib_user_type.pascal}Module),
            data: {{
              breadcrumb: {{ alias: 'NEW_{module_name.snake.upper()}', translatable: true }},
            }},
          }},
          {{
            path: ':id',
            canActivate: [AuthGuard],
            loadChildren: () =>
              import(
                '@biolan/{scope_name.kebab}/{module_name.kebab}/feature/{lib_user_type.kebab}/{module_name.kebab}-detail-{lib_user_type.kebab}'
              ).then((m) => m.{module_name.pascal}Detail{lib_user_type.pascal}Module),
            data: {{
              // Gets data from resolver
              breadcrumb: (data: Data) =>
                data['{module_name.camel}'].displayName
                  ? `${{data['{module_name.camel}'].displayName}}`
                  : `${{data['{module_name.camel}'].id}}`,
            }},
            resolve: {{ {module_name.camel}: {module_name.pascal}{lib_user_type.pascal}Resolver }},
          }},
        ];

        '''
        return file_content

