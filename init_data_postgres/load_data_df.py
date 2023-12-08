import pandas as pd
from sqlalchemy import create_engine
import logging
import json
from sqlalchemy.types import Boolean


# Load database configuration from a JSON file
with open("init_data_postgres/config/db_config.json") as f:
    db_config = json.load(f)

# Use the loaded configuration to create the database engine
engine = create_engine(db_config["database_url"], echo=True)

# Path to your Excel file
excel_file_path = "data/Clienti.xlsx"

# Load column_translation from a JSON file
with open("init_data_postgres/config/clients_columns.json") as f:
    column_translation = json.load(f)

df = pd.read_excel(excel_file_path)

df.rename(columns=column_translation, inplace=True)

df["last_order_date"] = df["last_order_date"].replace("0", pd.NaT)
df["registration_date"] = df["registration_date"].replace("0000-00-00", pd.NaT)
df["newsletter_subscription"] = df["newsletter_subscription"].astype(bool)
df["active_client"] = df["active_client"].astype(bool)


try:
    df.to_sql(
        "t_ecuator_clients_initial",
        engine,
        schema="ecuator",
        if_exists="append",
        index=False,
    )
    logging.info("Data successfully loaded into the database.")
except Exception as e:
    logging.error("An error occurred: %s", e)
