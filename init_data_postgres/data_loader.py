import pandas as pd
import logging
import json

class DataLoader:
    def __init__(self, engine, excel_file_path, column_mapping_path):
        self.engine = engine
        self.excel_file_path = excel_file_path
        self.column_mapping_path = column_mapping_path

    def load_excel(self):
        self.df = pd.read_excel(self.excel_file_path)
        logging.info("Excel file '%s' loaded successfully.", self.excel_file_path)

    def apply_column_transformation(self):
        with open(self.column_mapping_path, 'r') as f:
            column_translation = json.load(f)
        self.df.rename(columns=column_translation, inplace=True)
        logging.info("Column transformations applied successfully.")

    def clean_data(self):
        # You may want to generalize this method depending on your cleaning requirements
        self.df["last_order_date"] = self.df["last_order_date"].replace("0", pd.NaT)
        self.df["registration_date"] = self.df["registration_date"].replace("0000-00-00", pd.NaT)
        self.df["newsletter_subscription"] = self.df["newsletter_subscription"].astype(bool)
        self.df["active_client"] = self.df["active_client"].astype(bool)

    def to_sql(self, table_name, schema):
        try:
            self.df.to_sql(
                table_name,
                self.engine,
                schema=schema,
                if_exists="append",
                index=False,
            )
            logging.info("Data successfully loaded into the database.")
        except Exception as e:
            logging.error("An error occurred while inserting into the database: %s", e)
