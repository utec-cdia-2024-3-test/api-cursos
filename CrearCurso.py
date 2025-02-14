import boto3

def lambda_handler(event, context):
    # Entrada (json)
    print(event) # Log en CloudWatch    
    curso = event['body']
    print(curso) # Log en CloudWatch    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cursos')
    response = table.put_item(Item=curso)
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
