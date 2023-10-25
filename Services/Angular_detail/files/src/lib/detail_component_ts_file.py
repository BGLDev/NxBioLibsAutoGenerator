from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class DetailComponentTsFile:


    def get_file_content(self,lib_name: StringCase, module_name: StringCase, lib_user_type: StringCase, params: [Param]):
        import_services = self._get_fk_imports_services(params,lib_user_type)
        imports_models = self._get_fk_imports_models(params,module_name)
        form_options = self._get_fk_form_options(params, lib_user_type)
        form_group = self._get_form_group(params)
        getters = self._get_getters(params, module_name)
        constructor_services = self._get_fk_constructor_services(params,lib_user_type)
        trasform_backup_form_values = self._trasform_backup_form_values(params)

        file_content = f'''
                import {{ ChangeDetectionStrategy, Component, OnInit, ViewChild }} from '@angular/core';
                import {{ FormBuilder, FormControl, NgForm, Validators }} from '@angular/forms';
                import {{ ActivatedRoute, Router }} from '@angular/router';
                import {{ {module_name.pascal}{lib_user_type.pascal}Service }} from '@biolan/biolanglobal/{module_name.kebab}/data-access';
                import {{ ActionsService }} from '@biolan/biolanglobal/layout/data-access/actions-service';
                import {{ FilterService }} from '@biolan/biolanglobal/layout/data-access/filter-service';
                import {{ {imports_models} }} from '@biolan/biolanglobal/utils/model';
                import {{ ThemingService }} from '@biolan/biolanglobal/layout/data-access/theming-service';
                import {{ GlobalFormDateService, GlobalFormValidatorService }} from '@biolan/biolanglobal/utils/services/global-form';
                import {{ GlobalTranslates }} from '@biolan/biolanglobal/utils/services/global-translations';

                import {{ macRegex }} from '@biolan/shared/utils';
                import * as moment from 'moment';
                {import_services}
                
                @Component({{
                  selector: 'biolan-{lib_name.kebab}',
                  templateUrl: './{lib_name.kebab}.component.html',
                  changeDetection: ChangeDetectionStrategy.OnPush,
                }})
                export class {lib_name.pascal}Component implements OnInit {{
                  @ViewChild('formRef') formRef!: NgForm;
                  {form_options}
                  
                  {module_name.camel}Data!: {module_name.pascal}
                  {module_name.camel}Form = this._fb.group({{
                    id: null,{form_group}
                  }});              
                
                  constructor(
                    private _fb: FormBuilder,
                    private router: Router,
                    private activatedRoute: ActivatedRoute,
                    private filterService: FilterService,
                    private globalFormDateService: GlobalFormDateService,
                    public globalTranslates: GlobalTranslates,
                    public themingService: ThemingService,
                    private globalFormValidatorService: GlobalFormValidatorService,
                    private actionsService: ActionsService,{constructor_services}
                    private {module_name.camel}{lib_user_type.pascal}Service: {module_name.pascal}{lib_user_type.pascal}Service,
                  ) {{
                    this.filterService.showFilter(false);
                    this.actionsService.restart();
                    this.actionsService.configSaveButton({{
                      show: true,
                      action: this.onSubmit.bind(this),
                    }});
                    this.actionsService.configDeleteButton({{
                      show: true,
                      action: this.onDelete.bind(this),
                    }});
                  }}
                
                  get id() {{ return this.{module_name.camel}Form.get('id'); }}{getters}
                
                  ngOnInit(): void {{
                    /* We have access to the {module_name.camel} in the activatedRoute data because we loaded
                    it into the {module_name.camel}{lib_user_type.pascal}Resolver. No need to make another http call */
                    this.activatedRoute.data.subscribe(({{ {module_name.camel} }}) => {{
                      if({module_name.camel}){{
                        this.{module_name.camel}Data = {module_name.camel}
                        this.{module_name.camel}Form.patchValue({module_name.camel});
                      }}
                    }});
                  }}
                
                  onSubmit() {{
                    if (this.formRef.valid) {{
                      const backupFormValue = {{...this.{module_name.camel}Form.value}} as Partial<{module_name.pascal}>;
                      {trasform_backup_form_values}
                      
                      const {module_name.camel} = backupFormValue as Partial<{module_name.pascal}>;
                      
                      const onSubmitAction = {module_name.camel}.id
                        ? this.{module_name.camel}{lib_user_type.pascal}Service
                          .updateElement({module_name.camel}.id.toString(), {module_name.camel})
                        : this.{module_name.camel}{lib_user_type.pascal}Service.createElement({module_name.camel})
                
                      onSubmitAction.subscribe(()=>{{
                        this.router.navigate(['/{module_name.kebab}-{lib_user_type.kebab}']);
                      }});
                    }}
                  }}
                
                  onDelete(): void {{
                    if (this.id?.value) {{
                      this.{module_name.camel}{lib_user_type.pascal}Service.deleteElement(this.id.value)
                        .subscribe(()=>{{
                          this.router.navigate(['/{module_name.kebab}-{lib_user_type.kebab}']);
                        }});
                    }}
                  }}
                }}
            '''
        return file_content

    @staticmethod
    def _get_fk_imports_services(params, lib_user_type):
        fk_services = ''
        for param in params:
            created_fks = []
            if param.type == TYPE_FK:
                if param.fk_model_name.pascal not in created_fks:
                    created_fks.append(param.fk_model_name.pascal)
                    fk_services += f'''
                import {{ {param.fk_model_name.pascal}{lib_user_type.pascal}Service }} from '@biolan/biolanglobal/{param.fk_model_name.kebab}/data-access';'''
        return fk_services

    @staticmethod
    def _get_fk_imports_models(params, module_name):
        created_fks = [module_name.pascal]
        for param in params:
            if param.type == TYPE_FK:
                if param.fk_model_name.pascal not in created_fks:
                    created_fks.append(param.fk_model_name.pascal)

        fk_services = ', '.join(created_fks)
        return fk_services

    @staticmethod
    def _get_fk_form_options(params, lib_user_type):
        fk_options = ''
        for param in params:
            created_fks = []
            if param.type == TYPE_FK:
                if param.fk_model_name.pascal not in created_fks:
                    created_fks.append(param.fk_model_name.pascal)
                    fk_options += f'''
                  all{param.fk_model_name.pascal}FormInputOptions$ = this.{param.fk_model_name.camel}{lib_user_type.pascal}Service.getAllElements();'''
        return fk_options

    @staticmethod
    def _get_fk_constructor_services(params, lib_user_type):
        fk_services = ''
        for param in params:
            created_fks = []
            if param.type == TYPE_FK:
                if param.fk_model_name.pascal not in created_fks:
                    created_fks.append(param.fk_model_name.pascal)
                    fk_services += f'''
                    private {param.fk_model_name.camel}{lib_user_type.pascal}Service: {param.fk_model_name.pascal}{lib_user_type.pascal}Service,'''
        return fk_services

    @staticmethod
    def _get_form_group(params):
        form_group = ''
        for param in params:
            validators = f", {param.form_validators}" if param.form_validators else ''
            form_group += f'''
                    {param.name.camel}: [null{validators}],'''
        return form_group

    @staticmethod
    def _get_getters(params,module_name):
        getters = ''
        for param in params:
            if param.type == TYPE_FK:
                getters += f'''
                  get {param.name.camel}(): FormControl<any>  {{ return this.{module_name.camel}Form.get('{param.name.camel}') as FormControl<any>; }}'''
            else:
                getters += f'''
                  get {param.name.camel}() {{ return this.{module_name.camel}Form.get('{param.name.camel}'); }}'''
        return getters

    @staticmethod
    def _trasform_backup_form_values(params):
        fk_options = ''
        for param in params:
            if param.type == TYPE_FK:
                fk_options += f'''
                      if (backupFormValue.{param.name.camel}) {{
                        backupFormValue.{param.name.camel} = (backupFormValue.{param.name.camel} as {param.fk_model_name.pascal})['id']
                      }}'''

            elif param.type == TYPE_DATE:
                fk_options += f'''
                      if (backupFormValue.{param.name.camel}) {{
                        const {param.name.camel}YYYYMMDD = this.globalFormDateService.backDateFormat(backupFormValue.{param.name.camel})
                        backupFormValue.{param.name.camel} = {param.name.camel}YYYYMMDD
                      }}'''

        return fk_options