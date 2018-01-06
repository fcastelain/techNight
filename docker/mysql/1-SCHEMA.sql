drop schema if exists `iterator-db`;
create schema if not exists `iterator-db`;
use `iterator-db`;

drop table if exists history;
drop table if exists cursor;

create table history (
    id              bigint not null auto_increment,
    action          varchar(255),
    actionTime      timestamp
);

create table cursor (
    state int
)
