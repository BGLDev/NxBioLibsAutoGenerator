from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class DataAccessServiceTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase, module_name: StringCase, lib_user_type: StringCase):
        file_content = f'''
        import {{ HttpClient }} from '@angular/common/http';
        import {{ Inject, Injectable }} from '@angular/core';
        import {{ APP_CONFIG, AppConfig }} from '@biolan/biolanglobal/app-config';
        import {{ {module_name.pascal}, ListPage }} from '@biolan/biolanglobal/utils/model';
        import {{
          GlobalHttpService,
          HttpServiceInterface,
        }} from '@biolan/biolanglobal/utils/services/global-http';
        import {{ Filter }} from '@biolan/shared/ui/filter';
        import {{ Observable }} from 'rxjs';
        
        @Injectable({{
          providedIn: 'root',
        }})
        export class {lib_name.pascal}Service implements HttpServiceInterface {{
          endPoint = '{module_name.kebab}-{lib_user_type.kebab}';
          apiUrl = this.appConfig.apiUrl;
        
          constructor(
            @Inject(APP_CONFIG) private appConfig: AppConfig,
            private http: HttpClient,
            private globalHttpService: GlobalHttpService
          ) {{}}
        
          getElement(id: string): Observable<{module_name.pascal}> {{
            return this.globalHttpService.getElement(id, this.endPoint);
          }}
        
          updateElement(id: string, {module_name.camel}: Partial<{module_name.pascal}>): Observable<{module_name.pascal}> {{
            return this.globalHttpService.updateElement(id, {module_name.camel}, this.endPoint);
          }}
        
          deleteElement(id: string): Observable<void> {{
            return this.globalHttpService.deleteElement(id, this.endPoint);
          }}
        
          getElementPage(
            filters: Filter[],
            pageIndex: number,
            pageSize: number,
            sortActive: string,
            sortDirection: 'asc' | 'desc' | ''
          ): Observable<ListPage<{module_name.pascal}[]>> {{
            return this.globalHttpService.getElementPage(
              this.endPoint,
              filters,
              pageIndex,
              pageSize,
              sortActive,
              sortDirection
            );
          }}
        
          getAllElements(
            filters: Filter[] = [],
            sortActive: string = '',
            sortDirection: 'asc' | 'desc' | '' = ''
          ): Observable<{module_name.pascal}[]> {{
            return this.globalHttpService.getAllElements(
              this.endPoint,
              filters,
              sortActive,
              sortDirection
            );
          }}
        
          createElement({module_name.camel}: Partial<{module_name.pascal}>): Observable<{module_name.pascal}> {{
            return this.globalHttpService.createElement({module_name.camel}, this.endPoint);
          }}
        
          bulkDeleteElements(ids: string[]) {{
            return this.globalHttpService.bulkDeleteElements(ids, this.endPoint);
          }}
        }}

        '''
        return file_content

