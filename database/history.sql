use api;
create table if not exists history_entries (
       entry_id int UNSIGNED primary key auto_increment,
       title text not null,
       content text not null,
       creation_date timestamp not null,
       author_id int UNSIGNED references users
);
