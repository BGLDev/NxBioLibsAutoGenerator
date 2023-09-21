from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class DataAccessServiceSpecTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase):
        file_content = f'''
        import {{ HttpClientTestingModule }} from '@angular/common/http/testing';
        import {{ TestBed }} from '@angular/core/testing';
        import {{
          AppConfig,
          getAppConfigProvider,
        }} from '@biolan/biolanglobal/app-config';
        
        import {{ {lib_name.pascal}Service }} from './{lib_name.kebab}.service';
        
        describe('{lib_name.pascal}Service', () => {{
          const appConfig: AppConfig = {{
            production: false,
            apiUrl: 'test-url',
          }};
          let service: {lib_name.pascal}Service;
        
          beforeEach(() => {{
            TestBed.configureTestingModule({{
              imports: [HttpClientTestingModule],
              providers: [getAppConfigProvider(appConfig)],
            }});
            service = TestBed.inject({lib_name.pascal}Service);
          }});

          it('should be created', () => {{
            expect(service).toBeTruthy();
          }});
        }});

        '''
        return file_content

