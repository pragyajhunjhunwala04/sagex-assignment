import chat 
import pandas as pd

def read_csv(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded CSV with {len(df)} rows and {len(df.columns)} column(s).")
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        raise

def add_column_to_csv(df: pd.DataFrame, column_name: str, default_value: str = "") -> pd.DataFrame:
    df[column_name] = default_value
    return df

def process_csv_with_gemini(df: pd.DataFrame, column_name: str, transformation_prompt: str) -> pd.DataFrame:
    pass