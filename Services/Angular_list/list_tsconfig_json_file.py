
class ListTsconfigJsonFile:

    @staticmethod
    def get_file_content():
        file_content = f'''
        {{
          "compilerOptions": {{
            "target": "es2022",
            "useDefineForClassFields": false,
            "forceConsistentCasingInFileNames": true,
            "strict": true,
            "noImplicitOverride": true,
            "noPropertyAccessFromIndexSignature": true,
            "noImplicitReturns": true,
            "noFallthroughCasesInSwitch": true
          }},
          "files": [],
          "include": [],
          "references": [
            {{
              "path": "./tsconfig.lib.json"
            }},
            {{
              "path": "./tsconfig.spec.json"
            }}
          ],
          "extends": "../../../../../../tsconfig.base.json",
          "angularCompilerOptions": {{
            "enableI18nLegacyMessageIdFormat": false,
            "strictInjectionParameters": true,
            "strictInputAccessModifiers": true,
            "strictTemplates": true
          }}
        }}
        '''
        return file_content