# %%
import sqlite3 
import pandas as pd 
import os 

db_path = os.path.join('..','..','data', 'WA_telecom.db')
con = sqlite3.connect(db_path)
data_path = os.path.join('..','..','data', 'WA_Fn-UseC_-Telco-Customer-Churn.csv')

def create_db(data, con):
    if data.endswith('.csv'):
        try:
            df = pd.read_csv(data)
            df.to_sql('WA_telecom_churn', con=con, if_exists='replace', index=False)
        except Exception as e:
                return {'erro. Saida':e}
if __name__ == '__main__':
    create_db(data_path, con)
# %%
