# Write your MySQL query statement below
SELECT u.name, SUM(IF(r.distance IS NULL, 0, r.distance)) as travelled_distance FROM Users u
LEFT JOIN Rides r ON
u.id = r.user_id
GROUP BY u.name
ORDER BY travelled_distance DESC, u.name ASC;