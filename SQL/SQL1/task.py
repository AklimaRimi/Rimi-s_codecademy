create table friends(
  id INTEGER,
  name TEXT,
  birthday DATE
);

--2
insert into friends(id,name,birthday) values (1,'Ororo Munroe','1940-05-30');

--3
select * 
from friends;

--4
insert into friends(id,name,birthday) values (2,'aklima rimi','1998-01-24');

insert into friends(id,name,birthday) values (3,'afia archie','1999-12-07');

select * 
from friends;

--5

update friends
set name = 'storm' 
where id is 2;
select * 
from friends;

--6
alter table friends
add column email text;
select * 
from friends;


--7

update friends 
set email = 'storm@codecademy.com'
where id is 2;
select * 
from friends;

--8

delete from friends
where id is 2;
select * 
from friends;






