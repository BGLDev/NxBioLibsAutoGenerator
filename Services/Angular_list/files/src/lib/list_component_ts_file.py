from Constants.config import TYPE_NUMBER, TYPE_STRING, TYPE_BOOLEAN, TYPE_FK, TYPE_DATE
from Models.model_interface import Param
from Models.string_case import StringCase
from Utils import utils


class ListComponentTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase, module_name: StringCase, lib_user_type: StringCase, params: [Param]):
        display_columns = ''
        for param in params:
            display_columns += f'''
                      '{param.name.snake}','''

        file_content = f'''
                import {{ SelectionModel }} from '@angular/cdk/collections';
                import {{ AfterViewInit, Component, OnDestroy, ViewChild }} from '@angular/core';
                import {{ MatPaginator }} from '@angular/material/paginator';
                import {{ MatSort }} from '@angular/material/sort';
                import {{ ActivatedRoute, Router }} from '@angular/router';
                import {{ {module_name.pascal}{lib_user_type.pascal}Service }} from '@biolan/biolanglobal/{module_name.kebab}/data-access';
                import {{ ActionsService }} from '@biolan/biolanglobal/layout/data-access/actions-service';
                import {{ BreadcrumbService }} from '@biolan/biolanglobal/layout/data-access/breadcrumb-service';
                import {{ FilterService }} from '@biolan/biolanglobal/layout/data-access/filter-service';
                import {{ ThemingService }} from '@biolan/biolanglobal/layout/data-access/theming-service';
                import {{ {module_name.pascal}, TableDataSource }} from '@biolan/biolanglobal/utils/model';
                import {{ GlobalTableService }} from '@biolan/biolanglobal/utils/services/global-table';
                import {{ filter, merge, tap }} from 'rxjs';
                import {{ {lib_name.pascal}DataSource }} from './{lib_name.kebab}.datasource';
                import {{ {lib_name.pascal}FilterCriterias }} from './{lib_name.kebab}.filter';
                
                @Component({{
                  selector: 'biolan-{lib_name.kebab}',
                  templateUrl: './{lib_name.kebab}.component.html',
                }})
                export class {lib_name.pascal}Component implements AfterViewInit, OnDestroy {{
                  {module_name.camel}Table: TableDataSource<{lib_name.pascal}DataSource> = {{
                    dataSource: new {lib_name.pascal}DataSource(this.{module_name.camel}{lib_user_type.pascal}Service),
                    displayedColumns: [
                      'select',{display_columns}
                    ],
                
                    selection: new SelectionModel<{module_name.pascal}>(true, []),
                  }};
                
                  @ViewChild(MatPaginator) paginator!: MatPaginator;
                  @ViewChild(MatSort) sort!: MatSort;
                
                  constructor(
                    private router: Router,
                    private route: ActivatedRoute,
                    private {module_name.camel}{lib_user_type.pascal}Service: {module_name.pascal}{lib_user_type.pascal}Service,
                    private filterService: FilterService,
                    private actionsService: ActionsService,
                    public breadcrumbService: BreadcrumbService,
                    public themingService: ThemingService,
                    public globalTableService: GlobalTableService,
                    private {lib_name.camel}FilterCriterias: {lib_name.pascal}FilterCriterias
                  ) {{
                    this.filterService.showFilter(true);
                    this.filterService.setFilterCriteria({lib_name.camel}FilterCriterias.filterCriteria);
                    this.actionsService.restart();
                    this.actionsService.configNewButton({{ show: true }});
                    this.actionsService.configDeleteButton({{
                      show: true,
                      action: this.onDelete.bind(this),
                    }});
                    // bind this or use an arrow function: https://stackoverflow.com/a/38245500
                    //this.actionsService.setDeleteAction(this.onDelete.bind(this));
                  }}
                
                  ngAfterViewInit(): void {{
                    this.paginator.page.subscribe((page) =>
                      this.breadcrumbService.storePaginator(page.pageIndex, page.pageSize)
                    );
                    this.sort.sortChange.subscribe((sort) =>
                      this.breadcrumbService.storeSort(sort.active, sort.direction)
                    );
                    this.sort.sortChange.subscribe(() => this.resetPage());
                    this.filterService.activeFilters$
                      .pipe(filter((filters) => filters != null))
                      .subscribe(() => this.resetPage());
                    merge(
                      this.sort.sortChange,
                      this.paginator.page,
                      this.filterService.activeFilters$
                    )
                      .pipe(tap(() => this.load{module_name.pascal}Page()))
                      .subscribe();
                  }}
                
                  onDelete(): void {{
                    if (this.{module_name.camel}Table.selection.hasValue()) {{
                      this.{module_name.camel}{lib_user_type.pascal}Service
                        .bulkDeleteElements(
                          this.{module_name.camel}Table.selection.selected.map(({module_name.camel}) => {module_name.camel}.id)
                        )
                        .subscribe();
                      this.{module_name.camel}Table.selection.clear();
                      this.load{module_name.pascal}Page();
                    }}
                  }}
                
                  load{module_name.pascal}Page(): void {{
                    this.{module_name.camel}Table.dataSource.load{module_name.pascal}s(
                      this.filterService.activeFilters,
                      this.paginator.pageIndex,
                      this.paginator.pageSize,
                      this.sort.active,
                      this.sort.direction
                    );
                  }}
                
                  openDetail({module_name.camel}: {module_name.pascal}) {{
                    this.router.navigate([{module_name.camel}.id], {{ relativeTo: this.route }});
                  }}
                
                  ngOnDestroy(): void {{
                    this.filterService.setFilterCriteria([]);
                  }}
                
                  private resetPage(): void {{
                    this.paginator.pageIndex = 0;
                  }}
                }}

            '''
        return file_content

