# Parcial2_BigData
This is the solution for the exam.
you have the requirements.txt, that contains all the necessary packages to use this project. 


You should to use an virtual environment to execute this project. To test it you have to change your .aws/credentials file and the bucket names. 

## punto1
This folder contains:
* a downloader, that is used for request an csv file from yahoo finances and save it in a s3 bucket.
* a fixer, that repairs an athena table.

And for this item:

The bucket to save files is: arn:aws:s3:::yahoofinancesbigdata2021 and they are reuploaded in arn:aws:s3:::yahoofinances2021bigdataresults

The unit tests for the downloader function are in test.py file

To make queries can you use Aws athena creating:

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS finances (
  date date,
  open double,
  high double,
  low double,
  close double,
  adj_close double,
  volume bigint
) PARTITIONED BY (
  company string,
  year int,
  month int,
  day int
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' 
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
) LOCATION 's3://yahoofinances2021bigdataresults/stocks'
TBLPROPERTIES ('has_encrypted_data'='false',
'skip.header.line.count'='1');

```
and repairing the table

``` sql
MSCK REPAIR TABLE finances;
```

Finally invoke the downloader
```zappa invoke dev app.handler```
## punto2

This folder contains:
* a reader, that is used for request an html page (El Tiempo and El Espectador newspaper) and save it in a s3 bucket.
* a scrapper, that process the page, and save the results in another s3 bucket.

And for this item:

* The bucket to save html files is: arn:aws:s3:::newsdata202110
* The bucket to save csv files is: arn:aws:s3:::resultsnewspaperbucket

The unit tests for the scrapper function are in scrapper/test folder 

To make queries can you use Aws athena creating:

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
```
and repairing the table:

```sql
MSCK REPAIR TABLE news;
```


To test the function, you have to invoke the reader with

```zappa invoke dev app.handler```


Have fun!


