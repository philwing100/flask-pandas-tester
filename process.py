import pandas as pd


def read_in_csv(csv: str):
    #print(pd.__version__)
    df = pd.read_csv(csv)
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
    if not is_Frame(df):
        print("❌ Invalid frame")
        return "Invalid frame"

    print("🧼 Cleaning data...")
    if 'age' in df.columns:
        df['age'] = df['age'].fillna(0).astype(int)

    # 1. Trim whitespace in 'name' and 'city'
    df['name'] = df['name'].astype(str).str.strip()
    df['city'] = df['city'].astype(str).str.strip()

    # 2. Normalize case (capitalize names and cities)
    df['name'] = df['name'].str.title()
    df['city'] = df['city'].str.title()

    # 3. Convert age to numeric (non-numeric becomes NaN)
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

    # 4. Drop rows where any of the important fields are missing
    df.dropna(subset=['name', 'city', 'age'], inplace=True)

    # 5. Drop duplicates
    df.drop_duplicates(inplace=True)

    print("✅ Cleaned", len(df), "rows")
    return df.to_dict(orient="records")

def read_in_json(json):
    return pd.DataFrame(pd.read_json(json))
     
#reverse_for_loop(read_in_csv())
#reverse_for_loop(read_in_json("uploads/sample.json"))
#clean_data(read_in_csv("uploads/sample.csv"))




