import argparse
import json
import logging
import os
import pandas as pd
from sqlalchemy import create_engine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("file_upload.log"),
        logging.StreamHandler(),
    ],
)

parser = argparse.ArgumentParser()

parser.add_argument(
    "--source_dir",
    required=True,
    help="The source directory of the file to be uploaded",
)
parser.add_argument(
    "--mysql_details", required=True, help="The MySQL connection details"
)
parser.add_argument(
    "--destination_table",
    required=True,
    help="The name of the table where the file will be uploaded",
)

args = parser.parse_args()

logging.info("Source Directory: %s", args.source_dir)
logging.info("MySQL Details: %s", args.mysql_details)
logging.info("Destination Table: %s", args.destination_table)

with open(args.mysql_details, "r") as f:
    config = json.load(f)
logging.info("loaded config: %s", config)

engine = create_engine(
    f"mysql+mysqlconnector://{config['user']}:{config['password']}"
    f"@{config['mysql_ip']}:{config['port']}/{config['database']}"
)

if not os.path.isdir(args.source_dir):
    logging.error("invalid source directory")
    exit()
files = os.listdir(args.source_dir)

logging.info("MySQL Engine Created Successfully")
for file in files:
    if not file.endswith(".csv"):
        continue

    full_path = os.path.join(args.source_dir, file)

    try:
        logging.info("reading file: %s", file)
        df = pd.read_csv(full_path)

        if df.empty:
            logging.warning("file is empty, skipping: %s", file)
            continue

        df.to_sql(args.destination_table, con=engine, if_exists="append", index=False)
        logging.info("file uploaded successfully: %s", file)

    except Exception as e:
        logging.error("error uploading file: %s", file)
        logging.error("Error details: %s", e)