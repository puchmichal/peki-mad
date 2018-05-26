from sqlalchemy import create_engine
import numpy as np
import pandas as pd

engine = create_engine('postgresql://sample_user:!TajemniczaTajemnica7@85.194.245.31:5432/locit_sample')

# STEP 1 - get all the demographic and around-demographic data
query = 'SELECT * FROM locit_datasets.grid250_demo_ext;'
demo = pd.read_sql_query(query, con=engine)

demo.to_csv(path_or_buf="data_demo.csv", sep=";")