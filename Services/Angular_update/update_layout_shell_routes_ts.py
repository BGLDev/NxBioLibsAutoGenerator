import json

from Models.base_config import BaseConfig
from Utils import utils


class UpdateLayoutShellRoutesTs:
    def __init__(self, config: BaseConfig):
        self.proyect_origin_path = f"{config.proyect_origin_path}/libs"
        self.scope_name = config.scope  # {self.scope_name.kebab} (StringCase)
        self.module_name = config.django_model_name  # Bio3000 (StringCase)
        self.lib_user_type = config.user_type  # Internal (StringCase)
        self.params_read = config.django_model_params_read  # modelo Bio3000
        self.update_file_path = f"{self.scope_name.kebab}/layout/feature/shell/src/lib"

        self.proyect_lib_absolute_path = f"{self.proyect_origin_path}/{self.update_file_path}"
        self.create() # crear todos los archivos

    def create(self):
        actions = {
            f'Update layoutShell lib.routes.ts whit new {self.module_name.kebab} module shell routes': self._add_new_path,

        }
        utils.execute_actions_with_progres_bar(f"LayoutShellRoutes {self.module_name.pascal}{self.lib_user_type.pascal}", actions)

    def _add_new_path(self):
        file_content = utils.read_file_content(self.proyect_lib_absolute_path, f"lib.routes.ts")
        spliter ="children: ["
        parts = file_content.split("children: [")
        if f"path: '{self.module_name.kebab}-{self.lib_user_type.kebab}'" not in parts[1]:
            parts[1]=f'''
      // {self.module_name.snake.upper()}
      {{
        path: '{self.module_name.kebab}-{self.lib_user_type.kebab}',
        canActivate: [AuthGuard],
        loadChildren: () =>
          import(
            '@biolan/{self.scope_name.kebab}/{self.module_name.kebab}/feature/{self.lib_user_type.kebab}/{self.module_name.kebab}-shell-{self.lib_user_type.kebab}'
          ).then((m) => m.{self.module_name.pascal}Shell{self.lib_user_type.pascal}Module),
      }},{parts[1]}
            '''
            new_file_content = "" + spliter.join(parts)
            file_content = utils.delete_tabs_to_text(new_file_content)
            utils.create_file(f"{self.proyect_lib_absolute_path}", 'lib', '.routes.ts', file_content)
