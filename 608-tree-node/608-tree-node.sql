# Write your MySQL query statement below
select id ,if(isnull(p_id),'Root' ,if (id in(select p_id from tree),'Inner','Leaf')) as type from tree order by id
