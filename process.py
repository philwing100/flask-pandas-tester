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
         
        

def clean_data(df):

    #rf = df.dropna()
    x = df["age"].median()
    rf.fillna({"age"})
    for frame in frames:
        pass

    return

def read_in_json(json):
    return pd.read_json(json)
    

#reverse_for_loop(read_in_csv())
reverse_for_loop(read_in_json("uploads/sample.json"))




