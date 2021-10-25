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
) LOCATION 's3://yahoofinancesbigdata2021/stocks'
TBLPROPERTIES ('has_encrypted_data'='false',
'skip.header.line.count'='1');