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