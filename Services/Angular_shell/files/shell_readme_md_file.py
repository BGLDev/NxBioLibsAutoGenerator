from Models.string_case import StringCase


class ShellReadmeMdFile:

    @staticmethod
    def get_file_content(lib_name: StringCase, module_name: StringCase, lib_user_type: StringCase):
        file_content = f'''                
                        Shell libraries always take care of the routing of its scope.

                        In shell libraries you will find:

                        - {lib_name.kebab}.module.ts
                        - lib.routes.ts
                        - ./src/index.ts

                        # {lib_name.kebab}.module.ts

                        In the layout shell library we already set a .forRoot() module set, in this case <b>layout/shellRoutes</b>, that is the default base router.

                        So in this library's module, the main goal is to import RouterModule and set the child routes defined in <b>{lib_name.camel}Routes</b>

                        # lib.routes.ts

                        In this file we define the child routes of '{module_name.kebab}-{lib_user_type.kebab}/', set in the <b>layout/shellRoutes</b>. In this library we just have 3 child paths.

                        IMPORTANT: pay attention to the data section

                        # index.ts

                        In this file we export both routes and module
                        '''
        return file_content