from Models.base_config import BaseConfig
from Models.string_case import StringCase
from Services.Angular_shell.files.shell_eslintrc_json_file import ShellEslintrcJsonFile
from Services.Angular_shell.files.src.shell_index_ts_file import ShellIndexTsFile
from Services.Angular_shell.files.shell_jest_config_ts_file import ShellJestConfigTsFile
from Services.Angular_shell.files.src.lib.shell_module_ts_file import ShellModuleTsFile
from Services.Angular_shell.files.shell_proyect_json_file import ShellProyectJsonFile
from Services.Angular_shell.files.shell_readme_md_file import ShellReadmeMdFile
from Services.Angular_shell.files.src.lib.shell_routes_ts_file import ShellRoutesTsFile
from Services.Angular_shell.files.src.shell_test_setup_ts_file import ShellTestSetupTsFile
from Services.Angular_shell.files.shell_tsconfig_json_file import ShellTsconfigJsonFile
from Services.Angular_shell.files.shell_tsconfig_lib_json_file import ShellTsconfigLibJsonFile
from Services.Angular_shell.files.shell_tsconfig_spec_json_file import ShellTsconfigSpecJsonFile
from Utils import utils


class CreateDjangoFiles:
    def __init__(self, config: BaseConfig):
        self.proyect_origin_path = f"{config.proyect_origin_path}/libs"
        self.scope_name = config.scope  # biolanglobal (StringCase)
        self.module_name = config.django_model_name  # Bio3000 (StringCase)
        self.sub_folder_name = StringCase('feature')  # Feature (StringCase)
        self.lib_comp_type = StringCase('shell')  # Shell (StringCase)
        self.lib_user_type = config.user_type  # Internal (StringCase)
        # bio3000-list-internal (StringCase)
        self.lib_name = StringCase(f"{config.django_model_name.kebab}-{self.lib_comp_type.kebab}-{config.user_type.kebab}")
        # biolanglobal/bio3000/feature/internal/bio3000-list-internal
        self.lib_path = f"{self.scope_name.kebab}/{self.module_name.kebab}/{self.sub_folder_name.kebab}/{self.lib_user_type.kebab}/{self.lib_name.kebab}"

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
        # file_content = f'''
        #        {{
        #          "name": "{self.lib_path.replace('/','-')}",
        #          "$schema": "../../../../../../node_modules/nx/schemas/project-schema.json",
        #          "projectType": "library",
        #          "sourceRoot": "libs/{self.lib_path}/src",
        #          "prefix": "biolan",
        #          "targets": {{
        #            "test": {{
        #              "executor": "@nrwl/jest:jest",
        #              "outputs": ["{{workspaceRoot}}/coverage/{{projectRoot}}"],
        #              "options": {{
        #                "jestConfig": "libs/{self.lib_path}/jest.config.ts",
        #                "passWithNoTests": true
        #              }}
        #            }},
        #            "lint": {{
        #              "executor": "@nrwl/linter:eslint",
        #              "outputs": ["{{options.outputFile}}"],
        #              "options": {{
        #                "lintFilePatterns": [
        #                  "libs/{self.lib_path}/**/*.ts",
        #                  "libs/{self.lib_path}/**/*.html"
        #                ]
        #              }}
        #            }}
        #          }},
        #          "tags": ["scope:{self.scope_name.kebab}", "type:{self.sub_folder_name.kebab }"]
        #        }}
        #        '''
        file_content = ShellProyectJsonFile().get_file_content(self.lib_path, self.module_name, self.sub_folder_name)

        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'project', '.json', file_content)

    def _create_module_readme_md(self):
        # file_content = f'''
        #         Shell libraries always take care of the routing of its scope.
        #
        #         In shell libraries you will find:
        #
        #         - {self.lib_name.kebab}.module.ts
        #         - lib.routes.ts
        #         - ./src/index.ts
        #
        #         # {self.lib_name.kebab}.module.ts
        #
        #         In the layout shell library we already set a .forRoot() module set, in this case <b>layout/shellRoutes</b>, that is the default base router.
        #
        #         So in this library's module, the main goal is to import RouterModule and set the child routes defined in <b>{self.lib_name.camel}Routes</b>
        #
        #         # lib.routes.ts
        #
        #         In this file we define the child routes of '{self.module_name.kebab}-{self.lib_user_type.kebab}/', set in the <b>layout/shellRoutes</b>. In this library we just have 3 child paths.
        #
        #         IMPORTANT: pay attention to the data section
        #
        #         # index.ts
        #
        #         In this file we export both routes and module
        #         '''
        file_content = ShellReadmeMdFile().get_file_content(self.lib_name, self.module_name, self.lib_user_type)

        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'README', '.md', file_content)

    def _create_module_eslintrc_json(self):
        file_content = ShellEslintrcJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", '.eslintrc', '.json', file_content)

    def _create_module_jest_config_ts(self):
        file_content = ShellJestConfigTsFile().get_file_content(self.lib_path)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'jest', '.config.ts', file_content)

    def _create_module_tsconfig_lib_json(self):
        file_content = ShellTsconfigLibJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'tsconfig', '.lib.json', file_content)

    def _create_module_tsconfig_json(self):
        file_content = ShellTsconfigJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'tsconfig', '.json', file_content)

    def _create_module_tsconfig_spec_json(self):
        file_content = ShellTsconfigSpecJsonFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}", 'tsconfig', '.spec.json', file_content)

    def _create_src_index_ts(self):
        # file_content = f'''
        #        export * from './lib/{self.lib_name.kebab}.module';
        #        export * from './lib/lib.routes';
        #        '''
        file_content = ShellIndexTsFile().get_file_content(self.lib_name)

        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src", 'index', '.ts', file_content)

    def _create_src_test_setup_ts(self):
        # file_content = f'''
        #        export * from './lib/{self.lib_name.kebab}.resolver';
        #        export * from './lib/{self.lib_name.kebab}.service';
        #        '''
        file_content = ShellTestSetupTsFile().get_file_content()
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src", 'test-setup', '.ts', file_content)
    def _create_module_ts_file(self):
        file_content = ShellModuleTsFile().get_file_content(self.lib_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"{self.lib_name.kebab}", '.module.ts', file_content)

    def _create_routes_ts_file(self):
        file_content = ShellRoutesTsFile().get_file_content(self.lib_name, self.module_name, self.lib_user_type, self.scope_name)
        file_content = utils.delete_tabs_to_text(file_content)
        utils.create_file(f"{self.proyect_lib_absolute_path}/src/lib", f"lib", '.routes.ts', file_content)
