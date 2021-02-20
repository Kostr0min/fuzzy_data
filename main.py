import numpy as np
import pandas as pd
import yaml

from utils import make_bin
from utils import make_datetime
from utils import make_int
from utils import make_str


class FuzzyData:

    def __init__(self):
        self.parse_yaml()

    def parse_yaml(self, path_to_config='cfg.yaml'):
        with open(path_to_config, encoding='utf-8') as f:
            cfg = yaml.load(f)
        self.cfg = cfg['table_2077']
        self._shape = self.cfg['shape']
        self.str_columns_cfg = self.cfg['columns']['string_columns']
        self.int_columns_cfg = self.cfg['columns']['integer_columns']
        self.bool_columns_cfg = self.cfg['columns']['bool_columns']
        self.date_columns_cfg = self.cfg['columns']['datetime_columns']

    def generate_data(self):
        cols_list = []
        for elem in self.cfg['columns']:
            cols_list += list(self.cfg['columns'][elem].keys())
        df = pd.DataFrame(columns=cols_list, data=np.zeros(self._shape))

        for col in self.str_columns_cfg.keys():
            params = self.str_columns_cfg[col]
            df[col] = df[col].apply(lambda x: make_str(params))

        for col in self.int_columns_cfg.keys():
            params = self.int_columns_cfg[col]
            df[col] = df[col].apply(lambda x: make_int(params))

        for col in self.bool_columns_cfg.keys():
            params = self.bool_columns_cfg[col]
            df[col] = df[col].apply(lambda x: make_bin(params))

        for col in self.date_columns_cfg.keys():
            params = self.date_columns_cfg[col]
            df[col] = df[col].apply(lambda x: make_datetime(params))

        return df


fd = FuzzyData()
cfg = fd.generate_data()

print(cfg)
