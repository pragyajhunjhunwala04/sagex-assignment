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

def convert_to_list(value: str) -> list:
    result = []
    item = ''
    in_string = False
    escape = False

    # Remove leading/trailing whitespace and brackets
    value = value.strip()
    if value.startswith('[') and value.endswith(']'):
        value = value[1:-1]

    for char in value:
        if char == '"' or char == "'":
            if not in_string:
                in_string = char
            elif in_string == char and not escape:
                in_string = False
            else:
                item += char
        elif char == '\\' and in_string:
            escape = True
            item += char
            continue
        elif char == ',' and not in_string:
            result.append(item.strip().strip('"').strip("'"))
            item = ''
        else:
            item += char
        escape = False

    if item:
        result.append(item.strip().strip('"').strip("'"))
    return result

def process_csv_with_gemini(df: pd.DataFrame, column_name: str, transformation_prompt: str) -> pd.DataFrame:
    batch_size = 25
    num_rows = len(df)
    first_col = df.columns[0]

    for start in range(0, num_rows, batch_size):
        end = min(start + batch_size, num_rows)
        values_batch = df.iloc[start:end][first_col].tolist()

        prompt = (
            f"You are given a list of values: {values_batch}. "
            f"Apply the following transformation to each value, in order: {transformation_prompt}. "
            "Return only a Python list of the transformed values, preserving the original order. "
            "Do not include any explanations or extra text, only the list."
        )
        processed_values = (chat.get_gemini_response(prompt)).strip()
        print(processed_values)
        processed_values = convert_to_list(processed_values)
        print(processed_values)
    
        if not isinstance(processed_values, list) or len(processed_values) != (end - start):
            raise ValueError("Gemini response did not return the expected number of values.")
        
        df.loc[start:end-1, column_name] = processed_values

    return df

def save_csv(df: pd.DataFrame, file_path: str) -> None:
    try:
        df.to_csv(file_path, index=False)
        print(f"CSV saved successfully to {file_path}.")
    except Exception as e:
        print(f"Error saving CSV file: {e}")
        raise