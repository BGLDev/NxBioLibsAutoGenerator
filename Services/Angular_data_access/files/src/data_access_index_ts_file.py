from Models.string_case import StringCase


class DataAccessIndexTsFile:

    @staticmethod
    def get_file_content(lib_name: StringCase):
        file_content = f'''
        export * from './lib/{lib_name.kebab}.resolver';
        export * from './lib/{lib_name.kebab}.service';
        '''
        return file_content