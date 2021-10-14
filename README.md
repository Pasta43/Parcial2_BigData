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
Have fun!

