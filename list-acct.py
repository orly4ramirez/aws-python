import boto3
import json

def lambda_handler(event, context):
    # List of AWS account IDs or aliases
    aws_accounts = ["account1", "account2", "account3"]  # Add your account IDs or aliases here

    # Initialize an empty list to store user information
    all_users = []

    for account in aws_accounts:
        try:
            # need to add credentials with assumerole here...
            # Create an IAM client for each account
            iam_client = boto3.client('iam', region_name='us-east-1', aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY')

            # Retrieve the list of users for the account
            response = iam_client.list_users()
            users = response['Users']

            # Extract relevant user information
            for user in users:
                user_info = {
                    "Account": account,
                    "UserName": user['UserName'],
                    "UserId": user['UserId'],
                    "Arn": user['Arn'],
                    "CreateDate": str(user['CreateDate'])
                }
                all_users.append(user_info)

        except Exception as e:
            print(f"Error fetching users for account {account}: {str(e)}")

    # Return the list of users as JSON
    return json.dumps(all_users, default=str)

# Note: Replace 'YOUR_ACCESS_KEY' and 'YOUR_SECRET_KEY' with your actual credentials
