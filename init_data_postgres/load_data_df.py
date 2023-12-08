from database_connector import DatabaseConnector
from data_loader import DataLoader


# Postgres database configuration
config_path = "init_data_postgres/config/db_config.json"

db_connector = DatabaseConnector(config_path=config_path)

engine = db_connector.get_engine()

# Client data loading
client_loader = DataLoader(
    engine, "data/Clienti.xlsx", "init_data_postgres/config/clients_columns.json"
)
client_loader.load_excel()
client_loader.apply_column_transformation()
client_loader.clean_data()
client_loader.to_sql("t_ecuator_clients_initial", "ecuator")
