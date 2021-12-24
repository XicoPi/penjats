use api;

create table if not exists users (
       user_id int UNSIGNED primary key auto_increment,
       username char(20) unique not null,
       email varchar(100) unique not null,
       pwd_hash text not null,
       pwd_salt char(32) not null,
       firstname varchar(40) not null,
       surname varchar(40) not null,
       secondsurname varchar(40),
       user_type char(10)
);
