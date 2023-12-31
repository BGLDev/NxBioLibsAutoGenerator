class DataAccessEslintrcJsonFile:

    @staticmethod
    def get_file_content():
        file_content = f'''
            {{
              "extends": ["../../../../.eslintrc.json"],
              "ignorePatterns": ["!**/*"],
              "overrides": [
                {{
                  "files": ["*.ts"],
                  "rules": {{
                    "@angular-eslint/directive-selector": [
                      "error",
                      {{
                        "type": "attribute",
                        "prefix": "biolan",
                        "style": "camelCase"
                      }}
                    ],
                    "@angular-eslint/component-selector": [
                      "error",
                      {{
                        "type": "element",
                        "prefix": "biolan",
                        "style": "kebab-case"
                      }}
                    ]
                  }},
                  "extends": [
                    "plugin:@nrwl/nx/angular",
                    "plugin:@angular-eslint/template/process-inline-templates"
                  ]
                }},
                {{
                  "files": ["*.html"],
                  "extends": ["plugin:@nrwl/nx/angular-template"],
                  "rules": {{}}
                }}
              ]
            }}
        '''
        return file_content