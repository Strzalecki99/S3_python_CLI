# S3 File Management CLI

A simple command-line interface (CLI) for managing files in an AWS S3 bucket. This CLI allows you to list files, upload files, filter files using regex, and delete files matching specified regex from a specified S3 bucket.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)

## Features

- List all files in a specified S3 bucket.
- Upload local files to a defined location in the S3 bucket.
- List files in an S3 bucket that match a given regex filter.
- Delete all files matching a regex from the S3 bucket.

## Requirements

- Python 3.x
- Boto3 library
- AWS credentials with access to the specified S3 bucket

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Strzalecki99/S3_python_CLI.git
   cd S3_python_CLI
   ```

2. **Set Up a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source .venv/bin/activate
    ```

3. **Install Required Packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Export AWS Credentials:**
    ```bash
    export AWS_ACCESS_KEY_ID='your-access-key-id'
    export AWS_SECRET_ACCESS_KEY='your-secret-access-key'
    export AWS_DEFAULT_REGION='region'  # e.g., eu-central-1
    ```

## Usage

The CLI is implemented in a Python script, and you can run it from the command line. Below are the commands for each functionality.

### Command-Line Interface:

1. **List Files in an S3 Bucket:**

   ```bash
   python3 s3_cli.py list --bucket <bucket-name> --prefix <directory>
   ```

2. **Upload a Local File:**

    ```bash
    python3 s3_cli.py upload --file <file> --bucket <bucket-name> --dest <destination-path-in-bucket>
    ```

3. **List Files Matching a Regex:**

    ```bash
    python3 s3_cli.py list-regex --bucket <bucket-name> --prefix <directory> --pattern <your-regex>
    ```

4. **Delete Files Matching a Regex:**

    ```bash
    python3 s3_cli.py delete-regex --bucket <bucket-name> --prefix <directory> --pattern <your-regex>
    ```

### Command-Line Options:

```
--bucket: Specifies the name of the S3 bucket.
--prefix: Specifies the prefix (directory) within the S3 bucket.
--file: The local file path to upload.
--dest: The S3 path where the file will be stored.
--pattern: The regex pattern to filter files.
```

## Examples:

**Assumaing that:**
- S3 bucket name = 'developer_task2'
- prefix = 'TIE-rp' 


1. **To list all files in the specified bucket:**

    ```bash
    python3 s3_cli.py list --bucket developer-task2 --prefix TIE-rp/
    ```

2. **To upload a files named test3.txt and test3_1.txt:**

    ```bash
    python3 s3_cli.py upload --file test3.txt --bucket developer-task2  --dest TIE-rp/test3.txt
    ```
    
    ```bash
    python3 s3_cli.py upload --file test3_1.txt --bucket developer-task2  --dest TIE-rp/test3_1.txt
    ```

3. **To list files containing the number 3:**

    ```bash
    python3 s3_cli.py list-regex --bucket developer-task2 --prefix TIE-rp --pattern '.*3.*'
    ```

4. To delete files containing the number 3:

    ```bash
    python3 s3_cli.py delete-regex --bucket developer-task2 --prefix TIE-rp --pattern '.*3.*'
    ```