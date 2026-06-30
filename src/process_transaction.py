import json
import boto3
import uuid
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
sqs = boto3.client('sqs')

def lambda_handler(event, context):
    try:
        # Parse incoming API Gateway payload
        body = json.loads(event.get('body', '{}'))
        
        transaction_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        
        # 1. Prepare data for DynamoDB
        item = {
            'transaction_id': transaction_id,
            'sender_name': body.get('sender_name', 'System'),
            'receiver_name': body.get('receiver_name', 'System'),
            'amount': body.get('amount', 0),
            'status': 'SUCCESS',
            'timestamp': timestamp
        }
        
        # 2. Write to DynamoDB Ledger
        table_name = os.environ.get('DYNAMO_TABLE', 'olupay-transactions-ledger')
        table = dynamodb.Table(table_name)
        table.put_item(Item=item)
        
        # 3. Queue message in SQS for the Auditor Lambda
        queue_url = os.environ.get('SQS_QUEUE_URL', 'https://sqs.us-east-1.amazonaws.com/123456789012/audit-queue')
        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(item)
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Transaction processed securely.',
                'transaction_id': transaction_id
            })
        }
        
    except Exception as e:
        # This is where your CloudWatch alarm would catch the failure
        print(f"[ERROR] Transaction failed: {str(e)}")
        raise e
