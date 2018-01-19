# sandp500
a project to create Standard and Poor 500 database 
code samples create databse from csv files. database is copy of daily price data of S&P500. 
i added a table file from database. the database can befound at sftp netuser@hawksresearch.com. Password secret_pass_word .





Install mariadb.
Create a database called sandp then create user called sftp_user with password. Grant user all rights on database . Load database with user and password "pass_secret" . Should be able to cut and paste commands below;

sftp netuser@hawksresearch.com
 password = secret_pass_word
cd downloads/
get sqldump.sql 
get sqldumphash.txt;

yum install mariadb mariadb-server;

systemctl restart  mariadb ;
type mysql ;
help grant;
create database sandp;
create user 'sftp_user'@'localhost' identified by 'pass_secret';
grant all on sandp.* to 'sftp_user'@'localhost';
mysql -u sftp_user -p sandp < sqldump.sql ;







i offer it with a humble request that if you find code usefull donate to my paypal account. Thanks !     PayPal.Me/Ralph423
 
