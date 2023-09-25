from Models.base_config import BaseConfig
from Models.string_case import StringCase
from Services.Angular_data_access.files.data_access_eslintrc_json_file import DataAccessEslintrcJsonFile
from Services.Angular_data_access.files.src.data_access_index_ts_file import DataAccessIndexTsFile
from Services.Angular_data_access.files.data_access_jest_config_ts_file import DataAccessJestConfigTsFile
from Services.Angular_data_access.files.data_access_proyect_json_file import DataAccessProyectJsonFile
from Services.Angular_data_access.files.data_access_readme_md_file import DataAccessReadmeMdFile
from Services.Angular_data_access.files.src.lib.data_access_resolver_spec_ts_file import DataAccessResolverSpecTsFile
from Services.Angular_data_access.files.src.lib.data_access_resolver_ts_file import DataAccessResolverTsFile
from Services.Angular_data_access.files.src.lib.data_access_service_spec_ts_file import DataAccessServiceSpecTsFile
from Services.Angular_data_access.files.src.lib.data_access_service_ts_file import DataAccessServiceTsFile
from Services.Angular_data_access.files.src.data_access_test_setup_ts_file import DataAccessTestSetupTsFile
from Services.Angular_data_access.files.data_access_tsconfig_json_file import DataAccessTsconfigJsonFile
from Services.Angular_data_access.files.data_access_tsconfig_lib_json_file import DataAccessTsconfigLibJsonFile
from Services.Angular_data_access.files.data_access_tsconfig_spec_json_file import DataAccessTsconfigSpecJsonFile

from Utils import utils


class CreateAngularDataAccess:
    def __init__(self, config: BaseConfig):
        self.proyect_origin_path = f"{config.proyect_origin_path}/libs"
        self.scope_name = config.scope  # biolanglobal (StringCase)
        self.module_name = config.django_model_name  # Bio3000 (StringCase)
        self.sub_folder_name = StringCase('data-access')  # Feature (StringCase)
        self.lib_comp_type = StringCase('')  # Detail (StringCase)
        self.lib_user_type = config.user_type  # Internal (StringCase)
        # bio3000-list-internal (StringCase)
        self.lib_name = StringCase(f"{config.django_model_name.kebab}-{config.user_type.kebab}")
        # biolanglobal/bio3000/feature/internal/bio3000-list-internal
        self.lib_path = f"{self.scope_name.kebab}/{self.module_name.kebab}/{self.sub_folder_name.kebab}"
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

            'test-setup.ts':self._create_src_test_setup_ts,

            f'{self.lib_name.kebab}.resolver.spec.ts': self._create_resolver_spec_ts_file,
            f'{self.lib_name.kebab}.resolver.ts': self._create_resolver_ts_file,
            f'{self.lib_name.kebab}.service.spec.ts': self._create_service_spec_ts_file,
            f'{self.lib_name.kebab}.service.ts': self._create_service_ts_file,
        }
        utils.execute_actions_with_progres_bar(f"{self.module_name.pascal}{self.sub_folder_name.pascal}{self.lib_user_type.pascal}", actions)

    def _create_folder_structure(self):
        path_structure = f"{self.lib_path}/src/lib"
        path_structure_list = path_structure.split('/')
        origin_path = f"{self.proyect_origin_path}/"
        for path in path_structure_list:
            utils.create_folder(origin_path, path)
            origin_path += f"{path}/"

    # #####################################################################################
    # module/data-accesss/proyect.json
    # #####################################################################################
    def _create_module_proyect_json(self):
        file_content = DataAccessProyectJsonFile().get_file_content(self.lib_path,self.scope_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'project', '.json', file_content)

    # #####################################################################################
    # module/data-accesss/readme.md
    # #####################################################################################
    def _create_module_readme_md(self):

        file_content = DataAccessReadmeMdFile().get_file_content(self.lib_path)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'README', '.md', file_content)

    # #####################################################################################
    # module/data-accesss/.eslintrc.json
    # #####################################################################################
    def _create_module_eslintrc_json(self):
        file_content = DataAccessEslintrcJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", '.eslintrc', '.json', file_content)

    # #####################################################################################
    # module/data-accesss/jest.config.ts
    # #####################################################################################
    def _create_module_jest_config_ts(self):
        file_content = DataAccessJestConfigTsFile().get_file_content(self.lib_path)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'jest', '.config.ts', file_content)

    # #####################################################################################
    # module/data-accesss/tsconfig.lib.json
    # #####################################################################################
    def _create_module_tsconfig_lib_json(self):
        file_content = DataAccessTsconfigLibJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'tsconfig', '.lib.json', file_content)

    # #####################################################################################
    # module/data-accesss/tsconfig.json
    # #####################################################################################
    def _create_module_tsconfig_json(self):
        file_content = DataAccessTsconfigJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'tsconfig', '.json', file_content)

    # #####################################################################################
    # module/data-accesss/tsconfig.spec.json
    # #####################################################################################
    def _create_module_tsconfig_spec_json(self):
        file_content = DataAccessTsconfigSpecJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'tsconfig', '.spec.json', file_content)

    # #####################################################################################
    # module/data-accesss/src/index.ts
    # #####################################################################################
    def _create_src_index_ts(self):
        file_content = DataAccessIndexTsFile().get_file_content(self.lib_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src", 'index', '.ts', file_content)

    # #####################################################################################
    # module/data-accesss/src/test.setup.ts
    # #####################################################################################
    def _create_src_test_setup_ts(self):
        file_content = DataAccessTestSetupTsFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src", 'test-setup', '.ts', file_content)

    # #####################################################################################
    # module/data-accesss/src/lib/?.resolver.spec.ts
    # #####################################################################################
    def _create_resolver_spec_ts_file(self):
        file_content = DataAccessResolverSpecTsFile().get_file_content(self.lib_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"{self.lib_name.kebab}", '.resolver.spec.ts', file_content)

    # #####################################################################################
    # module/data-accesss/src/lib/?.resolver.ts
    # #####################################################################################
    def _create_resolver_ts_file(self):
        file_content = DataAccessResolverTsFile().get_file_content(self.lib_name, self.module_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"{self.lib_name.kebab}", '.resolver.ts', file_content)

    # #####################################################################################
    # module/data-accesss/src/lib/?.service.spec.ts
    # #####################################################################################
    def _create_service_spec_ts_file(self):
        file_content = DataAccessServiceSpecTsFile().get_file_content(self.lib_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"{self.lib_name.kebab}", '.service.spec.ts', file_content)

    # #####################################################################################
    # module/data-accesss/src/lib/?.service.ts
    # #####################################################################################
    def _create_service_ts_file(self):
        file_content = DataAccessServiceTsFile().get_file_content(self.lib_name, self.module_name, self.lib_user_type)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"{self.lib_name.kebab}", '.service.ts', file_content)

