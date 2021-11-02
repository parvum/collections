import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employee-wahaj')

def lambda_handler(event, context):

    employee_id = event['employee_id']
    last_name = event['last_name']

    UpdateExpression = 'SET last_name = :val1'
    ExpressionAttributeValues = {':val1': last_name }


    if 'first_name' in event:
        
        first_name= event['first_name']
        UpdateExpression = 'SET last_name = :val1, first_name = :val2'
        ExpressionAttributeValues = {
                ':val1': last_name,
                ':val2': first_name
            }

    update = table.update_item(
        Key={
            'employee_id': employee_id
        },
        ConditionExpression= 'attribute_exists(employee_id)',
        UpdateExpression=UpdateExpression,
        ExpressionAttributeValues=ExpressionAttributeValues
    )
