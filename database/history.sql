use api;
create table if not exists history_entries (
       id int UNSIGNED primary key auto_increment,
       title text not null,
       content not null,
       user_id references users
);
