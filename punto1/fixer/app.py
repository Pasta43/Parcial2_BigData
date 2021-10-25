import boto3
import ntpath
destinationBucket="yahoofinances2021bigdataresults"

def handler(event,context):
    """
    Function that handles an s3 upload event.

    Parameters:
    - event: that contains the information about the event.
    - context: that represents the execution context of the lambda function
    """
    bucketName= event['Records'][0]['s3']['bucket']['name']
    fileName=event['Records'][0]['s3']['object']['key']
    fileName=fileName.replace('%3D','=')
    s3 = boto3.resource('s3')
    justFileName=ntpath.basename(fileName)   
    s3.meta.client.download_file(bucketName, fileName, '/tmp/'+justFileName)
    s3.meta.client.upload_file('/tmp/'+justFileName, destinationBucket,fileName)
    repairTable()

def repairTable():

    client = boto3.client('athena')

    config = {
        'OutputLocation': 's3://' + destinationBucket + '/stocks',
        'EncryptionConfiguration': {'EncryptionOption': 'SSE_S3'}

    }

    # Query Execution Parameters
    sql = 'MSCK REPAIR TABLE finances.finances'
    context = {'Database': 'finances'}

    client.start_query_execution(QueryString = sql, 
                                 QueryExecutionContext = context,
                                 ResultConfiguration = config)