SELECT * FROM trips;
 
SELECT * FROM riders;
 
SELECT * FROM cars;

--3

select * from riders
cross join cars;

--4

select * from trips

left join riders
on trips.id = riders.id;

--5
select * from trips
INNER JOIN cars 
  on trips.id = cars.id;


--6
select avg(cost)
from trips;

--7

select *
from riders
where total_trips< 500;

--8
select *
from cars
where status is 'active';

--9


SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;







