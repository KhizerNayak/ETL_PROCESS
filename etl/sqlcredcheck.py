import os
from dotenv import load_dotenv
from sqlalchemy import sql,Connection,create_engine
from urllib.parse import quote_plus

load_dotenv()

# MYSQL_USER=user
# MYSQL_PASSWORD=Asdf@1234
# MYSQL_HOST=127.0.0.1
# MYSQL_PORT=3306
# MYSQL_DB=ETL_CSV_DB


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
