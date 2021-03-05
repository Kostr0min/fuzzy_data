import numpy as np
import pandas as pd
import yaml
from utils import make_cols


class FuzzyData:

    def __init__(self):
        self.parse_yaml()

    def parse_yaml(self, path_to_config='cfg.yaml'):
        with open(path_to_config, encoding='utf-8') as f:
            cfg = yaml.load(f)
        self.cfg = cfg['table_2077']
        self._shape = self.cfg['shape']

    def generate_data(self):
        cols_list = []
        for elem in self.cfg['columns']:
            cols_list += list(self.cfg['columns'][elem].keys())
        df = pd.DataFrame(columns=cols_list, data=np.zeros(self._shape))

        for elem in self.cfg['columns']:
            for col in self.cfg['columns'][elem]:
                params = self.cfg['columns'][elem][col]
                df[col] = df[col].apply(lambda x: make_cols(elem, params))

        return df
