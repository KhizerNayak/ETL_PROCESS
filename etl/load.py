from sqlalchemy import create_engine, text
import logging
from dotenv import load_dotenv
import os
from transform import Transform
import extraxt
import pandas as pd
from urllib.parse import quote_plus

load_dotenv()

df = extraxt.extract_csv()

transformer = Transform(df)
cleaned_df = (
    transformer
    .outlier_handling()
    .total_late()
    .credit_burden()
    .high_risk()
    .get_df()  # make sure you add this method to return df (see below)
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='transform.log',
    filemode='a'
)



user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
database = os.getenv("MYSQL_DB")


encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://{user}:{encoded_password}@{host}:{port}/{database}")

print("🔍 MYSQL_USER:", os.getenv("MYSQL_USER"))  # Should print "user"
print("🔍 MYSQL_PASSWORD:", os.getenv("MYSQL_PASSWORD"))  # Should print Asdf@1234


with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("✅ Connection successful:", result.scalar())
    cleaned_df.to_sql(
        name="credit_risk_data",
        con=engine,
        index=False,
        if_exists="replace"
    )
    print(f"Connecting to MySQL at {host}:{port} with user {user} and password (encoded): {encoded_password}")

    print("✅ Data loaded to MySQL successfully!")
