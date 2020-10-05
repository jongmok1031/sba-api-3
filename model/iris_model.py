import pandas as pd

class IrisModel:
    def __init__(self):
        df = pd.read_csv('https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data', header=None)
        print(df.head())
        print('==================')
        print(df.tail())