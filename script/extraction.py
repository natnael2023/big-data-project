import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


def load_csv(filename):
    return  pd.read_csv(filename)
def display_basic_info(df):
    print(f"The dataframe has {df.shape[0]} rows and {df.shape[1]} columns.")
    print(df.info())
    print(df.describe())


