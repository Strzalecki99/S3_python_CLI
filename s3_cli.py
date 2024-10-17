import boto3
import re
import argparse
from botocore.exceptions import NoCredentialsError, ClientError

def get_s3_client() -> boto3.client:
    try:
        s3 = boto3.client('s3')
        return s3
    except NoCredentialsError:
        print("AWS credentials not found.")
        exit(1)

def list_files(bucket_name : str, prefix : str = "") -> None:
    s3 = get_s3_client()
    try:
        response = s3.list_objects_v2(Bucket = bucket_name, Prefix = prefix)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f"No files found in bucket '{bucket_name}' with prefix '{prefix}'")
    except ClientError as e:
        print(f"Error: {e}")

def upload_file(file_name : str, bucket_name : str, destination : str) -> None:
    s3 = get_s3_client()
    try:
        s3.upload_file(file_name, bucket_name, destination)
        print(f"File '{file_name}' uploaded to '{bucket_name}/{destination}'")
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except NoCredentialsError:
        print("Credentials not found.")
    except ClientError as e:
        print(f"Error: {e}")

def list_files_with_regex(bucket_name : str, prefix : str, pattern : str) -> None:
    s3 = get_s3_client()
    try:
        response = s3.list_objects_v2(Bucket = bucket_name, Prefix = prefix)
        if 'Contents' in response:
            for obj in response['Contents']:
                if re.match(pattern, obj['Key']):
                    print(obj['Key'])
        else:
            print(f"No files found in bucket '{bucket_name}' with prefix '{prefix}'")
    except NoCredentialsError:
        print("Credentials not found.")
    except ClientError as e:
        print(f"Error: {e}")

def delete_files_with_regex(bucket_name : str, prefix : str, pattern : str):
    s3 = get_s3_client()
    try:
        response = s3.list_objects_v2(Bucket = bucket_name, Prefix = prefix)
        if 'Contents' in response:
            for obj in response['Contents']:
                if re.match(pattern, obj['Key']):
                    s3.delete_object(Bucket = bucket_name, Key = obj['Key'])
                    print(f"Deleted: {obj['Key']}")
        else:
            print(f"No files found in bucket '{bucket_name}' with prefix '{prefix}'")
    except NoCredentialsError:
        print("Credentials not found.")
    except ClientError as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description = "Python CLI to interact with S3 bucket")
    
    subparsers = parser.add_subparsers(dest = "command")

    # List files
    list_parser = subparsers.add_parser('list', help = "List all files in S3 bucket")
    list_parser.add_argument('--bucket', required = True, help = "S3 bucket name")
    list_parser.add_argument('--prefix', required = False, default = "", help = "Prefix (folder) in the bucket")
    
    # Upload file
    upload_parser = subparsers.add_parser('upload', help = "Upload a file to S3")
    upload_parser.add_argument('--file', required = True, help = "File to upload")
    upload_parser.add_argument('--bucket', required = True, help = "S3 bucket name")
    upload_parser.add_argument('--dest', required = True, help = "Destination path in the bucket")
    
    # List files with regex
    regex_list_parser = subparsers.add_parser('list-regex', help = "List files in S3 matching a regex")
    regex_list_parser.add_argument('--bucket', required = True, help = "S3 bucket name")
    regex_list_parser.add_argument('--prefix', required = False, default = "", help = "Prefix (folder) in the bucket")
    regex_list_parser.add_argument('--pattern', required = True, help = "Regex pattern to match")
    
    # Delete files with regex
    delete_parser = subparsers.add_parser('delete-regex', help = "Delete files in S3 matching a regex")
    delete_parser.add_argument('--bucket', required = True, help = "S3 bucket name")
    delete_parser.add_argument('--prefix', required = False, default = "", help = "Prefix (folder) in the bucket")
    delete_parser.add_argument('--pattern', required = True, help = "Regex pattern to match")

    args = parser.parse_args()

    if args.command == 'list':
        list_files(args.bucket, args.prefix)
    elif args.command == 'upload':
        upload_file(args.file, args.bucket, args.dest)
    elif args.command == 'list-regex':
        list_files_with_regex(args.bucket, args.prefix, args.pattern)
    elif args.command == 'delete-regex':
        delete_files_with_regex(args.bucket, args.prefix, args.pattern)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
