create database sensedata;

create table hatdata (
	id int not null AUTO_INCREMENT,
    createdate datetime,
    temp double,
    primary key (id))
    

select * from hatdata;

drop table hatdata;