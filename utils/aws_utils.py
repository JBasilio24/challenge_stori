import boto3

def read_csv_from_s3(bucket_name, file_name):
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    csv_content = response['Body'].read().decode('utf-8')
    return csv_content

def send_email(sender, recipients, subject, body):
    ses_client = boto3.client('ses', region_name='us-east-2')
    response = ses_client.send_email(
        Source=sender,
        Destination={'ToAddresses': recipients},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Html': {'Data': body}}
        }
    )
    return response