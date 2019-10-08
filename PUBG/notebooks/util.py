import pandas as pd


def load_train_data():
    df = pd.read_csv("../data/raw/train_V2.csv")
    return df

def load_test_data():
    df = pd.read_csv("../data/raw/test_V2.csv")
    return df