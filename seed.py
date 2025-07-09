import os

folders = [
    "dags",
    "data/raw",
    "data/processed",
    "logs",
    "scripts",
    "configs",
    "notebooks"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Optional: Create starter files
open("requirements.txt", "a").close()
open(".env", "a").close()
open("README.md", "a").close()

print("Folder structure created.")


"""
Folder/File	         Purpose
dags/	             If using Airflow, place DAG definitions here
data/raw/	         Save unprocessed scraped files here (HTML, JSON, etc.)
data/processed/	     Save cleaned and formatted data (CSV, parquet, etc.)
scripts/	         Core scraping and transformation scripts
configs/	         YAML/JSON files with headers, proxy config, URLs to scrape
logs/	             Logging output for tracking scrape status and errors
.env	             Store secrets like API keys or proxy settings (use python-dotenv)
notebooks/	         For experimentation, quick tests, or reports
requirements.txt	 List your pip packages (requests, pandas, bs4, etc.)

"""