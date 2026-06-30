import json
import boto3
import os
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = os.environ.get('REPORTS_BUCKET', 'olupay-financial-reports')
    
    # Process batch of messages from SQS
    for record in event.get('Records', []):
        try:
            payload = json.loads(record['body'])
            tx_id = payload.get('transaction_id')
            
            # Generate the Audit Report content
            report_content = (
                f"=== OLUPAY TRANSACTION AUDIT ===\n"
                f"Transaction ID: {tx_id}\n"
                f"Sender: {payload.get('sender_name')}\n"
                f"Receiver: {payload.get('receiver_name')}\n"
                f"Amount: NGN {payload.get('amount')}\n"
                f"Settlement Status: VERIFIED\n"
                f"Audit Time: {datetime.utcnow().isoformat()} UTC\n"
            )
            
            file_key = f"audits/audit_{tx_id}.txt"
            
            # Export report to S3
            s3.put_object(
                Bucket=bucket_name,
                Key=file_key,
                Body=report_content
            )
            
            print(f"[SUCCESS] Audit report {file_key} saved to S3.")
            
        except Exception as e:
            print(f"[ERROR] Failed to audit record: {str(e)}")
            raise e
            
    return {
        'statusCode': 200,
        'body': json.dumps('Audit batch processing complete.')
    }
