from database_connector import DatabaseConnector
from entity_data_loaders import ClientDataLoader, ProductDataLoader, OrderDataLoader
import json

try:
    # Postgres database configuration
    config_path = "init_data_postgres/config/db_config.json"

    db_connector = DatabaseConnector(config_path=config_path)

    engine = db_connector.get_engine()

    # Load the new config
    with open("init_data_postgres/config/file_config.json", "r") as f:
        config = json.load(f)

    # Instantiate each specific DataLoader
    client_loader = ClientDataLoader(
        engine, config["clients"]["excel"], config["clients"]["mapping"]
    )
    product_loader = ProductDataLoader(
        engine, config["products"]["excel"], config["clients"]["mapping"]
    )
    order_loader = OrderDataLoader(
        engine, config["orders"]["excel"], config["orders"]["mapping"]
    )

except FileNotFoundError as fnf_error:
    print(f"File not found: {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error in JSON decoding: {json_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# # Process each DataLoader
# for loader in [client_loader, product_loader, order_loader]:
#     loader.load_excel()
#     loader.apply_column_transformation()
#     loader.clean_data()
#     loader.load_data(loader.table_name, loader.schema)

client_loader.load_excel()
client_loader.apply_column_transformation()
client_loader.clean_data()
client_loader.load_data(client_loader.table_name, client_loader.schema)
