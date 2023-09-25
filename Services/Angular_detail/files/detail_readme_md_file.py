class DetailReadmeMdFile:

    @staticmethod
    def get_file_content(lib_path):
        file_content = f'''
        # {lib_path.replace('/', '-')}
        
        This library was generated with [Nx](https://nx.dev).
        
        ## Running unit tests
        
        Run `nx test {lib_path.replace('/', '-')}` to execute the unit tests.
        '''
        return file_content