import requests
import boto3
import time

bucket="newsdata202110"
def handler(event,context):
	"""
    Function that handles an s3 upload event.

    Parameters:
    - event: that contains the information about the event.
    - context: that represents the execution context of the lambda function
    """
	localtime=time.localtime()
	print("Getting html content...")
	
	s3 = boto3.resource('s3')
	print("Loading in s3...")
	getHTMLNewspaper("El_tiempo","https://www.eltiempo.com/",localtime,bucket,s3)
	getHTMLNewspaper("El_espectador","https://www.elespectador.com/",localtime,bucket,s3)
	print("files uploaded!")
	return {
			"status_code":200
		}

def getHTMLNewspaper(name, url,localtime,bucketname,s3):	
	"""
	Function that saves a html file from a newspaper web page in a s3 bucket.

	Parameters:
	- name: that contains the newspaper web page name
	- url: that contains the newspaper web page url
	- localtime: that contains an instance of localtime from time package
	- bucketname: that contains the bucketname where the page will be saved.
	- s3:that contains a boto3 resource instance to manage s3
	"""
	r = requests.get(url)
	print("Creating temporaly file...")
	filepath="/tmp/"+name+".html"
	f = open(filepath,"w")
	print("Saving file from "+name)
	f.write(r.text)
	f.close()
	data={
		'file':filepath,
		'bucket':bucketname,
		'path':'headlines/raw/newspaper='+name+'/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/'+str(localtime.tm_hour)+str(localtime.tm_min)+str(localtime.tm_sec)+'page.html'
	}
	s3.meta.client.upload_file(data['file'],data['bucket'] , data['path'])