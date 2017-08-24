import pandas as pd


HEADER = ('pd', 'Z00', 'Z1-1', 'Z11', 'Z2-2', 'Z20', 'Z22', 'Z3-3', 'Z3-1',
          'Z31', 'Z33', 'Z4-4', 'Z4-2', 'Z40', 'Z42', 'Z44', 'Z5-5', 'Z5-3',
          'Z5-1', 'Z51', 'Z53', 'Z55', 'Z6-6', 'Z6-4', 'Z6-2', 'Z60', 'Z62',
          'Z64', 'Z66', 'Z7-7', 'Z7-5', 'Z7-3', 'Z7-1', 'Z71', 'Z73', 'Z75',
          'Z77')


def load(filename):
    df = pd.read_excel(filename)
    assert tuple(df.columns) == HEADER
    X = df.values
    assert X.ndim == 2
    assert X.shape[1] == 37
    return X




