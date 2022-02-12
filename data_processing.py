import pandas as pd

def derive_vars(df):

    df_ = df.copy()

    # String of datetime
    df_.datetime_ = pd.to_datetime(df_.datetime).dt.strftime('%A %Y-%m-%d @ %H:%M' )
    return df_