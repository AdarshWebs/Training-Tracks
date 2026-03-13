# Python Assignment – File Upload Utility

## Overview

This utility reads CSV files from a specified directory and uploads the data into a MySQL table.
The script uses **Python, Pandas, MySQL, JSON configuration, and argparse** to automate the data upload process.

## Technologies Used

* Python
* Pandas
* MySQL
* SQLAlchemy
* argparse
* JSON

## Project Structure

```
python/
│
├── file_upload.py          # Main script to upload CSV files to MySQL
├── connection.py           # MySQL connection helper
│
├── data/
│   └── students1.csv       # Sample CSV file used for upload
```

## Prerequisites

Install the required Python libraries:

```
pip install pandas sqlalchemy mysql-connector-python
```

Ensure **MySQL is installed and running**.

## Configuration

Create a file named `config.json` with your MySQL connection details:

```
{
  "mysql_ip": "localhost",
  "port": 3306,
  "user": "root",
  "password": "your_password",
  "database": "practice_db"
}
```

⚠️ This file is ignored in Git to protect credentials.

## Usage

Run the script using:

```
python file_upload.py \
--source_dir data \
--mysql_details config.json \
--destination_table students
```

### Arguments

| Argument              | Description                                           |
| --------------------- | ----------------------------------------------------- |
| `--source_dir`        | Directory containing CSV files                        |
| `--mysql_details`     | Path to JSON file containing MySQL connection details |
| `--destination_table` | MySQL table where data will be inserted               |

## Process Flow

1. Parse command line arguments.
2. Load MySQL configuration from JSON file.
3. Establish connection to MySQL database.
4. Read all CSV files from the specified directory.
5. Convert CSV data into Pandas DataFrame.
6. Upload the data into the destination MySQL table.

## Output

Logs are printed in the console and saved to:

```
file_upload.log
```

## Author

Adarsh Opalkar
