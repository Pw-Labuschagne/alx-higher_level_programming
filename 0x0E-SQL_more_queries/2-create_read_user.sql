-- Creates a database named hbtn_0d_2 and user_0d_2
CREATE IF NOT EXISTS hbtn_0d_2@localhost;
CREATE IF NOT EXISTS 'user_0d_2'@'hbtn_0d_2' IDENTIFIED BY 'user_0d_2pwd';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_pwd';

