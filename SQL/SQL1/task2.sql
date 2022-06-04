-- select *
-- from startups;

--#2

-- select count(*)
-- from startups;

--3
-- select sum(valuation)
-- from startups;

--4

-- select max(raised)
-- from startups;

--5

select max(raised)
from startups
where stage = 'Seed';


--6

select min(founded)
from startups;

--7

select avg(valuation)
from startups;

--8

select category,avg(valuation)
from startups
group by category;

--9

select category,round(avg(valuation),2)
from startups
group by category;

--10

select category, round(avg(valuation),2)
from startups
group by 1
order by 2 desc;

--11

select category, count(*)
from startups
group by category;

--12

select category , count(*)
from startups
group by category
having count(*) > 3
order by 2 desc;

--13

SELECT location, AVG(employees)
FROM startups
GROUP BY location;

--14

SELECT location, AVG(employees)
FROM startups
GROUP BY location
having avg(employees) > 500;



