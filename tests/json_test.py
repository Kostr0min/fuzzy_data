import pytest
from json_ import Column
from json_ import JsonFuzzy


@pytest.mark.parametrize(
    'json, output', [
        (
            {
                'row_count': 10,
                'columns': [
                    {
                        'column_name': 'name1',
                        'column_type': 'string',
                        'properties': {
                            'len': 5,
                            'has_lower': True,
                            'has_upper': True,
                            'has_digit': True,
                        },
                    },
                ],
            },
            [
                Column(
                    name='name1',
                    type='string',
                    properties={
                        'len': 5,
                        'has_lower': True,
                        'has_upper': True,
                        'has_digit': True,
                    },
                ),
            ],

        ),
        (
            {
                'row_count': 10,
                'columns': [
                    {
                        'column_name': 'name1',
                        'column_type': 'string',
                        'properties': {
                            'len': 5,
                            'has_lower': True,
                            'has_upper': True,
                            'has_digit': True,
                        },
                    },
                    {
                        'column_name': 'name2',
                        'column_type': 'string',
                        'properties': {
                            'len': 5,
                            'has_lower': True,
                            'has_upper': True,
                            'has_digit': True,
                        },
                    },
                ],
            },
            [
                Column(
                    name='name1',
                    type='string',
                    properties={
                        'len': 5,
                        'has_lower': True,
                        'has_upper': True,
                        'has_digit': True,
                    },
                ),
                Column(
                    name='name2',
                    type='string',
                    properties={
                        'len': 5,
                        'has_lower': True,
                        'has_upper': True,
                        'has_digit': True,
                    },
                ),
            ],

        ),
    ],
)
def test_json(json: dict, output):
    test_object = JsonFuzzy(json)
    parsed_data = test_object.parse_json_columns()

    for real, excepted in zip(parsed_data, output):
        assert real == excepted
