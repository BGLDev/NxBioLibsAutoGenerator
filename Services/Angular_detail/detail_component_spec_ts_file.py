from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class DetailComponentSpecTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase):
        file_content = f'''
        import {{ HttpClientTestingModule }} from '@angular/common/http/testing';
        import {{ ComponentFixture, TestBed }} from '@angular/core/testing';
        import {{ FormsModule, ReactiveFormsModule }} from '@angular/forms';
        import {{ MatAutocompleteModule }} from '@angular/material/autocomplete';
        import {{ MatCheckboxModule }} from '@angular/material/checkbox';
        import {{ MatFormFieldModule }} from '@angular/material/form-field';
        import {{ MatIconModule }} from '@angular/material/icon';
        import {{ MatInputModule }} from '@angular/material/input';
        import {{ MatSelectModule }} from '@angular/material/select';
        import {{ MatSlideToggleModule }} from '@angular/material/slide-toggle';
        import {{ MatSortModule }} from '@angular/material/sort';
        import {{ MatTableModule }} from '@angular/material/table';
        import {{ NoopAnimationsModule }} from '@angular/platform-browser/animations';
        import {{ RouterTestingModule }} from '@angular/router/testing';
        import {{ MatNativeDateModule }} from '@angular/material/core';
        import {{ MatDatepickerModule }} from '@angular/material/datepicker';
        import {{
          AppConfig,
          getAppConfigProvider,
        }} from '@biolan/biolanglobal/app-config';
        import {{ NoRoundDecimalPipeModule }} from '@biolan/shared/pipes/no-round-decimal';
        import {{ ChipModule }} from '@biolan/shared/ui/chip';
        import {{ TranslocoModule }} from '@ngneat/transloco';
        import {{ {lib_name.pascal}Component }} from './{lib_name.kebab}.component';

        describe('{lib_name.pascal}Component', () => {{
          const appConfig: AppConfig = {{
            production: false,
            apiUrl: 'test-url',
          }};
          let component: {lib_name.pascal}Component;
          let fixture: ComponentFixture<{lib_name.pascal}Component>;

          beforeEach(async () => {{
            await TestBed.configureTestingModule({{
              imports: [
                NoopAnimationsModule,
                HttpClientTestingModule,
                RouterTestingModule,
                ReactiveFormsModule,
                MatInputModule,
                MatFormFieldModule,
                MatAutocompleteModule,
                MatIconModule,
                MatSelectModule,
                TranslocoModule,
                MatCheckboxModule,
                MatDatepickerModule,
                MatNativeDateModule,
                ChipModule,
                MatTableModule,
                MatSortModule,
                MatSlideToggleModule,
                FormsModule,
                NoRoundDecimalPipeModule,
              ],
              declarations: [{lib_name.pascal}Component],
              providers: [getAppConfigProvider(appConfig)],
            }}).compileComponents();

            fixture = TestBed.createComponent({lib_name.pascal}Component);
            component = fixture.componentInstance;
            fixture.detectChanges();
          }});

          it('should create', () => {{
            expect(component).toBeTruthy();
          }});
        }});

        '''
        return file_content

