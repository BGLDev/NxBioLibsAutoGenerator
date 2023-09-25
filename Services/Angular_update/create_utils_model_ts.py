import re

from Constants.config import TYPE_FK
from Models.base_config import BaseConfig
from Utils import utils


class CreateUtilsModel:
    def __init__(self, config: BaseConfig):
        self.proyect_origin_path = f"{config.proyect_origin_path}/libs"
        self.scope_name = config.scope  # biolanglobal (StringCase)
        self.module_name = config.django_model_name  # Bio3000 (StringCase)
        self.params_read = config.django_model_params_read  # modelo Bio3000
        self.models_path = f"{self.scope_name.kebab}/utils/model"

        self.proyect_lib_absolute_path = f"{self.proyect_origin_path}/{self.models_path}"

        self.create() # crear todos los archivos

    def create(self):
        actions = {
            'Folders': self._create_folder_structure,
            'proyect.json': self._create_module_proyect_json,
            'README.md': self._create_module_readme_md,
            'index.ts': self._create_src_index_ts,
        }
        utils.execute_actions_with_progres_bar(f"UtilsModel Base Sctructure Check/Create For {self.module_name.pascal}", actions)
        all_models_path_dict = self.get_all_models_path_dict()
        interface_exist = all_models_path_dict.get(self.module_name.pascal, None)
        actions = {}
        if not interface_exist:
            update_model = self.has_related_model()
            if update_model:
                actions[f"Update file {update_model}.model.ts with {self.module_name.pascal} Interface"] = self.update_file
            else:
                actions[f"Create file {self.module_name.kebab}.model.ts with {self.module_name.pascal} Interface"] = self.create_file
                actions[f"Update model\\index.ts with {self.module_name.kebab}.model"] = self._update_new_model_index_ts

        # if not all_models_path_dict.get('fk', None):
        #     actions[f"Create file fk.model.ts with FK Type"] = self._create_fk_model_file
        #     actions["Update model\\index.ts with fk.model"] = self._update_fk_model_index_ts

        utils.execute_actions_with_progres_bar(f"UtilsModel {self.module_name.pascal}", actions)

    def _create_folder_structure(self):
        path_structure = f"{self.models_path}/src/lib"
        path_structure_list = path_structure.split('/')
        origin_path = f"{self.proyect_origin_path}/"
        for path in path_structure_list:
            utils.create_folder(origin_path, path)
            origin_path += f"{path}/"

    def _create_module_proyect_json(self):
        file_content = f'''
               {{
                  "name": "{self.scope_name.kebab}-utils-model",
                  "$schema": "../../../../node_modules/nx/schemas/project-schema.json",
                  "projectType": "library",
                  "sourceRoot": "libs/{self.scope_name.kebab}/utils/model/src",
                  "prefix": "biolan",
                  "targets": {{
                    "lint": {{
                      "executor": "@nrwl/linter:eslint",
                      "outputs": ["{{options.outputFile}}"],
                      "options": {{
                        "lintFilePatterns": [
                          "libs/{self.scope_name.kebab}/utils/model/**/*.ts",
                          "libs/{self.scope_name.kebab}/utils/model/**/*.html"
                        ]
                      }}
                    }}
                  }},
                  "tags": ["scope:{self.scope_name.kebab}", "type:model"]
                }}
               '''
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'project', '.json', file_content)

    def _create_module_readme_md(self):
        file_content = f'''                
                # {self.scope_name.kebab}-utils-model

                This library was generated with [Nx](https://nx.dev).
                
                ## Running unit tests
                
                Run `nx test {self.scope_name.kebab}-utils-model` to execute the unit tests.

                '''
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'README', '.md', file_content)

    def _create_src_index_ts(self):
        file_content = f''''''
        file_content = utils.delete_tabs_to_text(file_content)
        if not utils.file_exist(f"{self.proyect_lib_absolute_path}/src", 'index', '.ts'):
            utils.create_file(f"{self.proyect_lib_absolute_path}/src", 'index', '.ts', file_content)

    def get_all_models_path_dict(self):
        models_origin_path = f"{self.proyect_lib_absolute_path}/src/lib"
        regex = r"export interface (\w+) {"
        spliter = '.model.ts'

        files = utils.get_path_file_names(models_origin_path)
        all_models = {}
        for file in files:
            file_content = utils.read_file_content(models_origin_path,file)
            model_names = re.findall(regex, file_content)
            for model_name in model_names:
                all_models[model_name] = file.split(spliter)[0]
        return all_models

    def has_related_model(self):
        spliter = '.model.ts'
        files = utils.get_path_file_names(f"{self.proyect_lib_absolute_path}/src/lib")
        file_names = [file.split(spliter)[0] for file in files]
        best_match = None
        highest_match = 0

        input_parts = self.module_name.kebab.split('-')
        input_first_word = input_parts[0]

        for item in file_names:
            item_parts = item.split('-')
            item_first_word = item_parts[0]

            if input_first_word == item_first_word:
                match_count = 0

                for input_part, item_part in zip(input_parts, item_parts):
                    if input_part == item_part:
                        match_count += 1
                    else:
                        break

                if match_count > highest_match:
                    best_match = f"{item}"
                    highest_match = match_count

        return best_match

    def create_file(self):
        all_models_path_dict = self.get_all_models_path_dict()

        imports_content = self._get_model_imports("", all_models_path_dict)
        export_content = self._get_model_exports("")

        model_content = f"{imports_content}\n\n{export_content}"
        file_content = utils.delete_tabs_to_text(model_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f'{self.module_name.kebab}', '.model.ts', file_content)

    def update_file(self):
        update_model = self.has_related_model()
        all_models_path_dict = self.get_all_models_path_dict()

        models_origin_path = f"{self.proyect_lib_absolute_path}/src/lib"
        file_content = utils.read_file_content(models_origin_path, f"{update_model}.model.ts")
        parts = file_content.split("export interface ")

        if len(parts) > 1:
            old_imports = parts[0]
            old_exports = "export interface " + "export interface ".join(parts[1:])
        else:
            old_imports = file_content
            old_exports = ""

        imports_content = self._get_model_imports(old_imports, all_models_path_dict)
        export_content = self._get_model_exports(old_exports)

        model_content = f"{imports_content}\n\n{export_content}"
        file_content = utils.delete_tabs_to_text(model_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f'{update_model}', '.model.ts', file_content)

    def _get_model_imports(self, old_imports, all_models_path_dict):
        regex_import = r"import { ([^}]+) } from '[^']+';"
        matches_import = re.findall(regex_import, old_imports)

        # diccionario de todas las importaciones necesarias
        all_imports_dict = {}

        # Añade las importaciones existentes
        for match in matches_import:
            for item in match.split(", "):
                class_name, alias = item.split(" as ") if " as " in item else (item, item)
                all_imports_dict[class_name] = all_models_path_dict[alias] if not class_name == 'FK' else 'fk'
        # Añade las importaciones no existentes
        for param in self.params_read:
            if param.type == TYPE_FK:
                if not all_imports_dict.get('FK', None):
                    all_imports_dict['FK'] = 'fk'

                if not all_imports_dict.get(param.fk_model_name.pascal, None):
                    if all_models_path_dict.get(param.fk_model_name.pascal, None):
                        all_imports_dict[param.fk_model_name.pascal] = all_models_path_dict.get(param.fk_model_name.pascal, None)
                    else:
                        print(f'   \033[91;93mNo existe el modelo => {param.fk_model_name.pascal}\033[0m')

        # agrupa las importaciones por archivos
        all_group_imports = {}
        for key, value in all_imports_dict.items():
            if all_group_imports.get(value, None):
                all_group_imports[value].append(key)
            else:
                all_group_imports[value] = [key]

        # crea el contenido de las importaciones
        inports_content = ''
        for key, value in all_group_imports.items():
            if key == 'fk':
                inports_content += f'''
                import {{ FK }} from '@biolan/biolanglobal/utils/type';'''
            else:
                inports_content += f'''
                import {{ {', '.join(value)} }} from './{key}.model';'''

        return utils.delete_tabs_to_text(inports_content)

    def _get_model_exports(self, old_exports):
        new_export_content = self._get_new_model_export()
        export_content = f"{old_exports}{new_export_content}"
        return export_content

    def _get_new_model_export(self):
        model_content = ''
        for param in self.params_read:
            param_type = param.type if not param.type == TYPE_FK else param.fk_type
            model_content += f'''
              {param.name.camel}: {param_type}'''
        export_content = f'''
            export interface {self.module_name.pascal} {{{model_content}
            }}
            '''
        return utils.delete_tabs_to_text(export_content)

    # def _create_fk_model_file(self):
    #     model_content = "export type FK<T> = string | T;"
    #     new_model_file_name = 'fk'
    #     file_content = utils.delete_tabs_to_text(model_content)
    #     utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", new_model_file_name, '.model.ts', file_content)

    def _update_new_model_index_ts(self):
        new_model_file_name = self.module_name.kebab
        self._update_model_index_ts(new_model_file_name)

    # def _update_fk_model_index_ts(self):
    #     new_model_file_name = 'fk'
    #     self._update_model_index_ts(new_model_file_name)

    def _update_model_index_ts(self,new_model_file_name):
        models_origin_path = f"{self.proyect_lib_absolute_path}/src"
        file_content = utils.read_file_content(models_origin_path, 'index.ts')
        if f"export * from './lib/{new_model_file_name}.model'" not in file_content:
            index_content = f"{file_content}export * from './lib/{new_model_file_name}.model';\n"
            file_content = utils.delete_tabs_to_text(index_content)
            utils.create_file(models_origin_path, 'index', '.ts', file_content)