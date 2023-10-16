from Models.base_config import BaseConfig
from Services.Angular_data_access.create_angular_data_access import CreateAngularDataAccess
from Services.Angular_detail.create_angular_detail import CreateAngularDetail
from Services.Angular_list.create_angular_list import CreateAngularList
from Services.Angular_shell.create_angular_shell import CreateAngularShell
from Services.Angular_update.create_utils_model_ts import CreateUtilsModel
from Services.Angular_update.update_layout_shell_routes_ts import UpdateLayoutShellRoutesTs
from Services.Angular_update.update_tsconfig_base_json import UpdateTsconfigBase

base_config = BaseConfig()

respuesta = input(f"¿Crear Modulo {base_config.django_model_name.pascal}? (Y/N): ").strip().lower()
if respuesta == "y":
    CreateAngularDataAccess(base_config)
    CreateAngularList(base_config)
    CreateAngularDetail(base_config)
    CreateAngularShell(base_config)

    CreateUtilsModel(base_config)
    UpdateTsconfigBase(base_config)
    UpdateLayoutShellRoutesTs(base_config)


elif respuesta == "n":
    print(f"Cancelada la creacion del Modulo {base_config.django_model_name.pascal}.")
else:
    print("Respuesta inválida.")