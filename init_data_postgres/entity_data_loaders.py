from data_loader import DataLoader
import pandas as pd


class ClientDataLoader(DataLoader):
    def __init__(self, engine, excel_file_path, column_mapping_path):
        super().__init__(engine, excel_file_path, column_mapping_path)
        self.table_name = "t_ecuator_clients_initial"
        self.schema = "ecuator"

    def clean_data(self):
        self.df["last_order_date"] = self.df["last_order_date"].replace("0", pd.NaT)
        self.df["registration_date"] = self.df["registration_date"].replace(
            "0000-00-00", pd.NaT
        )
        self.df["newsletter_subscription"] = self.df["newsletter_subscription"].astype(
            bool
        )
        self.df["active_client"] = self.df["active_client"].astype(bool)


class ProductDataLoader(DataLoader):
    def __init__(self, engine, excel_file_path, column_mapping_path):
        super().__init__(engine, excel_file_path, column_mapping_path)
        self.table_name = "products_table"
        self.schema = "ecuator"

    def clean_data(self):
        # Implement product-specific cleaning logic here
        # Cleaning logic code ...
        ...


class OrderDataLoader(DataLoader):
    def __init__(self, engine, excel_file_path, column_mapping_path):
        super().__init__(engine, excel_file_path, column_mapping_path)
        self.table_name = "orders_table"
        self.schema = "ecuator"

    def clean_data(self):
        # Implement order-specific cleaning logic here
        # Cleaning logic code ...
        ...
