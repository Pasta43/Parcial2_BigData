import boto3
destinationBucket="yahoofinancesbigdata2021"

def handler(event,context):
    """
    Function that handles an s3 upload event.

    Parameters:
    - event: that contains the information about the event.
    - context: that represents the execution context of the lambda function
    """
    repairTable()

def repairTable():

    client = boto3.client('athena')

    config = {
        'OutputLocation': 's3://' + destinationBucket + '/',
        'EncryptionConfiguration': {'EncryptionOption': 'SSE_S3'}

    }

    # Query Execution Parameters
    sql = 'MSCK REPAIR TABLE finances.finances'
    context = {'Database': 'finances'}

    client.start_query_execution(QueryString = sql, 
                                 QueryExecutionContext = context,
                                 ResultConfiguration = config)