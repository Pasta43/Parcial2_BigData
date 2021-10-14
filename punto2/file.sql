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