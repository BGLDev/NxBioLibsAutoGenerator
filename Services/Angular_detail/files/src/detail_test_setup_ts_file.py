

class DetailTestSetupTsFile:

    @staticmethod
    def get_file_content():
        file_content = f'''
        import 'jest-preset-angular/setup-jest';
        '''
        return file_content