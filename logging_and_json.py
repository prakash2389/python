import os
import json
import logging
from datetime import datetime

# Setup basic logging
def setup_logger(log_file="app.log"):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger()

# Read a JSON file
def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Write data to a JSON file
def write_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# Get current timestamp
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Check if a file exists
def file_exists(file_path):
    return os.path.exists(file_path)
