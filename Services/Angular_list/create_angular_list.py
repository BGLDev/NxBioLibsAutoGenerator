from Models.base_config import BaseConfig
from Models.string_case import StringCase
from Services.Angular_list.files.src.lib.list_component_spec_ts_file import ListComponentSpecTsFile
from Services.Angular_list.files.src.lib.list_component_ts_file import ListComponentTsFile
from Services.Angular_list.files.src.lib.list_datasource_ts_file import ListDatasourceTsFile
from Services.Angular_list.files.list_eslintrc_json_file import ListEslintrcJsonFile
from Services.Angular_list.files.src.lib.list_filter_ts_file import ListFilterTsFile
from Services.Angular_list.files.src.lib.list_component_html_file import ListHtmlFile
from Services.Angular_list.files.src.list_index_ts_file import ListIndexTsFile
from Services.Angular_list.files.list_jest_config_ts_file import ListJestConfigTsFile
from Services.Angular_list.files.src.lib.list_module_ts_file import ListModuleTsFile
from Services.Angular_list.files.list_proyect_json_file import ListProyectJsonFile
from Services.Angular_list.files.list_readme_md_file import ListReadmeMdFile
from Services.Angular_list.files.src.lib.list_routes_ts_file import ListRoutesTsFile
from Services.Angular_list.files.src.list_test_setup_ts_file import ListTestSetupTsFile
from Services.Angular_list.files.list_tsconfig_json_file import ListTsconfigJsonFile
from Services.Angular_list.files.list_tsconfig_lib_json_file import ListTsconfigLibJsonFile
from Services.Angular_list.files.list_tsconfig_spec_json_file import ListTsconfigSpecJsonFile
from Utils import utils


class CreateAngularList:
    def __init__(self, config: BaseConfig):
        self.proyect_origin_path = f"{config.proyect_origin_path}/libs"
        self.scope_name = config.scope  # biolanglobal (StringCase)
        self.module_name = config.django_model_name  # Bio3000 (StringCase)
        self.sub_folder_name = StringCase('feature')  # Feature (StringCase)
        self.lib_comp_type = StringCase('list')  # List (StringCase)
        self.lib_user_type = config.user_type  # Internal (StringCase)
        # bio3000-list-internal (StringCase)
        self.lib_name = StringCase(f"{config.django_model_name.kebab}-{self.lib_comp_type.kebab}-{config.user_type.kebab}")
        # biolanglobal/bio3000/feature/internal/bio3000-list-internal
        self.lib_path = f"{self.scope_name.kebab}/{self.module_name.kebab}/{self.sub_folder_name.kebab}/{self.lib_user_type.kebab}/{self.lib_name.kebab}"
        self.params_read = config.django_model_params_read  # modelo Bio3000
        self.params_write = config.django_model_params_write  # modelo Bio3000

        self.proyect_lib_absolute_path = f"{self.proyect_origin_path}/{self.lib_path}"

        # crear todos los archivos
        self.create()

    def create(self):
        actions = {
            'Folders': self._create_folder_structure,
            'proyect.json': self._create_module_proyect_json,
            'README.md': self._create_module_readme_md,
            'index.ts': self._create_src_index_ts,

            '.eslintrc.json': self._create_module_eslintrc_json,
            'jest.config.ts': self._create_module_jest_config_ts,
            'tsconfig.json': self._create_module_tsconfig_json,
            'tsconfig.lib.json': self._create_module_tsconfig_lib_json,
            'tsconfig.spec.json': self._create_module_tsconfig_spec_json,

            'test-setup.ts': self._create_src_test_setup_ts,

            f'{self.lib_name.kebab}.component.html': self._create_component_html_file,
            f'{self.lib_name.kebab}.component.spec.ts': self._create_component_spec_ts_file,
            f'{self.lib_name.kebab}.component.ts': self._create_component_ts_file,
            f'{self.lib_name.kebab}.datasource.ts': self._create_datasource_ts_file,
            f'{self.lib_name.kebab}.filter.ts': self._create_filter_ts_file,
            f'{self.lib_name.kebab}.module.ts': self._create_module_ts_file,
            'lib.routes.ts': self._create_routes_ts_file,
        }
        utils.execute_actions_with_progres_bar(self.lib_name.pascal, actions)

    def _create_folder_structure(self):
        path_structure = f"{self.lib_path}/src/lib"
        path_structure_list = path_structure.split('/')
        origin_path = f"{self.proyect_origin_path}/"
        for path in path_structure_list:
            utils.create_folder(origin_path, path)
            origin_path += f"{path}/"

    def _create_module_proyect_json(self):

        file_content = ListProyectJsonFile().get_file_content(self.lib_path, self.module_name, self.sub_folder_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'project', '.json', file_content)

    def _create_module_readme_md(self):

        file_content = ListReadmeMdFile().get_file_content(self.lib_path)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'README', '.md', file_content)

    def _create_module_eslintrc_json(self):
        file_content = ListEslintrcJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", '.eslintrc', '.json', file_content)

    def _create_module_jest_config_ts(self):
        file_content = ListJestConfigTsFile().get_file_content(self.lib_path)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'jest', '.config.ts', file_content)

    def _create_module_tsconfig_lib_json(self):
        file_content = ListTsconfigLibJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'tsconfig', '.lib.json', file_content)

    def _create_module_tsconfig_json(self):
        file_content = ListTsconfigJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'tsconfig', '.json', file_content)

    def _create_module_tsconfig_spec_json(self):
        file_content = ListTsconfigSpecJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'tsconfig', '.spec.json', file_content)

    def _create_src_index_ts(self):
        # file_content = f'''
        #        export * from './lib/{self.lib_name.kebab}.module';
        #        export * from './lib/lib.routes';
        #        '''
        file_content = ListIndexTsFile().get_file_content(self.lib_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src", 'index', '.ts', file_content)

    def _create_src_test_setup_ts(self):
        # file_content = f'''
        #        export * from './lib/{self.lib_name.kebab}.resolver';
        #        export * from './lib/{self.lib_name.kebab}.service';
        #        '''
        file_content = ListTestSetupTsFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src", 'test-setup', '.ts', file_content)
    def _create_component_html_file(self):
        file_content = ListHtmlFile().get_file_content(self.params_write, self.module_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"{self.lib_name.kebab}", '.component.html', file_content)

    def _create_component_spec_ts_file(self):
        file_content = ListComponentSpecTsFile().get_file_content(self.lib_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"{self.lib_name.kebab}", '.component.spec.ts', file_content)

    def _create_component_ts_file(self):
        file_content = ListComponentTsFile().get_file_content(self.lib_name, self.module_name, self.lib_user_type, self.params_write)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"{self.lib_name.kebab}", '.component.ts', file_content)

    def _create_datasource_ts_file(self):
        file_content = ListDatasourceTsFile().get_file_content(self.lib_name, self.module_name, self.lib_user_type, self.scope_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"{self.lib_name.kebab}", '.datasource.ts', file_content)

    def _create_filter_ts_file(self):
        file_content = ListFilterTsFile().get_file_content(self.lib_name,self.params_write, self.lib_user_type, self.scope_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"{self.lib_name.kebab}", '.filter.ts', file_content)

    def _create_module_ts_file(self):
        file_content = ListModuleTsFile().get_file_content(self.lib_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"{self.lib_name.kebab}", '.module.ts', file_content)

    def _create_routes_ts_file(self):
        file_content = ListRoutesTsFile().get_file_content(self.lib_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"lib", '.routes.ts', file_content)
