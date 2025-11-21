import numpy as np
import pandas as pd 
class DataValidation():
    def unique(self, data:pd.DataFrame, column:str):
        if data is None:
            return ValueError('inpute um valor em data')
        response = data[column].nunique()
        if response < data.shape[1]:
            print(f'ha valores duplicados em {column} ')
    def NaN(self, data: pd.DataFrame):
        if data is None:
            return ValueError('inpute um valor em data') 
        try:
            for nun in data.columns:
                response = data[nun].isna().sum()
                if response > 1:
                    print(f'valores nulos em {nun}: {response}')
                print(f'nao há valores nulos em: {nun}')
        except ValueError as value:
            print(f'erro de valor: {value}')
        except Exception as e:
            print(f'erro: {e}')