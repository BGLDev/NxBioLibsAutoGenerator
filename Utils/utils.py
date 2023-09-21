import os
import textwrap
import re

from tqdm import tqdm
import yaml
# creacion de carpetas y archivos
PRINT_ACTION_LOG = False
# Puntos de control
PRINT_PROGRES_LOG = True
# Mostrar barra de progreso al final de la ejecucion
SHOW_PROGRES_BAR = False

# CREAR CARPETA
def create_folder(in_path,folder_name):
    new_folder_path = os.path.join(in_path, folder_name)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        action_log_print(f"La carpeta '{folder_name}' ha sido creada en {in_path}.")
    else:
        action_log_print(f"La carpeta '{folder_name}' ya existe en {in_path}.")


# CREAR ARCHIVO
def create_file(in_path,file_name,extension,content):
    new_file_path = os.path.join(in_path, f"{file_name}{extension}")
    with open(new_file_path, "w") as file:
        file.write(content)

    action_log_print(f"El archivo '{file_name}{extension}' ha sido creado  en {in_path}.")


# LEER ARCHIVO YAML
def read_yaml_file(in_path,file_name):
    read_file_path = os.path.join(in_path, f"{file_name}.yaml")
    content = None
    if os.path.exists(read_file_path):
        with open(read_file_path, 'r') as archivo:
            content = yaml.safe_load(archivo)
        action_log_print(f"El archivo '{file_name}.yaml' ha sido creado.")
    else:
        action_log_print(f"El archivo '{file_name}.yaml' no ha sido leido.")
    return content


def read_yaml_file(in_path,file_name):
    read_file_path = os.path.join(in_path, f"{file_name}.yaml")
    content = None
    if os.path.exists(read_file_path):
        with open(read_file_path, 'r') as archivo:
            content = yaml.safe_load(archivo)
        action_log_print(f"El archivo '{file_name}' ha sido creado.")
    else:
        action_log_print(f"El archivo '{file_name}' no ha sido leido.")
    return content


def read_file_content(in_path,file):
    read_file_path = os.path.join(in_path, file)
    if os.path.exists(read_file_path):
        with open(read_file_path, 'r') as archivo:
            return archivo.read()


def delete_tabs_to_text(text):
    return textwrap.dedent(text)


def pascal_case_to_all_cases(pascal_string) -> dict:
    camel = re.sub(r'^\w', lambda x: x.group(0).lower(), pascal_string)
    pascal = pascal_string
    snake = re.sub(r'(?<!^)(?=[A-Z])', '_', pascal_string).lower()
    kebab = re.sub(r'(?<!^)(?=[A-Z])', '-', pascal_string).lower()

    return {'camel': camel, 'pascal': pascal, 'snake': snake, 'kebab': kebab}


def snake_case_to_pascal_case(snake_case):
    return re.sub(r'_([a-zA-Z])', lambda x: x.group(1).upper(), snake_case)


def action_log_print(string):
    if PRINT_ACTION_LOG:
        print(string)


def progres_log_print(string):
    if PRINT_PROGRES_LOG:
        print(string)


def execute_actions_with_progres_bar(lib_name_pascal , actions):
    total_iterations = len(actions)
    pbar = tqdm(total=total_iterations, position=0, leave=SHOW_PROGRES_BAR)
    pbar.set_description(f"{lib_name_pascal}")
    tqdm.write(f"[{lib_name_pascal}] ================================================================================")
    for key, action in actions.items():
        pbar.set_postfix({"file": f"{key}"})
        try:
            action()  # Ejecutar la acción correspondiente......
            tqdm.write(f"   [   \033[32mOK\033[0m   ] : {key}")
        except Exception as e:
            tqdm.write(f"   [ \033[91mERROR!\033[0m ] : {key} \n              \033[91m{e}\033[0m ]")
        finally:
            pbar.update(1)  # Actualizar la barra de progreso
    pbar.set_postfix({"<": f"= COMPLETE"})


def get_path_file_names(path):
    file_names = os.listdir(path)
    return file_names


def file_exist(in_path, file_name, extension):
    file = os.path.join(in_path, f"{file_name}{extension}")
    return os.path.exists(file)