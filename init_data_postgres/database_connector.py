from sqlalchemy import create_engine
import json


class DatabaseConnector:
    def __init__(self, config_path):
        # Load database configuration from a JSON file
        with open(config_path, "r") as f:
            self.db_config = json.load(f)

        # Create the engine using the loaded configuration
        self.engine = create_engine(
            self.db_config["database_url"],
            echo=False,  # Set to False when you don't need the log output
        )

    def get_engine(self):
        # Return the engine to be used elsewhere in the application
        return self.engine
