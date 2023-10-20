-- Creates the database hbtn_0d_2 and the user user_0d_2.
-- The user_0d_2 password should be set to user_0d_2_pwd.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT privileges.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
