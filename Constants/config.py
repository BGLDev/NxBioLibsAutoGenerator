SCOPE = 'scope'
USER_TYPE = 'user type'
DJANGO_MODEL_NAME = 'django model name'
DJANGO_MODEL_EXTENDS = 'django model extends'
DJANGO_MODEL_PARAMS = 'django model params'

FK_PARAM_TYPE = 'models.ForeignKey'


BASE_MODEL_PARAMS={
    'id': 'models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)',
    'created': 'models.DateTimeField()',
    'updated': 'models.DateTimeField()',
    'update_user': 'models.ForeignKey(User, on_delete=models.CASCADE)',
    'create_user': 'models.ForeignKey(User, on_delete=models.CASCADE)',
    'display_name': 'models.CharField()',
}

TYPE_NUMBER = 'number'
TYPE_STRING = 'string'
TYPE_BOOLEAN = 'boolean'
TYPE_FK = 'FK'
TYPE_DATE = 'Date'
TYPE_ANY = 'any'

PARAM_TYPE_INFO = {
    TYPE_NUMBER: {
        'type': TYPE_NUMBER,
        'filter_type': TYPE_NUMBER,
        'filter_lookup_expr': ['exact', 'gt', 'gte', 'lt', 'lte'],
        'field_types': [
            'AutoField',
            'BigAutoField',
            'BigIntegerField',
            'BinaryField',
            'DecimalField',
            'FloatField',
            'IntegerField',
            'PositiveBigIntegerField',
            'PositiveIntegerField',
            'PositiveSmallIntegerField',
            'SmallAutoField',
            'SmallIntegerField',
        ]
    },
    TYPE_STRING: {
        'type': TYPE_STRING,
        'filter_type': 'text',
        'filter_lookup_expr': ['iexact', 'icontains', 'istartswith', 'iendswith'],
        'field_types': [
            'CharField',
            'EmailField',
            'FileField',
            'FilePathField',
            'GenericIPAddressField',
            'ImageField',
            'JSONField',
            'SlugField',
            'TextField',
            'URLField',
            'UUIDField',
            'ManyToManyField',#TODO
        ]
    },
    TYPE_BOOLEAN: {
        'type': TYPE_BOOLEAN,
        'filter_type': TYPE_BOOLEAN,
        'filter_lookup_expr': ['exact'],
        'field_types': [
            'BooleanField',
        ]
    },
    TYPE_FK: {
        'type': TYPE_FK,
        'filter_type': 'option',
        'filter_lookup_expr': ['exact'],
        'field_types': [
            'ForeignKey',
        ]
    },
    TYPE_DATE: {
        'type': TYPE_DATE,
        'filter_type': TYPE_DATE,
        'filter_lookup_expr': ['exact'],
        'field_types': [
            'DateField',
            'DateTimeField',
            'DurationField',
        ]
    },
   # TYPE_ANY: {
    #    'type': TYPE_ANY,
    #   'filter_type': TYPE_ANY,
    #  'filter_lookup_expr': ['exact'],
    # 'field_types': [
    #    'ManyToManyField',
    #    ]
   # },
}