import re

class StringCase:
    def __init__(self, input_string):
        pascal_string = self.to_pascal_case(input_string)
        self.camel = re.sub(r'^\w', lambda x: x.group(0).lower(), pascal_string)
        self.pascal = pascal_string
        self.snake = re.sub(r'(?<!^)(?=[A-Z])', '_', pascal_string).lower()
        self.kebab = re.sub(r'(?<!^)(?=[A-Z])', '-', pascal_string).lower()
        self.snake_upper = re.sub(r'(?<!^)(?=[A-Z])', '_', pascal_string).upper()

    @staticmethod
    def to_pascal_case(input_string):
        words = re.split(r'(?=[A-Z])|[_-]', input_string)
        return ''.join([word.capitalize() for word in words])