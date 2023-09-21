

class ListTsconfigLibJsonFile:

    @staticmethod
    def get_file_content():
        file_content = f'''
        {{
          "extends": "./tsconfig.json",
          "compilerOptions": {{
            "outDir": "../../../../../../dist/out-tsc",
            "declaration": true,
            "declarationMap": true,
            "inlineSources": true,
            "types": []
          }},
          "exclude": [
            "src/test-setup.ts",
            "src/**/*.spec.ts",
            "jest.config.ts",
            "src/**/*.test.ts"
          ],
          "include": ["src/**/*.ts"]
        }}
        '''
        return file_content