

class DataAccessTsconfigSpecJsonFile:

    @staticmethod
    def get_file_content():
        file_content = f'''
        {{
          "extends": "./tsconfig.json",
          "compilerOptions": {{
            "outDir": "../../../../dist/out-tsc",
            "module": "commonjs",
            "types": ["jest", "node"]
          }},
          "files": ["src/test-setup.ts"],
          "include": [
            "jest.config.ts",
            "src/**/*.test.ts",
            "src/**/*.spec.ts",
            "src/**/*.d.ts"
          ]
        }}
        '''
        return file_content
