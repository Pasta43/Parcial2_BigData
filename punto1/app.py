import requests
import boto3
from datetime import date

def handler(event,context):
	today = date.today()
	print(today)
	r = requests.get('https://www.eltiempo.com/')
	
	print("Fecha")
	f = open("/tmp/newspaper.html","w")
	f.write(r.text)
	f.close()
	print("Guardo página")
	s3 = boto3.resource('s3')
	print("Cargo s3")
	s3.meta.client.upload_file('/tmp/newspaper.html', 'newsdata202110', 'newspaper/stage/year='+str(today.year)+'/month='+str(today.month)+'/day='+str(today.day)+'/page.html')
	print("Subo en bucket")
	return {
			"status_code":200
		}
