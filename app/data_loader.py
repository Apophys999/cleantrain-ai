import pandas as pd
import jsonlines
import os

def load_data(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines

    elif ext == ".csv":
        df = pd.read_csv(file_path)
        return df[df.columns[0]].dropna().tolist()

    elif ext == ".jsonl":
        with jsonlines.open(file_path) as reader:
            return [obj for obj in reader]

    else:
        raise ValueError(f"Unsupported file type: {ext}")
