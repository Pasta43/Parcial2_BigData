# Parcial2_BigData
This is the solution for the exam.
you have the requirements.txt, that contains all the necessary packages to use this project. 


You should to use an virtual environment to execute this project. To test it you have to change your .aws/credentials file and the bucket names. 

## punto2

This folder contains:
* a reader, that is used for request an html page (El Tiempo and El Espectador newspaper) and save it in a s3 bucket.
* a scrapper, that process the page, and save the results in another s3 bucket.

And for this item:

* The bucket to save html files is: arn:aws:s3:::newsdata202110
* The bucket to save csv files is: arn:aws:s3:::resultsnewspaperbucket

The unit tests for the scrapper function are in scrapper/test folder 

To make queries can you use Aws athena

```sql
CREATE EXTERNAL TABLE news(
  title string, 
  section string, 
  url string)
 PARTITIONED BY ( 
  newspaper string,
  year int,
  month int,
  day int)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://resultsnewspaperbucket/news/final'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'transient_lastDdlTime'='1634184844',
  'skip.header.line.count'='1')

MSCK REPAIR TABLE news;
```

Have fun!

