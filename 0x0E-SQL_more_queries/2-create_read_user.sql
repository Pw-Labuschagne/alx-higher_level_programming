-- Creates a database named hbtn_0d_2 and user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2@localhost;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_pwd';

