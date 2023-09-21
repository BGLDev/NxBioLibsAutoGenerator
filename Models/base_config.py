from Constants.config import BASE_MODEL_PARAMS
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class BaseConfig:
    def __init__(self):
        data = utils.read_yaml_file('./', 'base_config')
        bc_params = {**data['DJANGO_MODEL_PARAMS'], **BASE_MODEL_PARAMS} \
            if StringCase(data['DJANGO_MODEL_EXTENDS']).pascal == 'BaseModel' else data['DJANGO_MODEL_PARAMS']
        self.data = data
        self.proyect_origin_path = f"{data['PROYECT_ORIGIN_PATH']}"
        self.scope = StringCase(data['SCOPE'])
        self.user_type = StringCase(data['USER_TYPE'])
        self.django_model_name = StringCase(data['DJANGO_MODEL_NAME'])
        self.django_model_extends = StringCase(data['DJANGO_MODEL_EXTENDS'])
        self.django_model_params_read = self._get_params(bc_params)
        self.django_model_params_write = self._get_params(data['DJANGO_MODEL_PARAMS'])

    @staticmethod
    def _get_params(bc_params):
        params = []
        for key,value in bc_params.items():
            params.append(Param(key, value))
        return params