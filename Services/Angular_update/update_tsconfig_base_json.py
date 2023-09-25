import json

from Models.base_config import BaseConfig
from Utils import utils


class UpdateTsconfigBase:
    def __init__(self, config: BaseConfig):
        self.proyect_origin_path = f"{config.proyect_origin_path}/tsconfig.base.json"
        self.scope_name = config.scope  # {self.scope_name.kebab} (StringCase)
        self.module_name = config.django_model_name  # Bio3000 (StringCase)
        self.lib_user_type = config.user_type  # Internal (StringCase)
        self.params_read = config.django_model_params_read  # modelo Bio3000

        self.create() # crear todos los archivos

    def create(self):
        actions = {
            f'Update tsconfig.base.ts with new {self.module_name.kebab} module index files': self._add_new_index,

        }
        utils.execute_actions_with_progres_bar(f"tsconfig.base.ts {self.module_name.pascal}{self.lib_user_type.pascal}", actions)

    def _add_new_index(self):
        # Nuevo diccionario de paths a agregar
        nuevos_paths = {
            f"@biolan/{self.scope_name.kebab}/{self.module_name.kebab}/data-access": [
                f"libs/{self.scope_name.kebab}/{self.module_name.kebab}/data-access/src/index.ts"
            ],
            f"@biolan/{self.scope_name.kebab}/{self.module_name.kebab}/feature/{self.lib_user_type.kebab}/{self.module_name.kebab}-detail-{self.lib_user_type.kebab}": [
                f"libs/{self.scope_name.kebab}/{self.module_name.kebab}/feature/{self.lib_user_type.kebab}/{self.module_name.kebab}-detail-{self.lib_user_type.kebab}/src/index.ts"
            ],
            f"@biolan/{self.scope_name.kebab}/{self.module_name.kebab}/feature/{self.lib_user_type.kebab}/{self.module_name.kebab}-list-{self.lib_user_type.kebab}": [
                f"libs/{self.scope_name.kebab}/{self.module_name.kebab}/feature/{self.lib_user_type.kebab}/{self.module_name.kebab}-list-{self.lib_user_type.kebab}/src/index.ts"
            ],
            f"@biolan/{self.scope_name.kebab}/{self.module_name.kebab}/feature/{self.lib_user_type.kebab}/{self.module_name.kebab}-shell-{self.lib_user_type.kebab}": [
                f"libs/{self.scope_name.kebab}/{self.module_name.kebab}/feature/{self.lib_user_type.kebab}/{self.module_name.kebab}-shell-{self.lib_user_type.kebab}/src/index.ts"
            ],
        }

        # Cargar el archivo JSON existente
        with open(self.proyect_origin_path, "r") as archivo:
            contenido_json = json.load(archivo)

        # Agregar los nuevos paths al diccionario "paths"
        contenido_json["compilerOptions"]["paths"].update(nuevos_paths)

        # Ordenar el diccionario "paths" alfabéticamente
        contenido_json["compilerOptions"]["paths"] = {k: v for k, v in
                                                      sorted(contenido_json["compilerOptions"]["paths"].items())}

        # Escribir el archivo JSON actualizado de vuelta en el disco
        with open(self.proyect_origin_path, "w") as archivo:
            json.dump(contenido_json, archivo, indent=2)