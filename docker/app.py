import boto3
import time
import os

db_params = {
    "database": os.getenv("DB_NAME"),
    "dbUser": os.getenv("DB_USER"),
    "dbPassword": os.getenv("DB_PASSWORD"),
    "clusterIdentifier": os.getenv("CLUSTER_IDENTIFIER"),
    "secretArn": os.getenv("SECRET_ARN"),
}

file_paths = [
    'docker/select_query.sql'
]

def execute_queries_from_files(file_paths, db_params):

    """
    Execute SQL queries loaded from the provided file paths using the given database parameters.

    Parameters:
    - file_paths (list of str): List of paths to the SQL files.
    - db_params (dict): Dictionary containing the database connection parameters such as dbname, user, password, host, etc.

    Returns:
    Success code and 'Queries ran successfully!' message.
    """

    try:
        redshift_data = boto3.client('redshift-data')
        
        for file_path in file_paths:
            try:
                with open(file_path, 'r') as file:
                    query = file.read()

                print(f"Executing query from file: {file_path}")  # Logging start of execution

                response = redshift_data.execute_statement(
                    ClusterIdentifier=db_params['clusterIdentifier'],
                    Database=db_params['database'],
                    DbUser=db_params['dbUser'],
                    Sql=query,
                    SecretArn=db_params['secretArn']
                )

                query_id = response['Id']
                done = False
                while not done:
                    status_description = redshift_data.describe_statement(Id=query_id)
                    status = status_description['Status']
                    if status in ['FINISHED', 'FAILED', 'ABORTED']:
                        done = True
                    else:
                        time.sleep(1)  # wait for a second before checking the status again
                    
                print(f"Finished executing query from {file_path}. Status: {status}")

            except FileNotFoundError:
                print(f"File not found: {file_path}")
            except Exception as e:
                print(f"Failed to execute query from file: {file_path}. Error: {e}")

    except Exception as e:
        print(f"Failed to connect or execute queries. Error: {e}")

def lambda_handler(event, context):
    execute_queries_from_files(file_paths, db_params)

    return {
        'statusCode': 200,
        'body': 'Queries ran successfully!'
    }

