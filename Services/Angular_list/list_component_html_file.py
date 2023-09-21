from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE, TYPE_ANY
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class ListHtmlFile:
    
    def __init__(self):
        self.table_columns = {
            TYPE_NUMBER: self._table_data_type_number,
            TYPE_STRING: self._table_data_type_string,
            TYPE_BOOLEAN: self._table_data_type_bool,
            TYPE_FK: self._table_data_type_fk,
            TYPE_DATE: self._table_data_type_date,
            TYPE_ANY: self._table_data_type_string,

        }
        
    def get_file_content(self, params: [Param], module_name: StringCase):
        table_name = f"{module_name.camel}Table"
        table_content = self._table_data_type_select(table_name)
        for param in params:
            table_content += self.table_columns[param.type](param.name)
        file_content = f'''
                <div class="list-header">
                  <h2
                    [ngClass]="
                      (themingService.changeTheming$ | async) ? 'light-theme' : 'dark-theme'
                    "
                  >
                    {{{{ '{module_name.snake.upper()}' | transloco }}}}
                  </h2>
                  <mat-paginator
                    #paginator
                    [pageIndex]="
                      (breadcrumbService.pageIndex$ | async) ??
                      breadcrumbService.pageIndexDefault
                    "
                    [pageSize]="
                      (breadcrumbService.pageSize$ | async) ?? breadcrumbService.pageSizeDefault
                    "
                    [pageSizeOptions]="breadcrumbService.pageSizeOptions"
                    [length]="{table_name}.dataSource.count"
                    showFirstLastButtons
                  >
                  </mat-paginator>
                </div>
                
                <section id="table-container">
                  <table
                    mat-table
                    [dataSource]="{table_name}.dataSource"
                    matSort
                    [matSortActive]="(breadcrumbService.sortActive$ | async) || ''"
                    [matSortDirection]="(breadcrumbService.sortDirection$ | async) || ''"
                  >
                    {table_content}
                    <tr mat-header-row *matHeaderRowDef="{table_name}.displayedColumns"></tr>
                    <tr
                      mat-row
                      *matRowDef="let row; columns: {table_name}.displayedColumns"
                      (click)="openDetail(row)"
                    ></tr>
                  </table>
                </section>
            '''
        
        return file_content

    @staticmethod
    def _table_data_type_select(table_name: str):
        table_content = f'''
                    <ng-container matColumnDef="select">
                      <th mat-header-cell *matHeaderCellDef>
                        <mat-checkbox
                          (change)="
                            $event
                              ? globalTableService.toggleAllRows({table_name} || [])
                              : null
                          "
                          [checked]="
                            {table_name}.selection.hasValue() &&
                            globalTableService.isAllSelected({table_name} || [])
                          "
                          [indeterminate]="
                            {table_name}.selection.hasValue() &&
                            !globalTableService.isAllSelected({table_name} || [])
                          "
                        >
                        </mat-checkbox>
                      </th>
                      <td mat-cell *matCellDef="let row">
                        <mat-checkbox
                          (click)="$event.stopPropagation()"
                          (change)="$event ? {table_name}.selection.toggle(row) : null"
                          [checked]="{table_name}.selection.isSelected(row)"
                        >
                        </mat-checkbox>
                      </td>
                    </ng-container>
                    '''
        return table_content

    @staticmethod
    def _table_data_type_number(param_name: StringCase):
        table_content = f'''
                    <ng-container matColumnDef="{param_name.snake}">
                      <th
                        mat-header-cell
                        *matHeaderCellDef
                        mat-sort-header
                        sortActionDescription="Sort by {param_name.snake}"
                      >
                        {{{{'{param_name.snake.upper()}' | transloco}}}}
                      </th>
                      <td mat-cell *matCellDef="let element">{{{{element.{param_name.camel}}}}}</td>
                    </ng-container>
                    '''
        return table_content

    @staticmethod
    def _table_data_type_string(param_name: StringCase):
        table_content = f'''
                    <ng-container matColumnDef="{param_name.snake}">
                      <th
                        mat-header-cell
                        *matHeaderCellDef
                        mat-sort-header
                        sortActionDescription="Sort by {param_name.snake}"
                      >
                        {{{{'{param_name.snake.upper()}' | transloco}}}}
                      </th>
                      <td mat-cell *matCellDef="let element">{{{{element.{param_name.camel}}}}}</td>
                    </ng-container>
                    '''
        return table_content

    @staticmethod
    def _table_data_type_bool( param_name: StringCase):
        table_content = f'''
                    <ng-container matColumnDef="{param_name.snake}">
                      <th
                        mat-header-cell
                        *matHeaderCellDef
                        mat-sort-header
                        sortActionDescription="Sort by {param_name.snake}"
                      >
                        {{{{'{param_name.snake.upper()}' | transloco}}}}
                      </th>
                      <td mat-cell *matCellDef="let element">
                        <biolan-chip
                          size="small"
                          [classMode]="element.{param_name.camel} === true ? 'ok' : 'warning'"
                        >
                          <mat-icon
                            class="material-symbols-outlined"
                            [fontIcon]="element.{param_name.camel} === true ? 'done' : 'close'"
                          ></mat-icon>
                        </biolan-chip>
                      </td>
                    </ng-container>
                    '''
        return table_content

    @staticmethod
    def _table_data_type_fk(param_name: StringCase):
        table_content = f'''
                    <ng-container matColumnDef="{param_name.snake}">
                      <th
                        mat-header-cell
                        *matHeaderCellDef
                        mat-sort-header
                        sortActionDescription="Sort by {param_name.snake}"
                      >
                        {{{{'{param_name.snake.upper()}' | transloco}}}}
                      </th>
                      <td mat-cell *matCellDef="let element">{{{{element.{param_name.camel}.displayName}}}}</td>
                    </ng-container>
                    '''
        return table_content

    @staticmethod
    def _table_data_type_date(param_name: StringCase):
        table_content = f'''
                    <ng-container matColumnDef="{param_name.snake}">
                      <th
                        mat-header-cell
                        *matHeaderCellDef
                        mat-sort-header
                        sortActionDescription="Sort by {param_name.snake}"
                      >
                        {{{{ '{param_name.snake.upper()}' | transloco }}}}
                      </th>
                      <td mat-cell *matCellDef="let element" class="not-word-break">
                        {{{{ element.{param_name.camel} | shortDate : 'FORMAT_DATE_TIME' }}}}
                      </td>
                    </ng-container>
                    '''
        return table_content
    
    