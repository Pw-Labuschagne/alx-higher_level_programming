-- Creates a user: user_0d_1 with some attributes
CREATE USER IF NOT EXISTS 'user_0d_01'@'localhost' IDENTIFIED WITH 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1@localhost';

