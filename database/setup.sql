create user if not exists 'auth'@'localhost';
set password for 'auth'@'localhost' = 'systemdb';
create database if not exists auth;
grant all on auth.* to 'auth'@'localhost';

create user if not exists 'api'@'localhost';
set password for 'api'@'localhost' = 'systemdb';
create database if not exists api;
grant all on api.* to 'api'@'localhost';
