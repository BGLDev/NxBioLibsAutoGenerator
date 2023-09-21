import string

from Models.string_case import StringCase


class DataAccessProyectJsonFile:

    @staticmethod
    def get_file_content(lib_path, scope_name: StringCase):
        file_content = f'''
        {{
          "name": "{lib_path.replace('/', '-')}",
          "$schema": "../../../../node_modules/nx/schemas/project-schema.json",
          "projectType": "library",
          "sourceRoot": "libs/{lib_path}/src",
          "prefix": "biolan",
          "targets": {{
            "test": {{
              "executor": "@nrwl/jest:jest",
              "outputs": ["{{workspaceRoot}}/coverage/{{projectRoot}}"],
              "options": {{
                "jestConfig": "libs/{lib_path}/jest.config.ts",
                "passWithNoTests": true
              }}
            }},
            "lint": {{
              "executor": "@nrwl/linter:eslint",
              "outputs": ["{{options.outputFile}}"],
              "options": {{
                "lintFilePatterns": [
                  "libs/{lib_path}/**/*.ts",
                  "libs/{lib_path}/**/*.html"
                ]
              }}
            }}
          }},
          "tags": ["scope:{scope_name.kebab}", "type:library"]
        }}
        '''
        return file_content