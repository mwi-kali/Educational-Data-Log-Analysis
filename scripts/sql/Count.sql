-- SQL script to count 
--


--
-- The number of tables 
--

select count(*) as all_tables 
from information_schema.tables;

-- Exact number of tables
select count(*) as base_tables 
from information_schema.tables 
where table_type = 'BASE TABLE';

-- Number of public tables
select count(*) as public_tables
from information_schema.tables
where table_schema = 'public';

-- List tables 
SELECT table_schema,table_name
FROM information_schema.tables
ORDER BY table_schema,table_name;

--
-- The number of records in each of the tables given in the MIT section
--
select count(*) 
from mdl_logstore_standard_log;

select count(*) 
from mdl_context;

select count(*) 
from mdl_user;

select count(*) 
from mdl_course;

select count(*) 
from mdl_modules;

select count(*) 
from mdl_course_modules;

select count(*) 
from mdl_course_modules_completion;

select count(*) 
from mdl_grade_items;

select count(*) 
from mdl_grade_grades;

select count(*) 
from mdl_grade_categories;

select count(*) 
from mdl_grade_items_history;

select count(*) 
from mdl_grade_grades_history;

select count(*) 
from mdl_grade_categories_history;

select count(*) 
from mdl_forum;

select count(*) 
from mdl_forum_discussions;

select count(*) 
from mdl_forum_posts;

--
--Number of quiz submissions by hour of day
--

select  date_part('hour', timestamp with time zone 'epoch' + timefinish * interval '1 second') as hour, count(1)
from mdl_quiz_attempts qa
where qa.preview = 0 and qa.timefinish <> 0
group by date_part('hour', timestamp with time zone 'epoch' + timefinish * interval '1 second')
order by hour

--
-- Monthly usage time of learners who have confirmed and are not deleted
--
select extract(month from to_timestamp(mdl_stats_user_monthly.timeend)) as calendar_month,
    count(distinct mdl_stats_user_monthly.userid) as total_users
from mdl_stats_user_monthly
    inner join mdl_role_assignments on mdl_stats_user_monthly.userid = mdl_role_assignments.userid
    inner join mdl_context on mdl_role_assignments.contextid = mdl_context.id
where mdl_stats_user_monthly.stattype = 'activity'
    and mdl_stats_user_monthly.courseid <>1
group by extract(month from to_timestamp(mdl_stats_user_monthly.timeend))
order by extract(month from to_timestamp(mdl_stats_user_monthly.timeend))

--
--Count of log events per user
--

-- loggedin
select u.id, count(*) as logincount
from mdl_logstore_standard_log l
join mdl_user u on u.id = l.userid
where action = 'loggedin'
group by u.id

-- viewed
select u.id, count(*) as logincount
from mdl_logstore_standard_log l
join mdl_user u on u.id = l.userid
where action = 'viewed'
group by u.id

--started
select u.id, count(*) as logincount
from mdl_logstore_standard_log l
join mdl_user u on u.id = l.userid
where action = 'started'
group by u.id

--submitted
select u.id, count(*) as logincount
from mdl_logstore_standard_log l
join mdl_user u on u.id = l.userid
where action = 'submitted'
group by u.id

--uploaded
select u.id, count(*) as logincount
from mdl_logstore_standard_log l
join mdl_user u on u.id = l.userid
where action = 'uploaded'
group by u.id

--updated
select u.id, count(*) as logincount
from mdl_logstore_standard_log l
join mdl_user u on u.id = l.userid
where action = 'updated'
group by u.id

-- searched
select u.id, count(*) as logincount
from mdl_logstore_standard_log l
join mdl_user u on u.id = l.userid
where action = 'searched'
group by u.id

--resumed
select u.id, count(*) as logincount
from mdl_logstore_standard_log l
join mdl_user u on u.id = l.userid
where action = 'resumed'
group by u.id

--answered
select u.id, count(*) as logincount
from mdl_logstore_standard_log l
join mdl_user u on u.id = l.userid
where action = 'answered'
group by u.id

--attempted
select u.id, count(*) as logincount
from mdl_logstore_standard_log l
join mdl_user u on u.id = l.userid
where action = 'attempted'
group by u.id

--abandoned
select u.id, count(*) as logincount
from mdl_logstore_standard_log l
join mdl_user u on u.id = l.userid
where action = 'abandoned'
group by u.id

