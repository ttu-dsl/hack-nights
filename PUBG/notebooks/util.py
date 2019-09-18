import pandas as pd


def load_train_data():
    df = pd.read_csv("../data/raw/train_V2.csv")
    return df
