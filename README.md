# Project Title

This project is a data loading pipeline for a PostgreSQL database. It uses Python scripts to load data from Excel files into the database.

## Project Structure

- `init_data_postgres/`: Contains the Python scripts for loading data into the database.
  - `config/`: Contains JSON configuration files for the database and data loading.
  - `data_loader.py`: Contains the base DataLoader class.
  - `database_connector.py`: Contains the DatabaseConnector class for connecting to the PostgreSQL database.
  - `entity_data_loaders.py`: Contains DataLoader subclasses for loading specific entities (clients, products, orders) into the database.
  - `load_data_df.py`: The main script that uses the other modules to load data into the database.
- `postgres_container/`: Contains the PostgreSQL Docker container configuration.
- `postgres_scripts/`: Contains SQL scripts for creating the database schema.
- `data/`: Contains the Excel files with the data to be loaded into the database.
- `docker-compose.yaml`: Docker Compose configuration file for running the PostgreSQL and pgAdmin containers.
- `.gitignore`: Specifies which files and directories to ignore in Git.

## How to Run

1. Ensure Docker is installed and running.
2. Run `docker-compose up` in the project root directory to start the PostgreSQL and pgAdmin containers.
3. Run `python init_data_postgres/load_data_df.py` to load the data into the database.

## Logging

The application logs its output to `app.log`, which is located in the project root directory.

## Error Handling

The application handles file not found errors, JSON decoding errors, and other unexpected errors by printing an error message to the console.