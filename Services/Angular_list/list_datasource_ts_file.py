from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class ListDatasourceTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase, module_name: StringCase, lib_user_type: StringCase, scope_name: StringCase):
        file_content = f'''
        import {{ DataSource }} from '@angular/cdk/collections';
        import {{ {module_name.pascal}{lib_user_type.pascal}Service }} from '@biolan/{scope_name.kebab}/{module_name.kebab}/data-access';
        import {{ {module_name.pascal}, ListPage }} from '@biolan/{scope_name.kebab}/utils/model';
        import {{ Filter }} from '@biolan/shared/ui/filter';
        import {{ BehaviorSubject, Observable }} from 'rxjs';
        
        export class {lib_name.pascal}DataSource implements DataSource<{module_name.pascal}> {{
          // BehaviorSubject: is an observable that emits the current value to new subscribers
          private _data$ = new BehaviorSubject<{module_name.pascal}[]>([]);
          data!: {module_name.pascal}[];
          count?: number;
        
          constructor(private {module_name.camel}{lib_user_type.pascal}Service: {module_name.pascal}{lib_user_type.pascal}Service) {{}}
        
          connect(): Observable<{module_name.pascal}[]> {{
            return this._data$.asObservable();
          }}
        
          disconnect(): void {{
            this._data$.complete();
          }}
        
          load{module_name.pascal}s(
            filters: Filter[],
            pageIndex: number,
            pageSize: number,
            sortActive: string,
            sortDirection: 'asc' | 'desc' | ''
          ) {{
            this.{module_name.camel}{lib_user_type.pascal}Service
              .getElementPage(filters, pageIndex, pageSize, sortActive, sortDirection)
              .subscribe(({module_name.camel}Page: ListPage<{module_name.pascal}[]>) => {{
                this._data$.next({module_name.camel}Page.results);
                this.data = {module_name.camel}Page.results;
                this.count = {module_name.camel}Page.count;
              }});
          }}
        }}
        '''
        return file_content

