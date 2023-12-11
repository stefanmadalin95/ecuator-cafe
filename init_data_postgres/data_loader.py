import pandas as pd
import logging
import json

# Set up logging to output to a file
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)


class DataLoader:
    def __init__(self, engine, excel_file_path, column_mapping_path):
        self.engine = engine
        self.excel_file_path = excel_file_path
        self.column_mapping_path = column_mapping_path

    def load_excel(self):
        self.df = pd.read_excel(self.excel_file_path)
        logging.info("Excel file '%s' loaded successfully.", self.excel_file_path)

    def apply_column_transformation(self):
        with open(self.column_mapping_path, "r") as f:
            column_translation = json.load(f)
        self.df.rename(columns=column_translation, inplace=True)
        logging.info("Column transformations applied successfully.")

    def clean_data(self):
        pass

    def load_data(self, table_name, schema):
        try:
            self.df.to_sql(
                table_name,
                self.engine,
                schema=schema,
                if_exists="replace",
                index=False,
            )
            logging.info(
                f"Data for table {table_name} successfully loaded into the database."
            )
        except Exception as e:
            logging.error("An error occurred while inserting into the database: %s", e)
