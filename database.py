import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv


load_dotenv()
DB_URL = f"mysql+pymysql://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}/{os.getenv('DATABASE')}?charset=utf8mb4"
engine = create_engine(
    DB_URL,
    connect_args={
        "ssl": {
            "ssl_ca": "C:\Users\darq\cacert-2023-05-30.pem""C:\Users\darq\cacert-2023-05-30.pem"}
    })

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    print(result.all())