import json
from dataclasses import dataclass
from typing import List
from typing import Tuple


@dataclass
class Column:

    name: str
    type: str
    properties: dict

    def __init__(self, **kwargs):
        # Redefine init for avoid exception with () class initialization
        # **kwargs provide
        for k in kwargs:
            setattr(self, k, kwargs[k])

    def __eq__(self, other):

        return all(
            [
                self.name == other.name,
                self.type == other.type,
                self.properties == other.properties,
            ],
        )


class JsonFuzzy:

    def __init__(self, request_json: dict):
        self.request = request_json
        self.columns = request_json['columns']

    @property
    def shape(self) -> Tuple[int, int]:
        return self.request['row_count'], len(self.columns)

    def parse_json_columns(self) -> List[Column]:
        # Convert JSON to list of columns
        columns = []

        for column in self.columns:
            new_column = Column()

            for attr in column:
                # keys has name: "column_name" we need to convert it to "name"
                attr_name = attr.replace('column_', '')
                setattr(new_column, attr_name, column[attr])
            columns.append(new_column)

        return columns


if __name__ == '__main__':
    with open('../data/test.json') as f:
        test = json.load(f)
    a = JsonFuzzy(test)
    b = a.parse_json_columns()
    print(b)
