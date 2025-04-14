import pandas as pd


def read_in_csv():
    #print(pd.__version__)
    df = pd.read_csv('uploads/sample.csv')
    #print(df)
    #print(type(df))
    return df

def is_Frame(data):
    return isinstance(data, pd.DataFrame)

def reverse_for_loop(frames):
    if not is_Frame(frames):
            print("Invalid frame")
            return "Invalid frame"

    for i in range(len(frames)-1, -1, -1):
         print(frames.iloc[i])
         
        

"""def clean_data(df):

    rf = df.dropna()
    for frame in frames:
        

    return

def json_to_frame():"""




reverse_for_loop(read_in_csv())




