import logging
import pandas as pd
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='extract.log',
    filemode='a'
)

def extract_csv(filepath="data/Credit Risk Benchmark Dataset.csv"):
    try:
        if not os.path.exists(filepath):
            logging.error(f"File not found: {filepath}")
            return None

        logging.info(f"Reading data from {filepath}")
        df = pd.read_csv(filepath)
        logging.info(f"Successfully extracted {len(df)} rows and {len(df.columns)} columns")
        return df

    except Exception as e:
        logging.critical(f"Failed to extract CSV: {e}")
        return None

if __name__ == "__main__":
    df = extract_csv()  # No argument needed now
    if df is not None:
        print(df)
