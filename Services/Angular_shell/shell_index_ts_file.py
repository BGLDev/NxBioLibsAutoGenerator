from Models.string_case import StringCase


class ShellIndexTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase):
        file_content = f'''
        export * from './lib/{lib_name.kebab}.module';
        export * from './lib/lib.routes';
        '''
        return file_content