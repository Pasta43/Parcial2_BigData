import boto3
import time
import requests

bucketname="yahoofinancesbigdata2021"
def handler(event,context):
    """
    Function that handles an s3 upload event.

    Parameters:
    - event: that contains the information about the event.
    - context: that represents the execution context of the lambda function
    """
    localtime=time.localtime()
    print("Getting html content...")
    tuples=generateUrls()
    s3 = boto3.resource('s3')
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
    for action,url in tuples:
        filepath='/tmp/'+action+'.csv'
        file = requests.get(url,headers=headers)
        csvFile=open(filepath, 'wb')
        csvFile.write(file.content)
        csvFile.close()
        
        data={
		'file':filepath,
		'bucket':bucketname,
		'path':'stocks/company='+action+'/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/'+str(localtime.tm_hour)+str(localtime.tm_min)+str(localtime.tm_sec)+'.csv'
	    }
        
        s3.meta.client.upload_file(data['file'],data['bucket'] , data['path'])
        time.sleep(2)
    return {
			"status_code":200
		}

def generateUrls():
    """Generates the urls for download
    """
    today=time.time()-2*86400
    yesterday = today-86400
    actions=['AVHOQ','EC','AVAL','CMTOY']
    return [(action,f"https://query1.finance.yahoo.com/v7/finance/download/{action}?period1={int(yesterday)}&period2={int(today)}&interval=1d&events=history&includeAdjustedClose=true") for action  in actions
    ]