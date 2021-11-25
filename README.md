# bash_history_time_convert_csv
Convert the linux timestamp from .bash_history and save it as CSV file. Output CSV file will be created as bash_time_processed.csv

Requrenment : Python 3.x

How to run : python bash_convert_time.py [bash_history_file_location]
             Ex. python bash_convert_time.py .bash_history
             
Input file content : 

#1615888058
exit
#1615889218
df -h

Output file content :

#1615888058,2021-03-16 15:17:38,exit
#1615889218,2021-03-16 15:36:58,df -h
