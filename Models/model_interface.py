import re

from Constants.config import PARAM_TYPE_INFO, TYPE_FK
from Models.string_case import StringCase


class ModelInterface:

    def get_angular_model(self, params):
        combined_dict = {}
        for paramKey, paramValue in params.items():
            for typeInfoKey, typeInfoValue in PARAM_TYPE_INFO.items():
                fieldTypes = typeInfoValue['fieldType']
                for fieldType in fieldTypes:
                    if fieldType in paramValue:
                        combined_dict[StringCase(paramKey).camel] = typeInfoKey

        return combined_dict


class Param:
    name: StringCase
    type: str
    filter_type: str
    lookup_expr: str
    fk_type: str
    fk_model_name: StringCase

    def __init__(self, param_key, param_value):
        data = self._get_data(param_value)
        self.name = StringCase(param_key)
        self.type = data['type']
        self.filter_type = data['filter_type']
        self.lookup_expr = data['filter_lookup_expr']
        self.form_validators = data.get('form_validators',None)
        self.fk_type = data.get('fk_type', None)
        self.fk_model_name = data.get('fk_model_name', None)

    def _get_data(self, param_value):
        for type_info_key, type_info_value in PARAM_TYPE_INFO.items():
            field_types = type_info_value['field_types']
            for field_type in field_types:
                if field_type in param_value:
                    type_info_value['form_validators'] = self._get_form_validators(param_value)
                    if type_info_value['type'] == TYPE_FK:
                        fk_model_name = StringCase(self._get_fk_model_name(param_value))
                        type_info_value['fk_type'] = f"{TYPE_FK}<{fk_model_name.pascal}>"
                        type_info_value['fk_model_name'] = fk_model_name
                    return type_info_value

    @staticmethod
    def _get_fk_model_name(param_value):
        # Definir la expresión regular para buscar el nombre del modelo
        pattern = r'models\.ForeignKey\(([^,]+), .*'

        # Buscar el nombre del modelo en la cadena
        match = re.search(pattern, param_value)

        return match.group(1).strip() if match else 'ErrorFkModel'

    @staticmethod
    def _get_form_validators(param_value):
        validators = "["
        index = 0

        if "null=True" not in param_value:
            separator = ', ' if index else ''
            validators += f"{separator}Validators.required"
            index += 1

        validators += "]"
        return validators if index else None