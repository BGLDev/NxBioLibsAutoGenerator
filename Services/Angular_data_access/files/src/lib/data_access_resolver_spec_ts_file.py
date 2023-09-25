from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class DataAccessResolverSpecTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase):
        file_content = f'''
        import {{ HttpClientTestingModule }} from '@angular/common/http/testing';
        import {{ TestBed }} from '@angular/core/testing';
        import {{ AppConfig, getAppConfigProvider }} from '@biolan/biolanglobal/app-config';
        
        import {{ GlobalHttpService }} from '@biolan/biolanglobal/utils/services/global-http';
        import {{ {lib_name.pascal}Resolver }} from './{lib_name.kebab}.resolver';
        
        describe('{lib_name.pascal}Resolver', () => {{
          const appConfig: AppConfig = {{
            production: false,
            apiUrl: 'test-url',
          }};
          let resolver: {lib_name.pascal}Resolver;
          let service: GlobalHttpService;
        
          beforeEach(() => {{
            TestBed.configureTestingModule({{
              imports: [HttpClientTestingModule],
              providers: [GlobalHttpService, getAppConfigProvider(appConfig)],
            }});
            resolver = TestBed.inject({lib_name.pascal}Resolver);
          }});
        
          it('should be created', () => {{
            expect(resolver).toBeTruthy();
          }});
        
          it('should use GlobalHttpService', () => {{
            service = TestBed.inject(GlobalHttpService);
            expect(service).toBeTruthy();
          }});
        }});
        '''
        return file_content

