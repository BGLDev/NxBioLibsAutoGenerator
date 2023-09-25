from Models.string_case import StringCase


class ShellJestConfigTsFile:

    @staticmethod
    def get_file_content(lib_path):
        file_content = f'''
        /* eslint-disable */
        export default {{
          displayName: '{lib_path.replace('/', '-')}',
          preset: '../../../../../../jest.preset.js',
          setupFilesAfterEnv: ['<rootDir>/src/test-setup.ts'],
          globals: {{
            'ts-jest': {{
              tsconfig: '<rootDir>/tsconfig.spec.json',
              stringifyContentPathRegex: '\\\\.(html|svg)$',
            }},
          }},
          coverageDirectory:
            '../../../../../../coverage/libs/{lib_path}',
          transform: {{
            '^.+\\\\.(ts|mjs|js|html)$': 'jest-preset-angular',
          }},
          transformIgnorePatterns: ['node_modules/(?!.*\\\\.mjs$)'],
          snapshotSerializers: [
            'jest-preset-angular/build/serializers/no-ng-attributes',
            'jest-preset-angular/build/serializers/ng-snapshot',
            'jest-preset-angular/build/serializers/html-comment',
          ],
        }};
        '''
        return file_content