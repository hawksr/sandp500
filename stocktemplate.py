

#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import MySQLdb as mdb
import argparse


# Obtain a database connection to the MySQL instance
db_host = 'localhost'
db_user = 'ralph'
db_pass = 'thriofch'
db_name = 'sandp'


parser = argparse.ArgumentParser()

parser.add_argument('-s', '--stock', type=str, help='ticker symbol', required=True)
args = parser.parse_args()
stock = args.stock
  

con = mdb.connect(db_host, db_user, db_pass, db_name)


def obtain_parse_wiki_snp500():







 

     

           
 
      
    with open('%s.csv' % stock ) as yf_data:
    
    # On failure, print an error message.
       
           
     for y in yf_data:
                                       
        prices = []
             
        p = y.rstrip('\n')
        p = y.strip().split(',')
        prices.append( (
                 ("%s" % stock), p[0], p[1], p[2], p[3], p[4],p[5] ) )
      
       
        print prices 

       

  # Create the insert strings
        column_str = """symbol,date,close,volume,open,high,low"""
        insert_str = ("%s, " * 7)[:-2]
        final_str = "INSERT INTO daily_closes(%s) VALUES (%s)" % (column_str, insert_str)
     
   
  # Using the MySQL connection, carry out an INSERT INTO for every symbol
        with con: 
         cur = con.cursor()
         cur.executemany(final_str, prices)
         print prices






if __name__ == "__main__":
  prices = obtain_parse_wiki_snp500()


 





