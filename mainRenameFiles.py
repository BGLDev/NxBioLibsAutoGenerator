import os
import re

from Models.string_case import StringCase
from Utils import utils

# Directorio raíz donde se iniciará la búsqueda
proyect_root = "/home/benat/Personal/01 - BIOLAN Proyects/01 - Biolan global/02_biolan_monorepo_front"
folder_root = "/libs/biolanglobal/biotest-plus-pack-assignment"

search = "BioTestAssignment"
replace = "BioTestPlusPackAssignment"

root_directory = f'{proyect_root}{folder_root}'
#root_directory = "/home/benat/Personal/04 - Codigo Automatico/magia_v2_front/__Result/libs/biolanglobal/biosensor7000"


def run(path, search_value, replace_value):
    search_value_name = StringCase(search_value)
    replace_value_name = StringCase(replace_value)

    rename_x_items(path, search_value_name, replace_value_name)


def rename_x_items(path, search_value: StringCase, replace_value: StringCase):
    for root, dirs, files in os.walk(path):
        for item in files:
            item_path = os.path.join(root, item)
            # Si es un archivo
            item_type = ' File '
            item_is_edited = replace_archive_content(item_path, search_value, replace_value)
            item_new_name = rename_item(item, root, item_path, search_value, replace_value)
            console_result(item_type, item_new_name, item_is_edited, item)
        for item in dirs:
            item_path = os.path.join(root, item)
            rename_x_items(item_path, search_value, replace_value)
            item_type = 'Direct'
            item_is_edited = False
            item_new_name = rename_item(item, root, item_path, search_value, replace_value)
            console_result(item_type, item_new_name, item_is_edited, item)


def console_result(item_type, item_new_name, item_is_edited, item):
    type_item = f'[{item_type}]'
    renamed = f'[Change Name]' if item_new_name else f'[ Good Name ]'
    edit = f'[Edited Content]' if item_is_edited else f'[ Good Content ]' if type_item == ' File ' else ''
    print(f'{type_item}{renamed}{edit} : {item}')


def rename_item(item, root, item_path, search_value, replace_value):
    if search_value.kebab in item:
        new_name = item.replace(search_value.kebab, replace_value.kebab)
        new_path = os.path.join(root, new_name)
        os.rename(item_path, new_path)
        return new_name
    return None


def replace_archive_content(file_path,search_value: StringCase, replace_value: StringCase):
    with open(file_path, 'r') as file:
        content = file.read()
    modified_content = content

    for key in vars(search_value).keys():
        attr_search_value = getattr(search_value, key)
        attr_replace_value = getattr(replace_value, key)

        regex = re.compile(re.escape(attr_search_value))
        modified_content = regex.sub(attr_replace_value, modified_content)

    with open(file_path, 'w') as file:
        file.write(modified_content)

    if modified_content not in content:
        return True
    return False
    # print(f"Sustituido en archivo: {file_path}")


run(root_directory, search, replace)

