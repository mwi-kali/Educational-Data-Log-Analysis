/*
  File: monthly_usage.sql
  Author: Mwikali Muoki
  Date: 2025-04-09
  Description:
    This script calculates the monthly usage time for confirmed and non-deleted learners.
    It joins the log table (mdl_logstore_standard_log) with the user table (mdl_user) and sums up session durations.
    It assumes that the log table has a 'duration' column representing the session length and the user table has
    'confirmed' and 'deleted' status flags.
*/

-- Calculate monthly usage time (in seconds or minutes, based on your 'duration' unit)
SELECT 
    DATE_TRUNC('month', TO_TIMESTAMP(l.timecreated)) AS month,
    SUM(l.duration) AS total_usage_time
FROM mdl_logstore_standard_log l
JOIN mdl_user u ON l.userid = u.id
WHERE u.confirmed = 1
  AND u.deleted = 0
GROUP BY month
ORDER BY month;

-- Include the number of sessions and average session duration per month.
SELECT 
    DATE_TRUNC('month', TO_TIMESTAMP(l.timecreated)) AS month,
    COUNT(*) AS session_count,
    SUM(l.duration) AS total_usage_time,
    AVG(l.duration) AS average_session_duration
FROM mdl_logstore_standard_log l
JOIN mdl_user u ON l.userid = u.id
WHERE u.confirmed = 1
  AND u.deleted = 0
GROUP BY month
ORDER BY month;
