from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class ListFilterTsFile:

    def get_file_content(self, lib_name: StringCase, params: [Param], lib_user_type: StringCase, scope_name: StringCase):
        imports_content = self._imports(params, lib_user_type, scope_name)
        constructor_content = self._constructor(params, lib_user_type)
        filter_criterions = self._filter_criterions(params, lib_user_type)
        file_content = f'''
            {imports_content}
            
            @Injectable({{
                providedIn: 'root',
            }})
            export class {lib_name.pascal}FilterCriterias{{
                constructor({constructor_content}
                ){{}}
                filterCriteria: FilterCriterion[] = [{filter_criterions}
                ]
            }}
            '''
        return file_content

    @staticmethod
    def _imports(params: [Param], lib_user_type: StringCase, scope_name: StringCase):
        imports_content = f'''
            import {{ Injectable }} from '@angular/core';
            import {{ FilterCriterion }} from '@biolan/shared/ui/filter';
            '''
        created_fks = []
        for param in params:
            if param.type == TYPE_FK:
                if param.fk_model_name.pascal not in created_fks:
                    created_fks.append(param.fk_model_name.pascal)
                    imports_content += f'''
            import {{ {param.fk_model_name.pascal}{lib_user_type.pascal}Service }} from '@biolan/{scope_name.kebab}/{param.fk_model_name.kebab}/data-access';'''

        return imports_content

    @staticmethod
    def _constructor(params: [Param], lib_user_type: StringCase):
        constructor_content = ''
        created_fks = []
        for param in params:
            if param.type == TYPE_FK:
                if param.fk_model_name.pascal not in created_fks:
                    created_fks.append(param.fk_model_name.pascal)
                    constructor_content += f'''
                    private {param.fk_model_name.camel}{lib_user_type.pascal}Service: {param.fk_model_name.pascal}{lib_user_type.pascal}Service,'''

        return constructor_content

    @staticmethod
    def _filter_criterions( params: [Param], lib_user_type: StringCase):
        filter_criterions_content = ''
        for param in params:
            if param.type == TYPE_FK:
                filter_criterions_content += f'''
                    {{
                        name: '{param.name.snake.upper()}',
                        placeholder: 'Search by {param.name.snake}',
                        queryKey: '{param.name.snake}__{param.fk_model_name.snake}',
                        type: '{param.filter_type.lower()}',
                        optionTypeData:{{options:this.{param.fk_model_name.camel}{lib_user_type.pascal}Service.getAllElements(),showParam:'displayName',sendParam:'id'}}
                    }},'''
            else:
                filter_criterions_content += f'''
                    {{
                        name: '{param.name.snake.upper()}',
                        placeholder: 'Search by {param.name.snake}',
                        queryKey: '{param.name.snake}',
                        type: '{param.filter_type.lower()}',
                    }},'''
        return filter_criterions_content



