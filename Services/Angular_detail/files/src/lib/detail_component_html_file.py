from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE, TYPE_ANY
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class DetailHtmlFile:
    
    def __init__(self):
        self.form_columns = {
            TYPE_NUMBER: self._form_data_type_number,
            TYPE_STRING: self._form_data_type_string,
            TYPE_BOOLEAN: self._form_data_type_bool,
            TYPE_FK: self._form_data_type_fk,
            TYPE_DATE: self._form_data_type_date,
            TYPE_ANY: self._form_data_type_string,
        }
        
    def get_file_content(self, params: [Param], module_name: StringCase):
        form_name = f"{module_name.camel}Form"
        file_content = ''
        file_content += self._form_start(form_name)
        for index, param in enumerate(params):
            count = index + 1
            if not count % 2 == 0:
                file_content += f'''
                    <div class="row">
                    '''
            file_content += self.form_columns[param.type](param)
            if count % 2 == 0 or count == len(params):
                file_content += f'''
                    </div>'''
        file_content += self._form_end()
        
        return file_content

    @staticmethod
    def _form_start(form_name: str):
        form_content = f'''
                <form
                  id="detailForm"
                  [formGroup]="{form_name}"
                  #formRef="ngForm"
                  class="form-container"
                >
                '''
        return form_content

    @staticmethod
    def _form_end():
        form_content = f'''
                </form>
                '''
        return form_content

    @staticmethod
    def _form_data_type_number(param: Param):
        param_name = param.name
        form_content = f'''
                        <div class="col">
                          <mat-form-field class="full-width" appearance="outline">
                            <mat-label>{{{{ '{param_name.snake.upper()}' | transloco }}}}</mat-label>
                            <input
                              matInput
                              type="number"
                              formControlName="{param_name.camel}"
                            />
                          </mat-form-field>
                        </div>
                    '''
        return form_content

    @staticmethod
    def _form_data_type_string(param: Param):
        param_name = param.name
        form_content = f'''
                        <div class="col">
                          <mat-form-field class="full-width" appearance="outline">
                            <mat-label>{{{{ '{param_name.snake.upper()}' | transloco }}}}</mat-label>
                            <input
                              matInput
                              type="text"
                              formControlName="{param_name.camel}"
                            />
                          </mat-form-field>
                        </div>
                    '''
        return form_content

    @staticmethod
    def _form_data_type_bool(param: Param):
        param_name = param.name
        form_content = f'''
                        <div class="col">
                          <mat-form-field class="example-full-width" appearance="outline">
                            <mat-label>{{{{ '{param_name.snake.upper()}' | transloco }}}}</mat-label>
                            <mat-select formControlName="{param_name.camel}" #option{param_name.pascal}>
                            <mat-select-trigger >
                                <mat-icon
                                  class="material-symbols-outlined"
                                  [fontIcon]="option{param_name.pascal}.value ? 'done' : 'close'"
                                ></mat-icon>
                                {{{{ globalTranslates.val[option{param_name.pascal}.value ? 'YES' : 'NOT'] }}}}
                            </mat-select-trigger>
                              <mat-option [value]="true">
                                <mat-icon
                                  class="material-symbols-outlined"
                                  fontIcon="done"
                                ></mat-icon>
                                {{{{ globalTranslates.val['YES'] }}}}
                              </mat-option>
                              <mat-option [value]="false">
                                <mat-icon
                                  class="material-symbols-outlined"
                                  fontIcon="close"
                                ></mat-icon>
                                {{{{ globalTranslates.val['NOT'] }}}}
                              </mat-option>
                            </mat-select>
                          </mat-form-field>
                        </div>
                    '''
        return form_content

    @staticmethod
    def _form_data_type_fk(param: Param):
        param_fk_model_name = param.fk_model_name
        param_name = param.name
        form_content = f'''
                        <div class="col">
                            <biolan-input-autocomplete
                                [inputController]="{param_name.camel}"
                                [allOptions$]="all{param_fk_model_name.pascal}FormInputOptions$"
                                [label]="'{param_name.snake.upper()}'"
                                showParam="displayName"
                            ></biolan-input-autocomplete>
                        </div>
                    '''
        return form_content

    @staticmethod
    def _form_data_type_date(param: Param):
        param_name = param.name
        form_content = f'''
                        <div class="col">
                            <mat-form-field class="full-width" appearance="outline">
                              <mat-label>{{{{ '{param_name.snake.upper()}' | transloco }}}}</mat-label>
                              <input
                                matInput
                                [matDatepicker]="picker{param_name.pascal}"
                                formControlName="{param_name.camel}"
                                required
                              />
                              <mat-datepicker-toggle
                                matSuffix
                                [for]="picker{param_name.pascal}"
                              ></mat-datepicker-toggle>
                              <mat-datepicker #picker{param_name.pascal}></mat-datepicker>
                            </mat-form-field>
                        </div>
                    '''
        return form_content
    
    